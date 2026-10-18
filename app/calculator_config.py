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


        """Set the maximum history size environment variables."""
        self.max_history_size = int(
            os.getenv("CALCULATOR_MAX_HISTORY_SIZE", "1000")
        )
        """Set the precision for calculations from environment variables."""
        self.precision = int(
            os.getenv("CALCULATOR_PRECISION", "10")
        )
        """Set the maximum input value for calculations from environment variables."""
        self.max_input_value = float(
            os.getenv("CALCULATOR_MAX_INPUT_VALUE", "1e100")
        )
        self.default_encoding = os.getenv(
            "CALCULATOR_DEFAULT_ENCODING", "utf-8"
        )

    @property
    def log_dir(self):
        """Return the directory where logs are stored."""
        return Path(
            os.getenv(
                "CALCULATOR_LOG_DIR",
                str(self.base_dir / "logs")
            )
        ).resolve()

    @property
    def log_file(self):
        """Return the path to the calculator log file."""
        return Path(
            os.getenv(
                "CALCULATOR_LOG_FILE",
                str(self.log_dir / "calculator.log")
            )
        ).resolve()





