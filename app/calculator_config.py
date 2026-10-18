import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

"""Class for managing calculator configuration settings."""
class CalculatorConfig:
    """Manage calculator config settings."""

    def __init__(self):
        self.base_dir = Path(__file__).resolve().parent.parent

        self.auto_save = os.getenv(
            "CALCULATOR_AUTO_SAVE", "true"
        ).lower() in ("true", "1")

        self.history_dir = self.base_dir / "history"
        self.history_file = self.history_dir / "calculator_history.csv"
        self.max_history_size = int(
            os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "1000")
        )

