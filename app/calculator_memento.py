import datetime

"""Class for saving and restoring the state of the calculator's history."""
class CalculatorMemento:

    """Save a snapshot of the calculator's history."""

    def __init__(self, history):
        self.history = history.copy()
        self.timestamp = datetime.datetime.now()

    def get_history(self):
        """Return a copy of the saved calculation history."""
        return self.history.copy()

    def to_dict(self):
        """Convert the saved history into a dictionary."""
        return {
            "history": [calculation.to_dict() for calculation in self.history],
            "timestamp": self.timestamp.isoformat()
        }

    @classmethod
    def from_dict(cls, data):
        """Restore a saved memento from a saved history dictionary."""
        from app.calculation import Calculation

        history = [
            Calculation.from_dict(item)
            for item in data["history"]
        ]

        memento = cls(history)
        memento.timestamp = datetime.datetime.fromisoformat(data["timestamp"])
        return memento
