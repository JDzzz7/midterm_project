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

class Power(Operation):
    """Implementation of power operation."""
    def execute(self, a, b):
        return a ** b


class Root(Operation):
    """Implementation of root operation."""
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Root degree must not be zero")

        if a < 0:
            if not float(b).is_integer() or int(b) % 2 == 0:
                raise ValueError(
                    "Negative numbers must have an odd integer root"
                )
            return -((-a) ** (1 / b))

        return a ** (1 / b)


class Modulus(Operation):
    """Implementation of modulus operation."""
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Modulus by zero cannot be calculated")
        return a % b

