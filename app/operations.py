from abc import ABC, abstractmethod
from app.exceptions import ValidationError

class Operation(ABC):
    """Starting point for all calculator operations."""

    @abstractmethod
    def execute(self, a, b):
        """Perform a calculation using two the provided operands."""
        pass

    def validate_operands(self, a, b):
        """Validate the two operand inputs before performing the operation."""
        for value in (a, b):
            if isinstance(value, bool) or not isinstance(value, (int, float)):
                raise ValidationError("Both operands must be valid numbers (int or float).")

    def __str__(self):
        """Return the operation name."""
        return self.__class__.__name__

class Addition(Operation):
    """Implementation of addition operation."""
    def execute(self, a, b):
        self.validate_operands(a, b)
        return a + b


class Subtraction(Operation):
    """Implementation of subtraction operation."""
    def execute(self, a, b):
        self.validate_operands(a, b)
        return a - b


class Multiplication(Operation):
    """Implementation of multiplication operation."""
    def execute(self, a, b):
        self.validate_operands(a, b)
        return a * b

class Division(Operation):
    """Implementation of division operation."""

    def execute(self, a, b):
        self.validate_operands(a, b)
        if b == 0:
            raise ValidationError("Cannot divide by zero")
        return a / b


class Power(Operation):
    """Implementation of power operation."""
    def execute(self, a, b):
        self.validate_operands(a, b)
        return a ** b



class Root(Operation):
    """Implementation of root operation."""

    def execute(self, a, b):
        self.validate_operands(a, b)

        if b == 0:
            raise ValidationError("Root degree must not be zero")
        if a < 0:
            if not float(b).is_integer() or int(b) % 2 == 0:
                raise ValidationError(
                    "Negative numbers must have an odd integer root"
                )
            return -((-a) ** (1 / b))
        if a == 0 and b < 0:
            raise ValidationError("Cannot take a negative root of value zero")
        return a ** (1 / b)


class Modulus(Operation):
    """Implementation of modulus operation."""
    def execute(self, a, b):
        self.validate_operands(a, b)
        if b == 0:
            raise ValidationError("Modulus by zero cannot be calculated")
        return a % b


class IntegerDivision(Operation):
    """Implementation of integer division operation."""
    def execute(self, a, b):
        self.validate_operands(a, b)
        if b == 0:
            raise ValidationError("Integer division by zero cannot be calculated")
        return a // b


class Percentage(Operation):
    """Implementation of percentage operation."""
    def execute(self, a, b):
        self.validate_operands(a, b)
        if b == 0:
            raise ValidationError("Percentage denominator of zero cannot be calculated")
        return (a / b) * 100


class AbsoluteDifference(Operation):
    """Implementation of absolute difference operation."""
    def execute(self, a, b):
        self.validate_operands(a, b)
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

