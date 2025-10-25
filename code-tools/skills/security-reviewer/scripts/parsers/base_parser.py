"""Base parser interface for SAST tools."""

from abc import ABC, abstractmethod
from typing import List
from pathlib import Path
import sys

# Add parent directory to path to import utils
sys.path.insert(0, str(Path(__file__).parent.parent))
from utils.deduplicator import Finding


class BaseParser(ABC):
    """Abstract base class for SAST tool parsers."""

    def __init__(self, tool_name: str):
        """Initialize parser with tool name."""
        self.tool_name = tool_name

    @abstractmethod
    def parse(self, output_file: Path) -> List[Finding]:
        """
        Parse SAST tool output and return list of findings.

        Args:
            output_file: Path to the tool's output file (usually JSON)

        Returns:
            List of Finding objects
        """
        pass

    @abstractmethod
    def is_available(self) -> bool:
        """Check if the SAST tool is available on the system."""
        pass

    @abstractmethod
    def get_command(self, target_path: str, output_file: str) -> List[str]:
        """
        Get the command to run the SAST tool.

        Args:
            target_path: Path to scan
            output_file: Path where output should be saved

        Returns:
            Command as list of strings
        """
        pass
