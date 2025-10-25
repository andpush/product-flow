"""Severity mapping utilities to normalize findings from different SAST tools."""

from typing import Dict, Literal

# Standard severity levels
SeverityLevel = Literal["CR", "HI", "ME", "LO"]

# Mapping tables for different SAST tools
SEVERITY_MAPPINGS: Dict[str, Dict[str, SeverityLevel]] = {
    "semgrep": {
        "ERROR": "CR",
        "WARNING": "HI",
        "INFO": "ME",
        "NOTE": "LO",
    },
    "bandit": {
        "HIGH": "CR",
        "MEDIUM": "HI",
        "LOW": "ME",
    },
    "npm_audit": {
        "critical": "CR",
        "high": "HI",
        "moderate": "ME",
        "low": "LO",
    },
    "trivy": {
        "CRITICAL": "CR",
        "HIGH": "HI",
        "MEDIUM": "ME",
        "LOW": "LO",
    },
}


def normalize_severity(tool: str, severity: str) -> SeverityLevel:
    """
    Normalize severity from a SAST tool to standard CR/HI/ME/LO levels.

    Args:
        tool: Name of the SAST tool (e.g., 'semgrep', 'bandit')
        severity: Severity level from the tool

    Returns:
        Normalized severity level (CR/HI/ME/LO)

    Raises:
        ValueError: If tool is not recognized or severity cannot be mapped
    """
    tool = tool.lower()

    if tool not in SEVERITY_MAPPINGS:
        raise ValueError(f"Unknown tool: {tool}. Supported tools: {list(SEVERITY_MAPPINGS.keys())}")

    mapping = SEVERITY_MAPPINGS[tool]
    severity_upper = severity.upper()

    if severity_upper not in mapping and severity.lower() not in mapping:
        # Try case-insensitive match
        for key, value in mapping.items():
            if key.upper() == severity_upper:
                return value
        raise ValueError(f"Cannot map severity '{severity}' for tool '{tool}'")

    return mapping.get(severity_upper, mapping.get(severity.lower(), "LO"))


def get_severity_order() -> list[SeverityLevel]:
    """Return severity levels in order from most to least critical."""
    return ["CR", "HI", "ME", "LO"]


def get_severity_name(severity: SeverityLevel) -> str:
    """Get full name of severity level."""
    names = {
        "CR": "Critical",
        "HI": "High",
        "ME": "Medium",
        "LO": "Low",
    }
    return names.get(severity, "Unknown")
