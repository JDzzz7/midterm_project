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

    
    def undo(self):
        """Restore the history before the last calculation."""

        if not self.undo_stack:
            return False

        current_state = CalculatorMemento(self.history)
        self.redo_stack.append(current_state)

        previous_state = self.undo_stack.pop()
        self.history = previous_state.get_history()

        return True
    
    def redo(self):
        """Restore the most recently undone calculation."""

        if not self.redo_stack:
            return False

        current_state = CalculatorMemento(self.history)
        self.undo_stack.append(current_state)

        next_state = self.redo_stack.pop()
        self.history = next_state.get_history()

        return True

