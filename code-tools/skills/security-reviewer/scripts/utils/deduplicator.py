"""Deduplication utilities for security findings."""

from dataclasses import dataclass
from typing import List, Dict, Any
import hashlib


@dataclass
class Finding:
    """Represents a security finding from a SAST tool."""
    tool: str
    title: str
    severity: str
    category: str
    file_path: str
    line_start: int
    line_end: int
    code_snippet: str
    description: str
    cwe: str = ""
    metadata: Dict[str, Any] = None

    def __post_init__(self):
        if self.metadata is None:
            self.metadata = {}

    def get_fingerprint(self) -> str:
        """
        Generate a fingerprint for this finding based on its key characteristics.

        Findings with the same fingerprint are considered duplicates.
        """
        # Normalize file path (remove leading ./)
        normalized_path = self.file_path.lstrip("./")

        # Create fingerprint from key attributes
        fingerprint_data = (
            f"{normalized_path}:"
            f"{self.line_start}:"
            f"{self.category}:"
            f"{self.title}"
        )

        return hashlib.md5(fingerprint_data.encode()).hexdigest()

    def merge_with(self, other: "Finding") -> "Finding":
        """
        Merge this finding with another duplicate finding.

        Combines metadata and keeps the more severe rating.
        """
        # Use the higher severity
        severity_order = {"CR": 0, "HI": 1, "ME": 2, "LO": 3}
        if severity_order.get(other.severity, 4) < severity_order.get(self.severity, 4):
            merged_severity = other.severity
        else:
            merged_severity = self.severity

        # Combine tool names
        tools = {self.tool, other.tool}
        merged_tool = ", ".join(sorted(tools))

        # Merge metadata
        merged_metadata = {**self.metadata, **other.metadata}
        if "tools" in merged_metadata:
            merged_metadata["tools"] = list(set(merged_metadata["tools"] + [self.tool, other.tool]))
        else:
            merged_metadata["tools"] = [self.tool, other.tool]

        # Keep the longer description
        merged_description = self.description if len(self.description) > len(other.description) else other.description

        return Finding(
            tool=merged_tool,
            title=self.title,
            severity=merged_severity,
            category=self.category,
            file_path=self.file_path,
            line_start=min(self.line_start, other.line_start),
            line_end=max(self.line_end, other.line_end),
            code_snippet=self.code_snippet if len(self.code_snippet) > len(other.code_snippet) else other.code_snippet,
            description=merged_description,
            cwe=self.cwe or other.cwe,
            metadata=merged_metadata,
        )


class FindingDeduplicator:
    """Deduplicate security findings from multiple SAST tools."""

    def __init__(self):
        self.fingerprint_map: Dict[str, Finding] = {}

    def add_finding(self, finding: Finding) -> bool:
        """
        Add a finding to the deduplicator.

        Args:
            finding: The finding to add

        Returns:
            True if this is a new finding, False if it's a duplicate
        """
        fingerprint = finding.get_fingerprint()

        if fingerprint in self.fingerprint_map:
            # Merge with existing finding
            self.fingerprint_map[fingerprint] = self.fingerprint_map[fingerprint].merge_with(finding)
            return False
        else:
            # New finding
            self.fingerprint_map[fingerprint] = finding
            return True

    def add_findings(self, findings: List[Finding]) -> None:
        """Add multiple findings to the deduplicator."""
        for finding in findings:
            self.add_finding(finding)

    def get_unique_findings(self) -> List[Finding]:
        """Get all unique findings after deduplication."""
        return list(self.fingerprint_map.values())

    def get_statistics(self) -> Dict[str, int]:
        """Get statistics about deduplicated findings."""
        findings = self.get_unique_findings()

        severity_counts = {"CR": 0, "HI": 0, "ME": 0, "LO": 0}
        category_counts: Dict[str, int] = {}

        for finding in findings:
            severity_counts[finding.severity] = severity_counts.get(finding.severity, 0) + 1
            category_counts[finding.category] = category_counts.get(finding.category, 0) + 1

        return {
            "total": len(findings),
            "by_severity": severity_counts,
            "by_category": category_counts,
        }
