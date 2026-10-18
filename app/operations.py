from abc import ABC, abstractmethod


class Operation(ABC):
    """Starting point for all calculator operations."""

    @abstractmethod
    def execute(self, a, b):
        """Perform a calculation using two the provided operands."""
        pass

class Addition(Operation):
    """Implementation of addition operation."""
    def execute(self, a, b):
        return a + b


class Subtraction(Operation):
    """Implementation of subtraction operation."""
    def execute(self, a, b):
        return a - b


class Multiplication(Operation):
    """Implementation of multiplication operation."""
    def execute(self, a, b):
        return a * b

class Division(Operation):
    """Implementation of division operation."""
    def execute(self, a, b):
        if b == 0:
            raise ValueError("The divisor cannot be zero.")
        return a / b