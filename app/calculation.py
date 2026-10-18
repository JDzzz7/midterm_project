import datetime
from app.exceptions import OperationError
from app.operations import OperationFactory

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
        """Perform the selected arithmetic operation using the Operation Factory Pattern."""

        try:
            operation = OperationFactory.create_operation(self.operation)
            return operation.execute(self.operand1, self.operand2)

        except (ValueError, ZeroDivisionError, OverflowError) as error:
            raise OperationError(f"Calculation failed: {error}") from error

    def __str__(self):
        """Display the calculation in a user friendly and easy to read format."""
        return f"{self.operation}({self.operand1}, {self.operand2}) = {self.result}"

    def to_dict(self):
        """Convert a calculation into a dictionary."""
        return {
            "operation": self.operation,
            "operand1": str(self.operand1),
            "operand2": str(self.operand2),
            "result": str(self.result),
            "timestamp": self.timestamp.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        """Create a Calculation object from a dictionary."""
        try:
            operation = data["operation"]
            operand1 = float(data["operand1"])
            operand2 = float(data["operand2"])
            timestamp = datetime.datetime.fromisoformat(data["timestamp"])

            calculation = cls(operation, operand1, operand2)
            calculation.timestamp = timestamp

            return calculation

        except (KeyError, ValueError, TypeError, OverflowError) as error:
            raise OperationError(f"Invalid calculation data: {error}") from error

    def format_result(self, precision=2):
        """Format the calculation result to the specified decimal places."""
        return f"{self.result:.{precision}f}"

    def __eq__(self, other):
        """Compare two calculations based on their values."""
        if not isinstance(other, Calculation):
            return NotImplemented

        return (
            self.operation == other.operation
            and self.operand1 == other.operand1
            and self.operand2 == other.operand2
            and self.result == other.result
        )
    def __repr__(self):
        """Return a detailed string representation of the calculation."""
        return (
            f"Calculation(operation='{self.operation}', "
            f"operand1={self.operand1}, "
            f"operand2={self.operand2}, "
            f"result={self.result})"
        )
