import pytest

from pathlib import Path
from unittest.mock import patch, PropertyMock
from app.calculator import Calculator
from app.calculator_config import CalculatorConfig
from app.exceptions import OperationError, ValidationError
from app.history import LoggingObserver

@pytest.fixture
def calculator(tmp_path):
    """Create a calculator with temporary directories."""

    with patch.object(
        CalculatorConfig, "history_dir", new_callable=PropertyMock
    ) as mock_history_dir, patch.object(
        CalculatorConfig, "history_file", new_callable=PropertyMock
    ) as mock_history_file, patch.object(
        CalculatorConfig, "log_dir", new_callable=PropertyMock
    ) as mock_log_dir, patch.object(
        CalculatorConfig, "log_file", new_callable=PropertyMock
    ) as mock_log_file:

        mock_history_dir.return_value = tmp_path / "history"
        mock_history_file.return_value = tmp_path / "history" / "calculator_history.csv"
        mock_log_dir.return_value = tmp_path / "logs"
        mock_log_file.return_value = tmp_path / "logs" / "calculator.log"

        yield Calculator()

def test_calculator_initialization(calculator):
    """Test that a calculator starts with empty history."""
    assert calculator.history == []
    assert calculator.undo_stack == []
    assert calculator.redo_stack == []

def test_calculator_addition(calculator):
    """Test addition using the calculator."""
    result = calculator.perform_operation("add", 2.0, 3.0)

    assert result == 5.0
    assert len(calculator.history) == 1

def test_calculator_subtraction(calculator):
    """Test subtraction using the calculator."""
    result = calculator.perform_operation("subtract", 10.0, 4.0)

    assert result == 6.0
    assert len(calculator.history) == 1

def test_calculator_multiplication(calculator):
    """Test multiplication using the calculator."""
    result = calculator.perform_operation("multiply", 4.0, 5.0)

    assert result == 20.0
    assert len(calculator.history) == 1

def test_calculator_division(calculator):
    """Test division using the calculator."""
    result = calculator.perform_operation("divide", 10.0, 2.0)

    assert result == 5.0
    assert len(calculator.history) == 1

def test_calculator_power(calculator):
    """Test exponentiation using the calculator."""
    result = calculator.perform_operation("power", 2.0, 3.0)

    assert result == 8.0
    assert len(calculator.history) == 1

def test_calculator_root(calculator):
    """Test calculating a root."""
    result = calculator.perform_operation("root", 27.0, 3.0)

    assert result == pytest.approx(3.0)
    assert len(calculator.history) == 1

def test_calculator_modulus(calculator):
    """Test modulus using the calculator."""
    result = calculator.perform_operation("modulus", 10.0, 3.0)

    assert result == 1.0
    assert len(calculator.history) == 1

def test_calculator_integer_division(calculator):
    """Test integer division using the calculator."""
    result = calculator.perform_operation("int_divide", 10.0, 3.0)

    assert result == 3.0
    assert len(calculator.history) == 1

def test_calculator_percentage(calculator):
    """Test percentage calculation."""
    result = calculator.perform_operation("percent", 25.0, 200.0)

    assert result == 12.5
    assert len(calculator.history) == 1

def test_calculator_absolute_difference(calculator):
    """Test absolute difference."""
    result = calculator.perform_operation("abs_diff", 5.0, 12.0)

    assert result == 7.0
    assert len(calculator.history) == 1

def test_calculator_invalid_first_operand(calculator):
    """Test invalid first operand."""
    with pytest.raises(ValidationError):
        calculator.perform_operation("add", "invalid", 3.0)

def test_calculator_invalid_second_operand(calculator):
    """Test invalid second operand."""
    with pytest.raises(ValidationError):
        calculator.perform_operation("add", 2.0, "invalid")

def test_calculator_division_by_zero(calculator):
    """Test division by zero."""
    with pytest.raises((ValidationError, OperationError)):
        calculator.perform_operation("divide", 10.0, 0.0)

def test_calculator_invalid_operation(calculator):
    """Test unsupported operation."""
    with pytest.raises(OperationError):
        calculator.perform_operation("unknown", 2.0, 3.0)

def test_calculator_invalid_root(calculator):
    """Test an even root of a negative number."""
    with pytest.raises((ValidationError, OperationError)):
        calculator.perform_operation("root", -16.0, 2.0)

def test_calculator_error_does_not_change_history(calculator):
    """Test that failed calculations are not added to history."""
    with pytest.raises(ValidationError):
        calculator.perform_operation("divide", 10.0, 0.0)

    assert calculator.history == []
    assert calculator.undo_stack == []
    assert calculator.redo_stack == []

def test_add_observer(calculator):
    """Test adding an observer to the calculator."""
    observer = LoggingObserver()

    calculator.add_observer(observer)

    assert observer in calculator.observers

def test_remove_observer(calculator):
    """Test removing an observer from the calculator."""
    observer = LoggingObserver()

    calculator.add_observer(observer)
    calculator.remove_observer(observer)

    assert observer not in calculator.observers

def test_calculator_default_observers(calculator):
    """Test that the calculator initializes with two observers."""
    assert len(calculator.observers) == 2

def test_notify_observers(calculator):
    """Test that observers are notified after a calculation."""
    from unittest.mock import Mock

    observer = Mock()
    calculator.add_observer(observer)

    calculator.perform_operation("add", 2.0, 3.0)

    observer.update.assert_called_once()

    calculation = observer.update.call_args.args[0]

    assert calculation.operation == "add"
    assert calculation.result == 5.0
