from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento
from app.history import HistoryObserver
from app.calculator_config import CalculatorConfig
from app.exceptions import ValidationError
import pandas as pd
import datetime

class Calculator:
    """Perform calculations and manage calculation history."""

    def __init__(self):
        self.config = CalculatorConfig()
        self.config.validate()
        self.history = []
        self.undo_stack = []
        self.redo_stack = []
        self.observers = []

    def add_observer(self, observer: HistoryObserver):
        """Add an observer."""
        self.observers.append(observer)
    
    def remove_observer(self, observer: HistoryObserver):
        """Remove an observer."""
        self.observers.remove(observer)
    
    def notify_observers(self, calculation: Calculation):
        """Notify all observers when a calculation is performed."""

        for observer in self.observers:
            observer.update(calculation)


    def perform_operation(self, operation, a, b):
        """Calculate a result and save it in history."""

        if abs(a) > self.config.max_input_value or abs(b) > self.config.max_input_value:
            raise ValidationError("Input exceeds maximum allowed value")
        
        calculation = Calculation(operation, a, b)

        snapshot = CalculatorMemento(self.history)
        self.undo_stack.append(snapshot)

        self.history.append(calculation)

        if len(self.history) > self.config.max_history_size:
            self.history.pop(0)

        self.redo_stack.clear()
        self.notify_observers(calculation)

        return calculation.result

    def show_history(self):
        """Show all recorded calculations."""
        return [str(calculation) for calculation in self.history]

    
    def save_history(self):
        """Save the calculation history to a CSV file using pandas."""

        self.config.history_dir.mkdir(parents=True, exist_ok=True)

        history_data = []

        for calculation in self.history:
            history_data.append({
                "operation": calculation.operation,
                "operand1": calculation.operand1,
                "operand2": calculation.operand2,
                "result": calculation.result,
                "timestamp": calculation.timestamp.isoformat()
            })

        columns = [
            "operation", "operand1", "operand2",
            "result", "timestamp"
        ]

        df = pd.DataFrame(history_data, columns=columns)

        df.to_csv(
            self.config.history_file,
            index=False,
            encoding=self.config.default_encoding
        )

    def load_history(self):
        """Load the calculation history from a CSV file using pandas."""

        if not self.config.history_file.exists():
            return

        df = pd.read_csv(
            self.config.history_file,
            encoding=self.config.default_encoding
        )

        self.history = []

        for _, row in df.iterrows():
            calculation = Calculation(
                row["operation"],
                float(row["operand1"]),
                float(row["operand2"])
            )

            calculation.timestamp = datetime.datetime.fromisoformat(
                row["timestamp"]
            )

            self.history.append(calculation)

        self.undo_stack.clear()
        self.redo_stack.clear()

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

