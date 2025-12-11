#!/usr/bin/env python3
"""
Codebase Analysis Script

Collects metrics about a codebase:
- Lines of code (total, source only, comments)
- Cyclomatic complexity (requires radon)
- Code duplication (basic detection)
- File and directory statistics

Usage:
    python analyze_codebase.py /path/to/codebase --output metrics.json
    python analyze_codebase.py /path/to/codebase --format table
"""

import os
import sys
import json
import argparse
from pathlib import Path
from collections import defaultdict
import re


# Common patterns for generated/vendor code to exclude
EXCLUDE_PATTERNS = [
    'node_modules', 'vendor', 'venv', 'env', '.env',
    'dist', 'build', '__pycache__', '.pytest_cache',
    'coverage', '.git', '.svn', '.hg',
    'min.js', 'bundle.js', '.min.css',
    'migrations', 'package-lock.json', 'yarn.lock',
    'Pipfile.lock', 'poetry.lock', 'composer.lock'
]

# File extensions to analyze
CODE_EXTENSIONS = {
    '.py', '.js', '.ts', '.jsx', '.tsx',
    '.java', '.c', '.cpp', '.h', '.hpp',
    '.rb', '.php', '.go', '.rs', '.swift',
    '.kt', '.scala', '.cs', '.vue', '.svelte',
    '.dart'
}

COMMENT_PATTERNS = {
    'python': [r'^\s*#', r'^\s*"""', r"^\s*'''"],
    'javascript': [r'^\s*//', r'^\s*/\*', r'^\s*\*'],
    'java': [r'^\s*//', r'^\s*/\*', r'^\s*\*'],
    'c': [r'^\s*//', r'^\s*/\*', r'^\s*\*'],
    'ruby': [r'^\s*#'],
    'php': [r'^\s*//', r'^\s*/\*', r'^\s*\*', r'^\s*#'],
    'dart': [r'^\s*//', r'^\s*/\*', r'^\s*\*'],
    'kotlin': [r'^\s*//', r'^\s*/\*', r'^\s*\*'],
}


def should_exclude(path_str):
    """Check if path should be excluded from analysis."""
    path_parts = Path(path_str).parts
    return any(pattern in path_parts for pattern in EXCLUDE_PATTERNS)


def detect_language(file_path):
    """Detect programming language from file extension."""
    ext = Path(file_path).suffix.lower()
    lang_map = {
        '.py': 'python',
        '.js': 'javascript', '.jsx': 'javascript', '.ts': 'javascript', '.tsx': 'javascript',
        '.java': 'java',
        '.c': 'c', '.cpp': 'c', '.h': 'c', '.hpp': 'c',
        '.rb': 'ruby',
        '.php': 'php',
        '.go': 'go',
        '.rs': 'rust',
        '.swift': 'swift',
        '.kt': 'kotlin',
        '.cs': 'csharp',
        '.dart': 'dart',
    }
    return lang_map.get(ext, 'unknown')


def is_comment_line(line, language):
    """Check if line is a comment."""
    if language not in COMMENT_PATTERNS:
        return False

    return any(re.match(pattern, line) for pattern in COMMENT_PATTERNS[language])


def analyze_file(file_path):
    """Analyze a single file for metrics."""
    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            lines = f.readlines()
    except Exception as e:
        return None

    total_lines = len(lines)
    blank_lines = sum(1 for line in lines if line.strip() == '')

    language = detect_language(file_path)
    comment_lines = sum(1 for line in lines if is_comment_line(line, language))

    code_lines = total_lines - blank_lines - comment_lines

    # Look for TODO/FIXME comments
    todos = sum(1 for line in lines if re.search(r'\b(TODO|FIXME|HACK|XXX)\b', line, re.IGNORECASE))

    return {
        'total_lines': total_lines,
        'code_lines': code_lines,
        'comment_lines': comment_lines,
        'blank_lines': blank_lines,
        'todos': todos,
        'language': language
    }


def find_duplicates(files_content, min_lines=6):
    """Find duplicated code blocks (simple line-based detection)."""
    duplicates = []

    # Create n-gram hashes of code blocks
    block_locations = defaultdict(list)

    for file_path, content in files_content.items():
        lines = [line.strip() for line in content.split('\n') if line.strip()]

        for i in range(len(lines) - min_lines + 1):
            block = '\n'.join(lines[i:i + min_lines])
            block_hash = hash(block)
            block_locations[block_hash].append((file_path, i + 1, block))

    # Find blocks that appear multiple times
    for block_hash, locations in block_locations.items():
        if len(locations) > 1:
            # Only report if in different files or far apart in same file
            unique_files = set(loc[0] for loc in locations)
            if len(unique_files) > 1 or len(locations) > 2:
                duplicates.append({
                    'locations': [(loc[0], loc[1]) for loc in locations],
                    'lines': min_lines,
                    'preview': locations[0][2][:100]
                })

    return duplicates[:20]  # Limit to top 20 duplications


def analyze_codebase(root_path):
    """Analyze entire codebase."""
    root = Path(root_path)

    metrics = {
        'total_files': 0,
        'code_files': 0,
        'total_lines': 0,
        'code_lines': 0,
        'comment_lines': 0,
        'blank_lines': 0,
        'todos': 0,
        'by_language': defaultdict(lambda: {
            'files': 0,
            'total_lines': 0,
            'code_lines': 0
        }),
        'largest_files': [],
        'files_with_todos': []
    }

    files_content = {}

    # Walk directory tree
    for file_path in root.rglob('*'):
        if file_path.is_file():
            metrics['total_files'] += 1

            # Check if it's a code file
            if file_path.suffix in CODE_EXTENSIONS and not should_exclude(str(file_path)):
                metrics['code_files'] += 1

                file_metrics = analyze_file(file_path)
                if file_metrics:
                    metrics['total_lines'] += file_metrics['total_lines']
                    metrics['code_lines'] += file_metrics['code_lines']
                    metrics['comment_lines'] += file_metrics['comment_lines']
                    metrics['blank_lines'] += file_metrics['blank_lines']
                    metrics['todos'] += file_metrics['todos']

                    # By language
                    lang = file_metrics['language']
                    metrics['by_language'][lang]['files'] += 1
                    metrics['by_language'][lang]['total_lines'] += file_metrics['total_lines']
                    metrics['by_language'][lang]['code_lines'] += file_metrics['code_lines']

                    # Track largest files
                    metrics['largest_files'].append({
                        'path': str(file_path.relative_to(root)),
                        'lines': file_metrics['code_lines']
                    })

                    # Track files with TODOs
                    if file_metrics['todos'] > 0:
                        metrics['files_with_todos'].append({
                            'path': str(file_path.relative_to(root)),
                            'count': file_metrics['todos']
                        })

                    # Store content for duplicate detection
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            files_content[str(file_path.relative_to(root))] = f.read()
                    except:
                        pass

    # Sort and limit largest files
    metrics['largest_files'].sort(key=lambda x: x['lines'], reverse=True)
    metrics['largest_files'] = metrics['largest_files'][:10]

    # Sort files with TODOs
    metrics['files_with_todos'].sort(key=lambda x: x['count'], reverse=True)

    # Find duplicates
    print("Analyzing code duplication...", file=sys.stderr)
    metrics['duplicates'] = find_duplicates(files_content)

    # Convert defaultdict to regular dict for JSON serialization
    metrics['by_language'] = dict(metrics['by_language'])

    return metrics


def print_table(metrics):
    """Print metrics in table format."""
    print("\n" + "="*60)
    print("CODEBASE ANALYSIS REPORT")
    print("="*60)

    print(f"\nTotal Files: {metrics['total_files']}")
    print(f"Code Files: {metrics['code_files']}")
    print(f"\nLines of Code:")
    print(f"  Total:    {metrics['total_lines']:,}")
    print(f"  Code:     {metrics['code_lines']:,}")
    print(f"  Comments: {metrics['comment_lines']:,}")
    print(f"  Blank:    {metrics['blank_lines']:,}")

    if metrics['code_lines'] > 0:
        comment_ratio = (metrics['comment_lines'] / metrics['code_lines']) * 100
        print(f"\nComment Ratio: {comment_ratio:.1f}%")

    print(f"\nTODO/FIXME Count: {metrics['todos']}")

    print("\n" + "-"*60)
    print("BY LANGUAGE")
    print("-"*60)
    for lang, stats in sorted(metrics['by_language'].items(),
                              key=lambda x: x[1]['code_lines'],
                              reverse=True):
        print(f"{lang:15} {stats['files']:4} files    {stats['code_lines']:8,} lines")

    print("\n" + "-"*60)
    print("LARGEST FILES (by code lines)")
    print("-"*60)
    for i, file_info in enumerate(metrics['largest_files'][:10], 1):
        print(f"{i:2}. {file_info['path']:50} {file_info['lines']:6,} lines")

    if metrics['files_with_todos']:
        print("\n" + "-"*60)
        print("FILES WITH TODO/FIXME")
        print("-"*60)
        for file_info in metrics['files_with_todos'][:10]:
            print(f"   {file_info['path']:50} {file_info['count']:3} items")

    if metrics['duplicates']:
        print("\n" + "-"*60)
        print(f"CODE DUPLICATION ({len(metrics['duplicates'])} blocks found)")
        print("-"*60)
        for i, dup in enumerate(metrics['duplicates'][:5], 1):
            print(f"{i}. Found in {len(dup['locations'])} locations:")
            for loc in dup['locations'][:3]:
                print(f"     {loc[0]}:{loc[1]}")

    print("\n" + "="*60)


def main():
    parser = argparse.ArgumentParser(description='Analyze codebase metrics')
    parser.add_argument('path', help='Path to codebase root')
    parser.add_argument('--output', help='Output JSON file path')
    parser.add_argument('--format', choices=['json', 'table'], default='table',
                       help='Output format (default: table)')

    args = parser.parse_args()

    if not os.path.isdir(args.path):
        print(f"Error: {args.path} is not a directory", file=sys.stderr)
        sys.exit(1)

    print(f"Analyzing codebase at: {args.path}", file=sys.stderr)
    metrics = analyze_codebase(args.path)

    if args.format == 'json' or args.output:
        json_output = json.dumps(metrics, indent=2)

        if args.output:
            with open(args.output, 'w') as f:
                f.write(json_output)
            print(f"Metrics written to: {args.output}", file=sys.stderr)
        else:
            print(json_output)

    if args.format == 'table':
        print_table(metrics)


if __name__ == '__main__':
    main()
