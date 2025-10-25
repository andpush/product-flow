"""Parser for Bandit SAST tool output."""

import json
import shutil
from pathlib import Path
from typing import List
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from parsers.base_parser import BaseParser
from utils.deduplicator import Finding
from utils.severity_mapper import normalize_severity


class BanditParser(BaseParser):
    """Parser for Bandit JSON output."""

    def __init__(self):
        super().__init__("bandit")

    def parse(self, output_file: Path) -> List[Finding]:
        """Parse Bandit JSON output."""
        try:
            with open(output_file) as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading Bandit output: {e}")
            return []

        findings = []

        for result in data.get("results", []):
            # Extract basic info
            test_id = result.get("test_id", "unknown")
            test_name = result.get("test_name", "")
            issue_text = result.get("issue_text", "")
            severity = result.get("issue_severity", "MEDIUM")

            # Extract file and line info
            file_path = result.get("filename", "")
            line_number = result.get("line_number", 0)

            # Extract code snippet
            code_snippet = result.get("code", "")

            # Extract CWE
            cwe = result.get("issue_cwe", {})
            cwe_id = str(cwe.get("id", "")) if cwe else ""

            # Normalize severity
            try:
                normalized_severity = normalize_severity("bandit", severity)
            except ValueError:
                normalized_severity = "ME"

            finding = Finding(
                tool=self.tool_name,
                title=test_name or test_id,
                severity=normalized_severity,
                category="security",
                file_path=file_path,
                line_start=line_number,
                line_end=line_number,
                code_snippet=code_snippet,
                description=issue_text,
                cwe=cwe_id,
                metadata={
                    "test_id": test_id,
                    "bandit_severity": severity,
                    "confidence": result.get("issue_confidence", ""),
                },
            )

            findings.append(finding)

        return findings

    def is_available(self) -> bool:
        """Check if Bandit is available."""
        return shutil.which("bandit") is not None

    def get_command(self, target_path: str, output_file: str) -> List[str]:
        """Get Bandit command."""
        return [
            "bandit",
            "-r",  # Recursive
            target_path,
            "-f", "json",  # JSON format
            "-o", output_file,  # Output file
            "--quiet",  # Suppress progress
        ]
