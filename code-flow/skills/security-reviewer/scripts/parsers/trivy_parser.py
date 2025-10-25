"""Parser for Trivy SAST tool output."""

import json
import shutil
from pathlib import Path
from typing import List
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from parsers.base_parser import BaseParser
from utils.deduplicator import Finding
from utils.severity_mapper import normalize_severity


class TrivyParser(BaseParser):
    """Parser for Trivy JSON output."""

    def __init__(self):
        super().__init__("trivy")

    def parse(self, output_file: Path) -> List[Finding]:
        """Parse Trivy JSON output."""
        try:
            with open(output_file) as f:
                data = json.load(f)
        except (json.JSONDecodeError, IOError) as e:
            print(f"Error reading Trivy output: {e}")
            return []

        findings = []

        # Trivy output has a "Results" array
        results = data.get("Results", [])

        for result in results:
            target = result.get("Target", "")
            vulnerabilities = result.get("Vulnerabilities", [])

            for vuln in vulnerabilities:
                vuln_id = vuln.get("VulnerabilityID", "unknown")
                pkg_name = vuln.get("PkgName", "")
                installed_version = vuln.get("InstalledVersion", "")
                fixed_version = vuln.get("FixedVersion", "")
                severity = vuln.get("Severity", "MEDIUM")
                title = vuln.get("Title", "")
                description = vuln.get("Description", "")

                # Get CWE if available
                cwe_ids = vuln.get("CweIDs", [])
                cwe = cwe_ids[0] if cwe_ids else ""

                # Normalize severity
                try:
                    normalized_severity = normalize_severity("trivy", severity)
                except ValueError:
                    normalized_severity = "ME"

                finding = Finding(
                    tool=self.tool_name,
                    title=f"{vuln_id}: {title}" if title else vuln_id,
                    severity=normalized_severity,
                    category="dependency-vulnerability",
                    file_path=target,
                    line_start=0,
                    line_end=0,
                    code_snippet=f"Package: {pkg_name}@{installed_version}",
                    description=description or title,
                    cwe=cwe,
                    metadata={
                        "vulnerability_id": vuln_id,
                        "package": pkg_name,
                        "installed_version": installed_version,
                        "fixed_version": fixed_version,
                        "trivy_severity": severity,
                        "references": vuln.get("References", []),
                    },
                )

                findings.append(finding)

        return findings

    def is_available(self) -> bool:
        """Check if Trivy is available."""
        return shutil.which("trivy") is not None

    def get_command(self, target_path: str, output_file: str) -> List[str]:
        """Get Trivy command."""
        return [
            "trivy",
            "fs",  # Filesystem scan
            "--format", "json",
            "--output", output_file,
            "--quiet",
            target_path,
        ]
