
import datetime
from app.exceptions import OperationError

"""Class for performing calculator operations and storing calculation history."""
class Calculation:
    """Shows a single calculator calculation."""

    def __init__(self, operation, operand1, operand2):
        self.operation = operation
        self.operand1 = operand1
        self.operand2 = operand2
        self.timestamp = datetime.datetime.now()
        self.result = self.calculate()

    def calculate(self):
        """Performs the following selected arithmetic operation."""

        if self.operation == "root":
            if self.operand2 == 0:
                raise OperationError("Root degree cannot be zero")

        if self.operand1 < 0 and self.operand2.is_integer() and int(self.operand2) % 2 == 0:
            raise OperationError("Cannot calculate an even root of a negative number")

        operations = {
            "add": lambda a, b: a + b,
            "subtract": lambda a, b: a - b,
            "multiply": lambda a, b: a * b,
            "divide": lambda a, b: a / b,
            "power": lambda a, b: a ** b,
            "root": lambda a, b: -((-a) ** (1 / b)) if a < 0 else a ** (1 / b),
            "modulus": lambda a, b: a % b,
            "int_divide": lambda a, b: a // b,
            "percent": lambda a, b: (a / b) * 100,
            "abs_diff": lambda a, b: abs(a - b)
        }

        if self.operation not in operations:
            raise OperationError(f"Unknown operation: {self.operation}")

        try:
            return operations[self.operation](self.operand1, self.operand2)
        except (ZeroDivisionError, ValueError, OverflowError) as error:
            raise OperationError(f"Calculation failed: {error}") from error

    def __str__(self):
        """Display the calculation in a user friendly and easy to read format."""
        return f"{self.operation}({self.operand1}, {self.operand2}) = {self.result}"
