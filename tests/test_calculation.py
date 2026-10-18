import pytest
import datetime
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

def test_timestamp():
    """Test that a calculation records a timestamp."""
    before = datetime.datetime.now()

    calc = Calculation(
        operation="add",
        operand1=2.0,
        operand2=3.0
    )

    after = datetime.datetime.now()

    assert isinstance(calc.timestamp, datetime.datetime)
    assert before <= calc.timestamp <= after

def test_str_representation():
    """Test the string representation of a calculation."""
    calc = Calculation(
        operation="add",
        operand1=2.0,
        operand2=3.0
    )

    assert str(calc) == "add(2.0, 3.0) = 5.0"

def test_negative_cube_root():
    """Test the cube root of a negative number."""
    calc = Calculation(
        operation="root",
        operand1=-27.0,
        operand2=3.0
    )

    assert calc.result == pytest.approx(-3.0)

def test_modulus_by_zero():
    """Test that modulus by zero raises ValidationError."""
    with pytest.raises(ValidationError):
        Calculation(
            operation="modulus",
            operand1=10.0,
            operand2=0.0
        )

def test_zero_to_negative_power():
    """Test that zero raised to a negative power raises an error."""
    with pytest.raises((ValidationError, OperationError)):
        Calculation(
            operation="power",
            operand1=0.0,
            operand2=-2.0
        )

def test_to_dict():
    """Test converting a calculation into a dictionary."""
    calc = Calculation(
        operation="add",
        operand1=2.0,
        operand2=3.0
    )

    result_dict = calc.to_dict()

    assert result_dict == {
        "operation": "add",
        "operand1": "2.0",
        "operand2": "3.0",
        "result": "5.0",
        "timestamp": calc.timestamp.isoformat()
    }

def test_from_dict():
    """Test reconstructing a calculation from a dictionary."""
    data = {
        "operation": "add",
        "operand1": "2.0",
        "operand2": "3.0",
        "result": "5.0",
        "timestamp": datetime.datetime.now().isoformat()
    }

    calc = Calculation.from_dict(data)

    assert calc.operation == "add"
    assert calc.operand1 == 2.0
    assert calc.operand2 == 3.0
    assert calc.result == 5.0
    assert calc.timestamp == datetime.datetime.fromisoformat(data["timestamp"])


def test_invalid_from_dict():
    """Test that invalid calculation data raises OperationError."""
    data = {
        "operation": "add",
        "operand1": "invalid",
        "operand2": "3.0",
        "result": "5.0",
        "timestamp": datetime.datetime.now().isoformat()
    }

    with pytest.raises(OperationError, match="Invalid calculation data"):
        Calculation.from_dict(data)


def test_missing_from_dict_field():
    """Test that missing dictionary fields raise OperationError."""
    data = {
        "operation": "add",
        "operand1": "2.0"
    }

    with pytest.raises(OperationError, match="Invalid calculation data"):
        Calculation.from_dict(data)
        