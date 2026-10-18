from abc import ABC, abstractmethod


class Operation(ABC):
    """Starting point for all calculator operations."""

    @abstractmethod
    def execute(self, a, b):
        """Perform a calculation using two the provided operands."""
        pass