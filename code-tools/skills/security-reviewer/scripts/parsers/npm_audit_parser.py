"""Parser for npm audit output."""

import json
import shutil
from pathlib import Path
from typing import List
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from parsers.base_parser import BaseParser
from utils.deduplicator import Finding
from utils.severity_mapper import normalize_severity


class NpmAuditParser(BaseParser):
    """Parser for npm audit JSON output."""

    def __init__(self):
        super().__init__("npm_audit")

    def parse(self, output_file: Path) -> List[Finding]:
        """Parse npm audit JSON output."""
        try:
            with open(output_file) as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading npm audit output: {e}")
            return []

        findings = []

        # npm audit v7+ format
        vulnerabilities = data.get("vulnerabilities", {})

        for package_name, vuln_data in vulnerabilities.items():
            severity = vuln_data.get("severity", "moderate")
            title = vuln_data.get("name", package_name)

            # Extract vulnerability details
            via = vuln_data.get("via", [])
            if isinstance(via, list) and via:
                for item in via:
                    if isinstance(item, dict):
                        description = item.get("title", "")
                        cwe = ""
                        url = item.get("url", "")

                        # Normalize severity
                        try:
                            normalized_severity = normalize_severity("npm_audit", severity)
                        except ValueError:
                            normalized_severity = "ME"

                        finding = Finding(
                            tool=self.tool_name,
                            title=f"{title} - {description}" if description else title,
                            severity=normalized_severity,
                            category="dependency-vulnerability",
                            file_path="package.json",
                            line_start=0,
                            line_end=0,
                            code_snippet=f"Package: {package_name}",
                            description=description,
                            cwe=cwe,
                            metadata={
                                "package": package_name,
                                "npm_severity": severity,
                                "url": url,
                                "range": vuln_data.get("range", ""),
                            },
                        )

                        findings.append(finding)
            else:
                # Simple vulnerability without details
                try:
                    normalized_severity = normalize_severity("npm_audit", severity)
                except ValueError:
                    normalized_severity = "ME"

                finding = Finding(
                    tool=self.tool_name,
                    title=title,
                    severity=normalized_severity,
                    category="dependency-vulnerability",
                    file_path="package.json",
                    line_start=0,
                    line_end=0,
                    code_snippet=f"Package: {package_name}",
                    description=f"Vulnerability in {package_name}",
                    cwe="",
                    metadata={
                        "package": package_name,
                        "npm_severity": severity,
                        "range": vuln_data.get("range", ""),
                    },
                )

                findings.append(finding)

        return findings

    def is_available(self) -> bool:
        """Check if npm is available."""
        return shutil.which("npm") is not None

    def get_command(self, target_path: str, output_file: str) -> List[str]:
        """Get npm audit command."""
        return [
            "npm",
            "audit",
            "--json",
            "--prefix", target_path,
        ]
