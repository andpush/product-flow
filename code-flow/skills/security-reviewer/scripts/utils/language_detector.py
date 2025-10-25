"""Language and framework detection for codebases."""

import json
import os
from pathlib import Path
from typing import Dict, List, Set


class LanguageDetector:
    """Detect programming languages and frameworks in a codebase."""

    # Extension to language mapping
    EXTENSIONS = {
        ".py": "python",
        ".js": "javascript",
        ".jsx": "javascript",
        ".ts": "typescript",
        ".tsx": "typescript",
        ".java": "java",
        ".go": "go",
        ".rb": "ruby",
        ".php": "php",
        ".c": "c",
        ".cpp": "cpp",
        ".cs": "csharp",
        ".rs": "rust",
        ".swift": "swift",
        ".kt": "kotlin",
        ".scala": "scala",
        ".sh": "bash",
        ".yaml": "yaml",
        ".yml": "yaml",
        ".json": "json",
        ".sql": "sql",
        ".html": "html",
        ".css": "css",
        ".vue": "vue",
    }

    # Framework detection markers
    FRAMEWORK_MARKERS = {
        "django": ["manage.py", "django", "INSTALLED_APPS"],
        "flask": ["flask", "Flask"],
        "fastapi": ["fastapi", "FastAPI"],
        "react": ["react", "React"],
        "vue": ["vue", "Vue"],
        "angular": ["angular", "@angular"],
        "express": ["express", "Express"],
        "spring": ["springframework", "@SpringBootApplication"],
        "rails": ["Gemfile", "rails", "Rails"],
    }

    def __init__(self, root_path: str):
        """Initialize detector with project root path."""
        self.root_path = Path(root_path)

    def detect_languages(self, max_depth: int = 3) -> Dict[str, int]:
        """
        Detect languages in the codebase by scanning file extensions.

        Args:
            max_depth: Maximum directory depth to scan

        Returns:
            Dictionary mapping language names to file counts
        """
        language_counts: Dict[str, int] = {}

        for root, dirs, files in os.walk(self.root_path):
            # Calculate depth
            depth = len(Path(root).relative_to(self.root_path).parts)
            if depth > max_depth:
                continue

            # Skip common non-source directories
            dirs[:] = [d for d in dirs if d not in {
                'node_modules', 'venv', '.venv', 'env', '.env',
                '__pycache__', '.git', '.github', 'dist', 'build',
                'target', 'vendor', '.idea', '.vscode'
            }]

            for file in files:
                ext = Path(file).suffix.lower()
                if ext in self.EXTENSIONS:
                    lang = self.EXTENSIONS[ext]
                    language_counts[lang] = language_counts.get(lang, 0) + 1

        return language_counts

    def detect_frameworks(self) -> Set[str]:
        """
        Detect frameworks by looking for marker files and import patterns.

        Returns:
            Set of detected framework names
        """
        detected = set()

        # Check for package files
        package_files = {
            "package.json": self._check_package_json,
            "requirements.txt": self._check_requirements_txt,
            "Pipfile": self._check_pipfile,
            "Gemfile": self._check_gemfile,
            "pom.xml": self._check_pom_xml,
        }

        for filename, checker in package_files.items():
            file_path = self.root_path / filename
            if file_path.exists():
                detected.update(checker(file_path))

        return detected

    def _check_package_json(self, file_path: Path) -> Set[str]:
        """Check package.json for JavaScript frameworks."""
        try:
            with open(file_path) as f:
                data = json.load(f)
            dependencies = {**data.get("dependencies", {}), **data.get("devDependencies", {})}

            frameworks = set()
            if "react" in dependencies:
                frameworks.add("react")
            if "vue" in dependencies:
                frameworks.add("vue")
            if "express" in dependencies:
                frameworks.add("express")
            if "@angular/core" in dependencies:
                frameworks.add("angular")

            return frameworks
        except (json.JSONDecodeError, IOError):
            return set()

    def _check_requirements_txt(self, file_path: Path) -> Set[str]:
        """Check requirements.txt for Python frameworks."""
        try:
            with open(file_path) as f:
                content = f.read().lower()

            frameworks = set()
            if "django" in content:
                frameworks.add("django")
            if "flask" in content:
                frameworks.add("flask")
            if "fastapi" in content:
                frameworks.add("fastapi")

            return frameworks
        except IOError:
            return set()

    def _check_pipfile(self, file_path: Path) -> Set[str]:
        """Check Pipfile for Python frameworks."""
        try:
            with open(file_path) as f:
                content = f.read().lower()

            frameworks = set()
            if "django" in content:
                frameworks.add("django")
            if "flask" in content:
                frameworks.add("flask")
            if "fastapi" in content:
                frameworks.add("fastapi")

            return frameworks
        except IOError:
            return set()

    def _check_gemfile(self, file_path: Path) -> Set[str]:
        """Check Gemfile for Ruby frameworks."""
        try:
            with open(file_path) as f:
                content = f.read().lower()

            if "rails" in content:
                return {"rails"}
            return set()
        except IOError:
            return set()

    def _check_pom_xml(self, file_path: Path) -> Set[str]:
        """Check pom.xml for Java frameworks."""
        try:
            with open(file_path) as f:
                content = f.read().lower()

            if "spring" in content:
                return {"spring"}
            return set()
        except IOError:
            return set()

    def get_primary_language(self) -> str:
        """Get the primary language based on file count."""
        languages = self.detect_languages()
        if not languages:
            return "unknown"
        return max(languages.items(), key=lambda x: x[1])[0]

    def get_summary(self) -> Dict:
        """Get a complete summary of detected languages and frameworks."""
        return {
            "languages": self.detect_languages(),
            "primary_language": self.get_primary_language(),
            "frameworks": list(self.detect_frameworks()),
        }
