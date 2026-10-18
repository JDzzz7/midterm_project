import pytest
from app.calculation import Calculation
from app.exceptions import OperationError, ValidationError

"""Unit tests for the Calculation class."""

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

def test_modulus():
    """Test modulus calculation."""
    calc = Calculation(operation="modulus", operand1=10.0, operand2=3.0)
    assert calc.result == 1.0


def test_integer_division():
    """Test integer division calculation."""
    calc = Calculation(operation="int_divide", operand1=10.0, operand2=3.0)
    assert calc.result == 3.0


def test_percentage():
    """Test percentage calculation."""
    calc = Calculation(operation="percent", operand1=25.0, operand2=100.0)
    assert calc.result == 25.0


def test_absolute_difference():
    """Test absolute difference calculation."""
    calc = Calculation(operation="abs_diff", operand1=10.0, operand2=15.0)
    assert calc.result == 5.0

def test_division_by_zero():
    """Test division by zero raises an error."""
    with pytest.raises(ValidationError):
        Calculation(operation="divide", operand1=8.0, operand2=0.0)


def test_invalid_root():
    """Test even root of a negative number raises an error."""
    with pytest.raises(ValidationError):
        Calculation(operation="root", operand1=-16.0, operand2=2.0)


def test_zero_root():
    """Test zero-degree root raises an error."""
    with pytest.raises(ValidationError):
        Calculation(operation="root", operand1=16.0, operand2=0.0)


def test_negative_power():
    """Test that negative exponents are supported."""
    calc = Calculation(operation="power", operand1=2.0, operand2=-3.0)
    assert calc.result == pytest.approx(0.125)


def test_unknown_operation():
    """Test unsupported operations raise OperationError."""
    with pytest.raises(OperationError, match="not supported"):
        Calculation(operation="unknown", operand1=5.0, operand2=3.0)