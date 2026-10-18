import logging
from app.calculator_config import CalculatorConfig

"""Class that handles logging for the calculator application."""
class Logger:
    """Handles calculator logging."""

    def __init__(self):
        config = CalculatorConfig()

        config.log_dir.mkdir(parents=True, exist_ok=True)
        config.log_file.parent.mkdir(parents=True, exist_ok=True)

        self.logger = logging.getLogger("Calculator")
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False

        if not self.logger.handlers:
            handler = logging.FileHandler(
                filename=config.log_file,
                encoding=config.default_encoding
            )

            formatter = logging.Formatter(
                "%(asctime)s - %(levelname)s - %(message)s"
            )

            handler.setFormatter(formatter)
            self.logger.addHandler(handler)

    def log_calculation(self, calculation):
        self.logger.info(str(calculation))

    def log_error(self, message):
        self.logger.error(message)