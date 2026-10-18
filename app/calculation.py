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
