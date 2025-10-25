#!/usr/bin/env python3
"""
Main orchestrator script for security scanning.

This script coordinates SAST tool execution, result parsing, deduplication,
and report generation.
"""

import argparse
import subprocess
import sys
from datetime import datetime
from pathlib import Path
from typing import List

# Add current directory to path to import modules
sys.path.insert(0, str(Path(__file__).parent))

from parsers.semgrep_parser import SemgrepParser
from parsers.bandit_parser import BanditParser
from parsers.npm_audit_parser import NpmAuditParser
from parsers.trivy_parser import TrivyParser
from generators.vulnerability_report import VulnerabilityReportGenerator
from generators.summary_generator import SummaryGenerator
from utils.deduplicator import FindingDeduplicator, Finding
from utils.language_detector import LanguageDetector


class SecurityScanner:
    """Main security scanner orchestrator."""

    def __init__(self, target_path: str, output_dir: str = None, project_name: str = ""):
        """
        Initialize scanner.

        Args:
            target_path: Path to scan
            output_dir: Output directory for reports (optional)
            project_name: Name of the project (optional)
        """
        self.target_path = Path(target_path).resolve()
        self.project_name = project_name or self.target_path.name

        # Set output directory
        if output_dir:
            self.output_dir = Path(output_dir)
        else:
            timestamp = datetime.now().strftime("%Y-%m-%d")
            self.output_dir = Path(f"security-issues-{timestamp}")

        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Initialize components
        self.language_detector = LanguageDetector(str(self.target_path))
        self.deduplicator = FindingDeduplicator()
        self.tools_used = []

        # Temporary directory for tool outputs
        self.temp_dir = self.output_dir / ".temp"
        self.temp_dir.mkdir(exist_ok=True)

    def detect_environment(self) -> dict:
        """Detect project languages and frameworks."""
        print("🔍 Detecting project environment...")
        summary = self.language_detector.get_summary()
        print(f"   Primary language: {summary['primary_language']}")
        print(f"   Languages found: {', '.join(summary['languages'].keys())}")
        if summary['frameworks']:
            print(f"   Frameworks: {', '.join(summary['frameworks'])}")
        return summary

    def run_tool(self, parser, tool_name: str) -> List[Finding]:
        """
        Run a SAST tool and parse its output.

        Args:
            parser: Parser instance for the tool
            tool_name: Name of the tool

        Returns:
            List of findings from the tool
        """
        if not parser.is_available():
            print(f"   ⚠️  {tool_name} not available, skipping...")
            return []

        print(f"   Running {tool_name}...")
        output_file = self.temp_dir / f"{tool_name}_output.json"

        try:
            command = parser.get_command(str(self.target_path), str(output_file))

            # Special handling for npm audit (needs to redirect output)
            if tool_name == "npm_audit":
                result = subprocess.run(
                    command,
                    cwd=str(self.target_path),
                    capture_output=True,
                    text=True,
                )
                # Write output to file
                with open(output_file, "w") as f:
                    f.write(result.stdout)
            else:
                subprocess.run(
                    command,
                    cwd=str(self.target_path),
                    check=False,  # Don't fail if tool finds issues
                    capture_output=True,
                )

            # Check if output file was created
            if not output_file.exists():
                print(f"   ⚠️  {tool_name} did not produce output")
                return []

            findings = parser.parse(output_file)
            print(f"   ✓ {tool_name}: found {len(findings)} potential issues")
            self.tools_used.append(tool_name)
            return findings

        except Exception as e:
            print(f"   ⚠️  Error running {tool_name}: {e}")
            return []

    def scan(self) -> List[Finding]:
        """
        Run all applicable SAST tools and collect findings.

        Returns:
            List of all deduplicated findings
        """
        print("\n🔎 Running security scans...")

        # Detect environment to determine which tools to use
        env = self.detect_environment()

        # Always run Semgrep (multi-language)
        semgrep_findings = self.run_tool(SemgrepParser(), "semgrep")
        self.deduplicator.add_findings(semgrep_findings)

        # Run language-specific tools
        if "python" in env["languages"]:
            bandit_findings = self.run_tool(BanditParser(), "bandit")
            self.deduplicator.add_findings(bandit_findings)

        # Run npm audit if package.json exists
        if (self.target_path / "package.json").exists():
            npm_findings = self.run_tool(NpmAuditParser(), "npm_audit")
            self.deduplicator.add_findings(npm_findings)

        # Run Trivy for dependency scanning
        trivy_findings = self.run_tool(TrivyParser(), "trivy")
        self.deduplicator.add_findings(trivy_findings)

        # Get deduplicated findings
        unique_findings = self.deduplicator.get_unique_findings()
        print(f"\n✓ Total unique findings after deduplication: {len(unique_findings)}")

        return unique_findings

    def generate_reports(self, findings: List[Finding]) -> None:
        """
        Generate vulnerability reports and summary.

        Args:
            findings: List of security findings
        """
        print(f"\n📝 Generating reports in {self.output_dir}...")

        # Generate individual vulnerability reports
        vuln_generator = VulnerabilityReportGenerator(self.output_dir)
        report_paths = vuln_generator.generate_all_reports(findings)
        print(f"   ✓ Generated {len(report_paths)} vulnerability reports")

        # Generate summary
        summary_generator = SummaryGenerator(self.output_dir)
        summary_path = summary_generator.generate_summary(
            findings=findings,
            project_name=self.project_name,
            tools_used=self.tools_used,
            scan_date=datetime.now().strftime("%Y-%m-%d"),
        )
        print(f"   ✓ Generated summary report: {summary_path.name}")

        # Print statistics
        stats = self.deduplicator.get_statistics()
        print("\n📊 Summary:")
        print(f"   Total vulnerabilities: {stats['total']}")
        print(f"   - Critical: {stats['by_severity']['CR']}")
        print(f"   - High: {stats['by_severity']['HI']}")
        print(f"   - Medium: {stats['by_severity']['ME']}")
        print(f"   - Low: {stats['by_severity']['LO']}")

    def cleanup(self) -> None:
        """Clean up temporary files."""
        import shutil
        if self.temp_dir.exists():
            shutil.rmtree(self.temp_dir)

    def run(self) -> None:
        """Execute complete security scan workflow."""
        print(f"🚀 Starting security audit for: {self.target_path}")
        print(f"   Output directory: {self.output_dir}\n")

        try:
            # Run scans
            findings = self.scan()

            # Generate reports
            if findings:
                self.generate_reports(findings)
            else:
                print("\n✅ No security issues found!")

            print(f"\n✅ Security audit complete!")
            print(f"   Reports saved to: {self.output_dir.resolve()}")

        except KeyboardInterrupt:
            print("\n\n❌ Scan interrupted by user")
            sys.exit(1)
        except Exception as e:
            print(f"\n❌ Error during scan: {e}")
            import traceback
            traceback.print_exc()
            sys.exit(1)
        finally:
            # Clean up
            self.cleanup()


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Run comprehensive security audit using multiple SAST tools",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Scan current directory
  %(prog)s .

  # Scan specific project with custom output
  %(prog)s /path/to/project --output ./my-security-report

  # Scan with project name
  %(prog)s . --project "My App"
        """,
    )

    parser.add_argument(
        "target",
        help="Path to the codebase to scan",
    )

    parser.add_argument(
        "-o", "--output",
        help="Output directory for reports (default: ./security-issues-YYYY-MM-DD)",
        default=None,
    )

    parser.add_argument(
        "-p", "--project",
        help="Project name for reports",
        default="",
    )

    args = parser.parse_args()

    # Validate target
    target_path = Path(args.target)
    if not target_path.exists():
        print(f"❌ Error: Target path does not exist: {args.target}")
        sys.exit(1)

    # Run scanner
    scanner = SecurityScanner(
        target_path=args.target,
        output_dir=args.output,
        project_name=args.project,
    )
    scanner.run()


if __name__ == "__main__":
    main()
