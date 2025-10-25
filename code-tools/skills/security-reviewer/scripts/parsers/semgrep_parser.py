"""Parser for Semgrep SAST tool output."""

import json
import shutil
from pathlib import Path
from typing import List
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from parsers.base_parser import BaseParser
from utils.deduplicator import Finding
from utils.severity_mapper import normalize_severity


class SemgrepParser(BaseParser):
    """Parser for Semgrep JSON output."""

    def __init__(self):
        super().__init__("semgrep")

    def parse(self, output_file: Path) -> List[Finding]:
        """Parse Semgrep JSON output."""
        try:
            with open(output_file) as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading Semgrep output: {e}")
            return []

        findings = []

        for result in data.get("results", []):
            # Extract basic info
            check_id = result.get("check_id", "unknown")
            message = result.get("extra", {}).get("message", "")
            severity = result.get("extra", {}).get("severity", "INFO")

            # Extract file and line info
            file_path = result.get("path", "")
            start_line = result.get("start", {}).get("line", 0)
            end_line = result.get("end", {}).get("line", 0)

            # Extract code snippet
            code_lines = result.get("extra", {}).get("lines", "")

            # Extract metadata
            metadata = result.get("extra", {}).get("metadata", {})
            category = metadata.get("category", "security")
            cwe = metadata.get("cwe", "")
            if isinstance(cwe, list) and cwe:
                cwe = cwe[0]

            # Normalize severity
            try:
                normalized_severity = normalize_severity("semgrep", severity)
            except ValueError:
                normalized_severity = "ME"  # Default to medium if unknown

            finding = Finding(
                tool=self.tool_name,
                title=check_id.replace(".", " ").title(),
                severity=normalized_severity,
                category=category,
                file_path=file_path,
                line_start=start_line,
                line_end=end_line,
                code_snippet=code_lines,
                description=message,
                cwe=str(cwe) if cwe else "",
                metadata={
                    "check_id": check_id,
                    "semgrep_severity": severity,
                    **metadata,
                },
            )

            findings.append(finding)

        return findings

    def is_available(self) -> bool:
        """Check if Semgrep is available."""
        return shutil.which("semgrep") is not None

    def get_command(self, target_path: str, output_file: str) -> List[str]:
        """Get Semgrep command."""
        return [
            "semgrep",
            "scan",
            "--config=auto",  # Use Semgrep registry rules
            "--json",
            f"--output={output_file}",
            "--quiet",
            target_path,
        ]
