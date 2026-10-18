from abc import ABC, abstractmethod
from app.logger import Logger

"""Class for managing the history of calculations."""
class HistoryObserver(ABC):
    """Base class for History Observers that react to calculations."""

    @abstractmethod
    def update(self, calculation):
        """Update when a new calculation is performed."""
        pass

class LoggingObserver(HistoryObserver):
    """Logging Observer that logs completed calculations."""

    def __init__(self):
        self.logger = Logger()

    def update(self, calculation):
        """Log a calculation if it's not None."""

        if calculation is None:
            raise AttributeError("Calculation must not be None")

        self.logger.log_calculation(calculation)

class AutoSaveObserver(HistoryObserver):
    """An Auto Save Observer that saves calculation history when enabled."""

    def __init__(self, calculator):
        self.calculator = calculator

    def update(self, calculation):
        """Save history when a new calculation is done."""

        if calculation is None:
            raise AttributeError("Calculation cannot be None")

        if self.calculator.config.auto_save:
            self.calculator.save_history()
