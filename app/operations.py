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


class IntegerDivision(Operation):
    """Implementation of integer division operation."""
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Integer division by zero cannot be calculated")
        return a // b


class Percentage(Operation):
    """Implementation of percentage operation."""
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Percentage denominator cannot be zero")
        return (a / b) * 100


class AbsoluteDifference(Operation):
    """Implementation of absolute difference operation."""
    def execute(self, a, b):
        return abs(a - b)


class OperationFactory:
    """Factory class for creating calculator operations based on their names."""

    _operation_types = {
        "add": Addition,
        "subtract": Subtraction,
        "multiply": Multiplication,
        "divide": Division,
        "power": Power,
        "root": Root,
        "modulus": Modulus,
        "int_divide": IntegerDivision,
        "percent": Percentage,
        "abs_diff": AbsoluteDifference
    }

    @classmethod
    def register_operation(cls, name, operation_class):
        """Register a new operation to the factory."""
        if not isinstance(operation_class, type) or not issubclass(
            operation_class, Operation
        ):
            raise TypeError("Invalid operation class")

        cls._operation_types[name.lower()] = operation_class

    @classmethod
    def create_operation(cls, name):
        """Return an instance of the requested operation."""
        operation = cls._operation_types.get(name.lower())

        if operation is None:
            raise ValueError(f"Operation '{name}' is not supported")

        return operation()

