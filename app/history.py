from abc import ABC, abstractmethod

class HistoryObserver(ABC):
    """Base class for History Observers that react to calculations."""

    @abstractmethod
    def update(self, calculation):
        """Update when a new calculation is performed."""
        pass
