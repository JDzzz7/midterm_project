"""Unit tests for the Calculation class."""

import pytest
from app.calculation import Calculation


def test_addition():
    """Test addition calculation."""
    calc = Calculation(operation="add", operand1=2.0, operand2=3.0)
    assert calc.result == 5.0


def test_subtraction():
    """Test subtraction calculation."""
    calc = Calculation(operation="subtract", operand1=5.0, operand2=3.0)
    assert calc.result == 2.0


def test_multiplication():
    """Test multiplication calculation."""
    calc = Calculation(operation="multiply", operand1=4.0, operand2=2.0)
    assert calc.result == 8.0


def test_division():
    """Test division calculation."""
    calc = Calculation(operation="divide", operand1=8.0, operand2=2.0)
    assert calc.result == 4.0


def test_power():
    """Test power calculation."""
    calc = Calculation(operation="power", operand1=2.0, operand2=3.0)
    assert calc.result == 8.0


def test_root():
    """Test root calculation."""
    calc = Calculation(operation="root", operand1=16.0, operand2=2.0)
    assert calc.result == pytest.approx(4.0)