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