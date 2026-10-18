from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento

class Calculator:
    """Perform calculations and manage calculation history."""

    def __init__(self):
        self.history = []
        self.undo_stack = []
        self.redo_stack = []

    def perform_operation(self, operation, a, b):
        """Calculate a result and save it in history."""
        calculation = Calculation(operation, a, b)

        snapshot = CalculatorMemento(self.history)
        self.undo_stack.append(snapshot)

        self.history.append(calculation)
        self.redo_stack.clear()

        return calculation.result

    def show_history(self):
        """Display all recorded calculations."""
        return [str(calculation) for calculation in self.history]
