"""Generator for summary report with statistics."""

from pathlib import Path
from typing import List, Dict
from datetime import datetime
from collections import defaultdict
import sys

sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.deduplicator import Finding
from utils.severity_mapper import get_severity_name, get_severity_order


class SummaryGenerator:
    """Generate summary.md with statistics and overview."""

    def __init__(self, output_dir: Path):
        """
        Initialize generator.

        Args:
            output_dir: Directory where summary will be saved
        """
        self.output_dir = output_dir

    def generate_summary(
        self,
        findings: List[Finding],
        project_name: str = "",
        tools_used: List[str] = None,
        scan_date: str = None,
    ) -> Path:
        """
        Generate summary.md file.

        Args:
            findings: List of all security findings
            project_name: Name of the project (optional)
            tools_used: List of SAST tools used (optional)
            scan_date: Date of scan (optional, defaults to now)

        Returns:
            Path to the generated summary file
        """
        if scan_date is None:
            scan_date = datetime.now().strftime("%Y-%m-%d")

        if tools_used is None:
            # Extract tools from findings
            tools_used = list(set(f.tool for f in findings))

        # Generate statistics
        stats = self._calculate_statistics(findings)

        # Generate markdown content
        content = self._generate_markdown(findings, stats, project_name, tools_used, scan_date)

        # Write file
        summary_path = self.output_dir / "summary.md"
        with open(summary_path, "w") as f:
            f.write(content)

        return summary_path

    def _calculate_statistics(self, findings: List[Finding]) -> Dict:
        """Calculate statistics from findings."""
        stats = {
            "total": len(findings),
            "by_severity": {"CR": 0, "HI": 0, "ME": 0, "LO": 0},
            "by_category": defaultdict(lambda: {"CR": 0, "HI": 0, "ME": 0, "LO": 0, "total": 0}),
            "by_file": defaultdict(int),
        }

        for finding in findings:
            # Count by severity
            stats["by_severity"][finding.severity] += 1

            # Count by category
            category = finding.category
            stats["by_category"][category][finding.severity] += 1
            stats["by_category"][category]["total"] += 1

            # Count by file
            stats["by_file"][finding.file_path] += 1

        return stats

    def _generate_markdown(
        self,
        findings: List[Finding],
        stats: Dict,
        project_name: str,
        tools_used: List[str],
        scan_date: str,
    ) -> str:
        """Generate markdown content for summary."""
        project_section = f"**Project:** {project_name}  \n" if project_name else ""
        tools_section = ", ".join(sorted(tools_used))

        # Executive summary
        exec_summary = self._generate_executive_summary(stats)

        # Category breakdown table
        category_table = self._generate_category_table(stats["by_category"])

        # Critical and high findings
        critical_findings = self._generate_findings_list(findings, "CR")
        high_findings = self._generate_findings_list(findings, "HI")

        # Files with most issues
        top_files = self._generate_top_files(stats["by_file"])

        # Recommendations
        recommendations = self._generate_recommendations(stats)

        markdown = f"""# Security Audit Summary

**Date:** {scan_date}
{project_section}**Tools Used:** {tools_section}

## Executive Summary

{exec_summary}

## Statistics

- **Total Vulnerabilities:** {stats['total']}
  - Critical (CR): {stats['by_severity']['CR']}
  - High (HI): {stats['by_severity']['HI']}
  - Medium (ME): {stats['by_severity']['ME']}
  - Low (LO): {stats['by_severity']['LO']}

## Breakdown by Category

{category_table}

{critical_findings}

{high_findings}

## Files with Most Issues

{top_files}

## Recommendations

{recommendations}

---

*This report was generated using automated SAST tools and should be reviewed by security experts for accurate risk assessment.*
"""

        return markdown

    def _generate_executive_summary(self, stats: Dict) -> str:
        """Generate executive summary based on statistics."""
        total = stats["total"]
        critical = stats["by_severity"]["CR"]
        high = stats["by_severity"]["HI"]

        if total == 0:
            return "No security vulnerabilities were detected in this scan. The codebase appears to be free of common security issues detectable by automated SAST tools."

        risk_level = "HIGH"
        if critical == 0 and high == 0:
            risk_level = "LOW"
        elif critical == 0 and high <= 3:
            risk_level = "MODERATE"
        elif critical > 0:
            risk_level = "CRITICAL" if critical > 2 else "HIGH"

        summary = f"This security audit identified **{total} potential vulnerabilities** with an overall risk level of **{risk_level}**. "

        if critical > 0:
            summary += f"There are **{critical} critical findings** that require immediate attention. "

        if high > 0:
            summary += f"Additionally, **{high} high-priority findings** should be addressed in the current development cycle. "

        summary += "Review all findings to assess their applicability to your specific context."

        return summary

    def _generate_category_table(self, category_stats: Dict) -> str:
        """Generate markdown table for category breakdown."""
        if not category_stats:
            return "No vulnerabilities found."

        # Sort categories by total count
        sorted_categories = sorted(
            category_stats.items(),
            key=lambda x: x[1]["total"],
            reverse=True,
        )

        table = "| Category | CR | HI | ME | LO | Total |\n"
        table += "|----------|----|----|----|----|-------|\n"

        for category, counts in sorted_categories:
            table += f"| {category} | {counts['CR']} | {counts['HI']} | {counts['ME']} | {counts['LO']} | {counts['total']} |\n"

        return table

    def _generate_findings_list(self, findings: List[Finding], severity: str) -> str:
        """Generate markdown list of findings for a specific severity."""
        severity_name = get_severity_name(severity)
        filtered = [f for f in findings if f.severity == severity]

        if not filtered:
            return ""

        # Sort by title
        filtered.sort(key=lambda f: f.title)

        # Generate sequential numbers
        items = []
        for i, finding in enumerate(filtered, 1):
            filename = f"{severity}-{i:03d}.md"
            items.append(f"- [{filename}](./{filename}) - {finding.title}")

        title = f"## {severity_name} Findings (Immediate Action Required)" if severity == "CR" else f"## {severity_name} Priority Findings"

        return f"""{title}

{chr(10).join(items)}
"""

    def _generate_top_files(self, file_stats: Dict[str, int]) -> str:
        """Generate list of files with most issues."""
        if not file_stats:
            return "No files analyzed."

        # Sort by count
        sorted_files = sorted(file_stats.items(), key=lambda x: x[1], reverse=True)

        # Take top 10
        top_files = sorted_files[:10]

        items = []
        for file_path, count in top_files:
            items.append(f"{count}. `{file_path}` - {count} finding{'s' if count > 1 else ''}")

        return "\n".join(items)

    def _generate_recommendations(self, stats: Dict) -> str:
        """Generate prioritized recommendations."""
        recommendations = []

        if stats["by_severity"]["CR"] > 0:
            recommendations.append("1. **Address all Critical findings immediately** - These represent severe security risks that could be actively exploited.")

        if stats["by_severity"]["HI"] > 0:
            recommendations.append(f"2. **Plan remediation for High findings** - Schedule {stats['by_severity']['HI']} high-priority issue{'s' if stats['by_severity']['HI'] > 1 else ''} for resolution in the current sprint.")

        if stats["by_severity"]["ME"] > 0:
            recommendations.append("3. **Triage Medium findings** - Review and prioritize these issues for upcoming development cycles.")

        if stats["by_severity"]["LO"] > 0:
            recommendations.append("4. **Review Low findings during code review** - Address these as part of regular development practices.")

        recommendations.append("5. **Implement security testing in CI/CD** - Integrate SAST tools into your continuous integration pipeline to catch issues early.")
        recommendations.append("6. **Conduct manual security review** - Automated tools cannot detect all vulnerabilities; complement with manual code review and penetration testing.")
        recommendations.append("7. **Security training** - Ensure development team is trained on secure coding practices relevant to identified vulnerability types.")

        return "\n".join(recommendations)
