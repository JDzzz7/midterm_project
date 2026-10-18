import datetime
import pytest

from app.calculation import Calculation
from app.calculator_memento import CalculatorMemento

"""Test cases for the Calculator Memento class."""

def test_memento_creation():
    """Test creating a memento with calculation history."""
    calc = Calculation("add", 2.0, 3.0)
    history = [calc]

    memento = CalculatorMemento(history)

    assert len(memento.get_history()) == 1
    assert memento.get_history()[0] == calc

def test_memento_empty_history():
    """Test creating a memento with empty history."""
    memento = CalculatorMemento([])

    assert memento.get_history() == []

def test_memento_history_copy():
    """Test that the memento stores a separate copy of history."""
    calc = Calculation("add", 2.0, 3.0)
    history = [calc]
    memento = CalculatorMemento(history)
    history.append(Calculation("multiply", 4.0, 5.0))

    assert len(memento.get_history()) == 1

def test_memento_get_history_copy():
    """Test that get_history returns a copy."""
    calc = Calculation("add", 2.0, 3.0)
    memento = CalculatorMemento([calc])

    restored_history = memento.get_history()
    restored_history.clear()

    assert len(memento.get_history()) == 1

def test_memento_timestamp():
    """Test that the memento records a timestamp."""
    before = datetime.datetime.now()
    memento = CalculatorMemento([])
    after = datetime.datetime.now()

    assert isinstance(memento.timestamp, datetime.datetime)
    assert before <= memento.timestamp <= after

def test_memento_to_dict():
    """Test converting a memento into a dictionary."""
    calculation = Calculation(
        operation="add",
        operand1=2.0,
        operand2=3.0
    )

    memento = CalculatorMemento(history=[calculation])
    data = memento.to_dict()

    assert "history" in data
    assert "timestamp" in data
    assert len(data["history"]) == 1
    assert data["history"][0]["operation"] == "add"
    assert data["history"][0]["operand1"] == "2.0"
    assert data["history"][0]["operand2"] == "3.0"
    assert data["history"][0]["result"] == "5.0"

def test_memento_from_dict():
    """Test restoring a memento from a dictionary."""
    timestamp = datetime.datetime.now()

    data = {
        "history": [
            {
                "operation": "add",
                "operand1": "2.0",
                "operand2": "3.0",
                "result": "5.0",
                "timestamp": timestamp.isoformat()
            }
        ],
        "timestamp": timestamp.isoformat()
    }

    memento = CalculatorMemento.from_dict(data)

    assert len(memento.history) == 1
    assert memento.history[0].operation == "add"
    assert memento.history[0].operand1 == 2.0
    assert memento.history[0].operand2 == 3.0
    assert memento.history[0].result == 5.0
    assert memento.timestamp == timestamp
