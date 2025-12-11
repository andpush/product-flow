#!/usr/bin/env python3
"""
Dependency Graph Generator

Analyzes and visualizes dependencies in a codebase:
- Internal module dependencies (import/require statements)
- External package dependencies
- Outputs in Mermaid or DOT format

Usage:
    python generate_dependency_graph.py /path/to/codebase --format mermaid
    python generate_dependency_graph.py /path/to/codebase --format dot --output graph.dot
    python generate_dependency_graph.py /path/to/codebase --type internal
"""

import os
import sys
import re
import json
import argparse
from pathlib import Path
from collections import defaultdict


EXCLUDE_PATTERNS = [
    'node_modules', 'vendor', 'venv', 'env',
    'dist', 'build', '__pycache__', '.git'
]


def should_exclude(path_str):
    """Check if path should be excluded."""
    path_parts = Path(path_str).parts
    return any(pattern in path_parts for pattern in EXCLUDE_PATTERNS)


def extract_python_imports(file_path, project_root):
    """Extract Python import statements."""
    imports = set()

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except:
        return imports

    # Match import statements
    import_patterns = [
        r'^\s*import\s+([\w\.]+)',
        r'^\s*from\s+([\w\.]+)\s+import',
    ]

    for line in content.split('\n'):
        for pattern in import_patterns:
            match = re.match(pattern, line)
            if match:
                module = match.group(1).split('.')[0]
                imports.add(module)

    return imports


def extract_javascript_imports(file_path, project_root):
    """Extract JavaScript/TypeScript import statements."""
    imports = set()

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except:
        return imports

    # Match import/require statements
    patterns = [
        r'import\s+.*?from\s+[\'"]([^\'"]+)[\'"]',
        r'require\s*\(\s*[\'"]([^\'"]+)[\'"]\s*\)',
        r'import\s*\(\s*[\'"]([^\'"]+)[\'"]\s*\)',
    ]

    for pattern in patterns:
        matches = re.finditer(pattern, content)
        for match in matches:
            module = match.group(1)
            # Extract package name (before first /)
            if module.startswith('.'):
                # Relative import - skip for external deps
                continue
            package = module.split('/')[0]
            if package.startswith('@'):
                # Scoped package
                parts = module.split('/')
                if len(parts) >= 2:
                    package = f"{parts[0]}/{parts[1]}"
            imports.add(package)

    return imports


def extract_dart_imports(file_path, project_root):
    """Extract Dart import statements."""
    imports = set()

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except:
        return imports

    # Match import statements
    patterns = [
        r"import\s+['\"]package:([^/'\"]+)",  # package imports
        r"import\s+['\"]([^'\"]+\.dart)['\"]",  # relative imports
    ]

    for pattern in patterns:
        matches = re.finditer(pattern, content)
        for match in matches:
            package = match.group(1)
            # For package imports, extract just the package name
            if '/' not in package:
                imports.add(package)
            else:
                # Skip relative imports for external deps
                if not package.startswith('.'):
                    imports.add(package.split('/')[0])

    return imports


def extract_kotlin_imports(file_path, project_root):
    """Extract Kotlin import statements."""
    imports = set()

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
    except:
        return imports

    # Match import statements
    patterns = [
        r'^\s*import\s+([\w\.]+)',
    ]

    for line in content.split('\n'):
        for pattern in patterns:
            match = re.match(pattern, line)
            if match:
                module = match.group(1).split('.')[0]
                imports.add(module)

    return imports


def extract_imports(file_path, project_root):
    """Extract imports based on file type."""
    ext = Path(file_path).suffix.lower()

    if ext == '.py':
        return extract_python_imports(file_path, project_root)
    elif ext in ['.js', '.jsx', '.ts', '.tsx', '.mjs']:
        return extract_javascript_imports(file_path, project_root)
    elif ext == '.dart':
        return extract_dart_imports(file_path, project_root)
    elif ext == '.kt':
        return extract_kotlin_imports(file_path, project_root)

    return set()


def analyze_internal_dependencies(root_path):
    """Analyze internal module dependencies."""
    root = Path(root_path)
    dependencies = defaultdict(set)
    all_modules = set()

    # Find all Python, JS, Dart, and Kotlin files
    code_files = []
    for ext in ['.py', '.js', '.ts', '.jsx', '.tsx', '.dart', '.kt']:
        code_files.extend(root.rglob(f'*{ext}'))

    # Build module map
    module_map = {}
    for file_path in code_files:
        if should_exclude(str(file_path)):
            continue

        rel_path = file_path.relative_to(root)
        # Convert path to module name
        module_name = str(rel_path.with_suffix('')).replace(os.sep, '.')

        module_map[file_path] = module_name
        all_modules.add(module_name)

    # Extract dependencies
    for file_path, module_name in module_map.items():
        imports = extract_imports(file_path, root)

        for imp in imports:
            # Check if it's an internal module
            for other_module in all_modules:
                if other_module.startswith(imp) or imp in other_module:
                    if other_module != module_name:
                        dependencies[module_name].add(other_module)

    return dict(dependencies), all_modules


def analyze_external_dependencies(root_path):
    """Analyze external package dependencies."""
    root = Path(root_path)
    dependencies = {}

    # Check for package.json (Node.js)
    package_json = root / 'package.json'
    if package_json.exists():
        try:
            with open(package_json) as f:
                data = json.load(f)
                deps = {}
                if 'dependencies' in data:
                    deps.update(data['dependencies'])
                if 'devDependencies' in data:
                    deps.update(data['devDependencies'])
                dependencies['npm'] = deps
        except:
            pass

    # Check for requirements.txt (Python)
    requirements = root / 'requirements.txt'
    if requirements.exists():
        try:
            with open(requirements) as f:
                deps = {}
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        # Extract package name and version
                        match = re.match(r'([a-zA-Z0-9_-]+)\s*([>=<~!].+)?', line)
                        if match:
                            pkg, ver = match.groups()
                            deps[pkg] = ver or '*'
                dependencies['pip'] = deps
        except:
            pass

    # Check for composer.json (PHP)
    composer_json = root / 'composer.json'
    if composer_json.exists():
        try:
            with open(composer_json) as f:
                data = json.load(f)
                deps = {}
                if 'require' in data:
                    deps.update(data['require'])
                if 'require-dev' in data:
                    deps.update(data['require-dev'])
                dependencies['composer'] = deps
        except:
            pass

    # Check for Gemfile (Ruby)
    gemfile = root / 'Gemfile'
    if gemfile.exists():
        try:
            with open(gemfile) as f:
                deps = {}
                for line in f:
                    match = re.match(r"gem\s+['\"]([^'\"]+)['\"](?:,\s*['\"]([^'\"]+)['\"])?", line)
                    if match:
                        pkg, ver = match.groups()
                        deps[pkg] = ver or '*'
                dependencies['bundler'] = deps
        except:
            pass

    # Check for go.mod (Go)
    go_mod = root / 'go.mod'
    if go_mod.exists():
        try:
            with open(go_mod) as f:
                deps = {}
                in_require = False
                for line in f:
                    if line.strip().startswith('require'):
                        in_require = True
                        continue
                    if in_require:
                        if line.strip() == ')':
                            break
                        match = re.match(r'\s*([^\s]+)\s+v?([^\s]+)', line)
                        if match:
                            pkg, ver = match.groups()
                            deps[pkg] = ver
                dependencies['go'] = deps
        except:
            pass

    # Check for pubspec.yaml (Flutter/Dart)
    pubspec_yaml = root / 'pubspec.yaml'
    if pubspec_yaml.exists():
        try:
            with open(pubspec_yaml) as f:
                deps = {}
                in_dependencies = False
                in_dev_dependencies = False
                for line in f:
                    # Simple YAML parsing for dependencies section
                    if line.strip() == 'dependencies:':
                        in_dependencies = True
                        in_dev_dependencies = False
                        continue
                    elif line.strip() == 'dev_dependencies:':
                        in_dev_dependencies = True
                        in_dependencies = False
                        continue
                    elif line.strip().endswith(':') and not line.startswith(' '):
                        in_dependencies = False
                        in_dev_dependencies = False
                        continue

                    if in_dependencies or in_dev_dependencies:
                        # Match package: version or package: ^version
                        match = re.match(r'\s+([a-zA-Z0-9_]+):\s*(.+)?', line)
                        if match:
                            pkg = match.group(1)
                            ver = match.group(2) if match.group(2) else '*'
                            # Skip sdk references
                            if ver.strip() not in ['sdk: flutter', 'sdk: dart']:
                                deps[pkg] = ver.strip()
                dependencies['pub'] = deps
        except:
            pass

    # Check for build.gradle.kts (Kotlin/Gradle)
    build_gradle_kts = root / 'build.gradle.kts'
    build_gradle = root / 'build.gradle'
    gradle_file = build_gradle_kts if build_gradle_kts.exists() else (build_gradle if build_gradle.exists() else None)

    if gradle_file:
        try:
            with open(gradle_file) as f:
                deps = {}
                content = f.read()
                # Simple pattern matching for dependencies
                # Match implementation("group:artifact:version") or implementation "group:artifact:version"
                patterns = [
                    r'implementation\s*\(\s*["\']([^:]+):([^:]+):([^"\']+)["\']\s*\)',
                    r'implementation\s+["\']([^:]+):([^:]+):([^"\']+)["\']',
                    r'api\s*\(\s*["\']([^:]+):([^:]+):([^"\']+)["\']\s*\)',
                    r'api\s+["\']([^:]+):([^:]+):([^"\']+)["\']',
                ]

                for pattern in patterns:
                    matches = re.finditer(pattern, content)
                    for match in matches:
                        group, artifact, version = match.groups()
                        pkg = f"{group}:{artifact}"
                        deps[pkg] = version

                if deps:
                    dependencies['gradle'] = deps
        except:
            pass

    return dependencies


def generate_mermaid_graph(dependencies, graph_type='internal'):
    """Generate Mermaid diagram."""
    lines = ['graph TD']

    if graph_type == 'internal':
        dep_dict, all_modules = dependencies

        # Limit to top-level modules for readability
        top_modules = set()
        for module in all_modules:
            parts = module.split('.')
            if len(parts) <= 2:  # Top-level or one level deep
                top_modules.add(module)

        for module, deps in dep_dict.items():
            if module not in top_modules:
                continue

            module_id = module.replace('.', '_').replace('-', '_')

            for dep in deps:
                if dep not in top_modules:
                    continue
                dep_id = dep.replace('.', '_').replace('-', '_')
                lines.append(f'    {module_id}["{module}"] --> {dep_id}["{dep}"]')

    else:  # external
        for manager, deps in dependencies.items():
            manager_id = manager
            for pkg, ver in sorted(deps.items())[:20]:  # Limit to 20 for readability
                pkg_id = pkg.replace('.', '_').replace('-', '_').replace('/', '_')
                label = f"{pkg}@{ver}" if ver and ver != '*' else pkg
                lines.append(f'    {manager_id}["{manager}"] --> {pkg_id}["{label}"]')

    return '\n'.join(lines)


def generate_dot_graph(dependencies, graph_type='internal'):
    """Generate DOT format graph."""
    lines = ['digraph Dependencies {']
    lines.append('    rankdir=LR;')
    lines.append('    node [shape=box];')

    if graph_type == 'internal':
        dep_dict, all_modules = dependencies

        for module, deps in dep_dict.items():
            module_id = module.replace('.', '_').replace('-', '_')

            for dep in deps:
                dep_id = dep.replace('.', '_').replace('-', '_')
                lines.append(f'    "{module}" -> "{dep}";')

    else:  # external
        for manager, deps in dependencies.items():
            for pkg, ver in deps.items():
                label = f"{pkg}@{ver}" if ver and ver != '*' else pkg
                lines.append(f'    "{manager}" -> "{label}";')

    lines.append('}')
    return '\n'.join(lines)


def main():
    parser = argparse.ArgumentParser(description='Generate dependency graph')
    parser.add_argument('path', help='Path to codebase root')
    parser.add_argument('--type', choices=['internal', 'external', 'both'],
                       default='both', help='Type of dependencies to analyze')
    parser.add_argument('--format', choices=['mermaid', 'dot'],
                       default='mermaid', help='Output format')
    parser.add_argument('--output', help='Output file path')

    args = parser.parse_args()

    if not os.path.isdir(args.path):
        print(f"Error: {args.path} is not a directory", file=sys.stderr)
        sys.exit(1)

    output_lines = []

    if args.type in ['internal', 'both']:
        print("Analyzing internal dependencies...", file=sys.stderr)
        internal_deps = analyze_internal_dependencies(args.path)

        if args.format == 'mermaid':
            output_lines.append("## Internal Dependencies")
            output_lines.append(generate_mermaid_graph(internal_deps, 'internal'))
        else:
            output_lines.append(generate_dot_graph(internal_deps, 'internal'))

    if args.type in ['external', 'both']:
        print("Analyzing external dependencies...", file=sys.stderr)
        external_deps = analyze_external_dependencies(args.path)

        if external_deps:
            if args.format == 'mermaid':
                output_lines.append("\n## External Dependencies")
                output_lines.append(generate_mermaid_graph(external_deps, 'external'))
            else:
                if args.type == 'both':
                    output_lines.append("\n")
                output_lines.append(generate_dot_graph(external_deps, 'external'))

    result = '\n'.join(output_lines)

    if args.output:
        with open(args.output, 'w') as f:
            f.write(result)
        print(f"Graph written to: {args.output}", file=sys.stderr)
    else:
        print(result)


if __name__ == '__main__':
    main()
