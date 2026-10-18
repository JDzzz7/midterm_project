import logging

"""Class for logging calculator operations and errors."""
class Logger:
    """Manages logging for the calculator application."""

    def __init__(self, filename="calculator.log"):
        self.logger = logging.getLogger("Calculator")
        self.logger.setLevel(logging.INFO)
        self.logger.propagate = False

        if not self.logger.handlers:
            handler = logging.FileHandler(filename)
            handler.setFormatter(
                logging.Formatter(
                    "%(asctime)s - %(levelname)s - %(message)s"
                )
            )
            self.logger.addHandler(handler)

    def log_calculation(self, calculation):
        """Record a completed successful calculation."""
        self.logger.info(
            f"{calculation.operation}({calculation.operand1}, "
            f"{calculation.operand2}) = {calculation.result}"
        )

    def log_error(self, message):
        """Record an error if there is one."""
        self.logger.error(message)
