import pytest
import datetime
import pandas as pd
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

def test_calculator_undo(calculator):
    """Test undoing a calculation."""
    calculator.perform_operation("add", 2.0, 3.0)

    result = calculator.undo()

    assert result is True
    assert calculator.history == []

def test_calculator_redo(calculator):
    """Test redoing an undone calculation."""
    calculator.perform_operation("add", 2.0, 3.0)

    calculator.undo()
    result = calculator.redo()

    assert result is True
    assert len(calculator.history) == 1
    assert calculator.history[0].result == 5.0

def test_calculator_undo_empty(calculator):
    """Test undo when there is nothing to undo."""
    result = calculator.undo()

    assert result is False
    assert calculator.history == []

def test_calculator_redo_empty(calculator):
    """Test redo when there is nothing to redo."""
    result = calculator.redo()

    assert result is False
    assert calculator.history == []

def test_calculator_multiple_undo(calculator):
    """Test undoing multiple calculations."""
    calculator.perform_operation("add", 2.0, 3.0)
    calculator.perform_operation("multiply", 4.0, 5.0)

    assert len(calculator.history) == 2

    calculator.undo()
    assert len(calculator.history) == 1
    assert calculator.history[0].result == 5.0

    calculator.undo()
    assert calculator.history == []

def test_calculator_new_operation_clears_redo(calculator):
    """Test that a new calculation clears the redo stack."""
    calculator.perform_operation("add", 2.0, 3.0)

    calculator.undo()
    assert len(calculator.redo_stack) == 1

    calculator.perform_operation("multiply", 4.0, 5.0)

    assert calculator.redo_stack == []
    assert len(calculator.history) == 1
    assert calculator.history[0].result == 20.0

def test_calculator_clear_history(calculator):
    """Test clearing calculator history."""
    calculator.perform_operation("add", 2.0, 3.0)
    calculator.perform_operation("multiply", 4.0, 5.0)

    calculator.clear_history()

    assert calculator.history == []
    assert calculator.undo_stack == []
    assert calculator.redo_stack == []

def test_calculator_clear_empty_history(calculator):
    """Test clearing history when it is already empty."""
    calculator.clear_history()

    assert calculator.history == []

def test_calculator_show_history(calculator):
    """Test displaying calculation history."""
    calculator.perform_operation("add", 2.0, 3.0)
    calculator.perform_operation("multiply", 4.0, 5.0)

    history = calculator.show_history()
    assert len(history) == 2
    assert history[0] == "add(2.0, 3.0) = 5.0"
    assert history[1] == "multiply(4.0, 5.0) = 20.0"

def test_calculator_show_empty_history(calculator):
    """Test displaying empty calculation history."""
    history = calculator.show_history()

    assert history == []

def test_calculator_max_history_size(calculator):
    """Test that history does not exceed its maximum size."""
    calculator.config.max_history_size = 2
    calculator.perform_operation("add", 1.0, 2.0)
    calculator.perform_operation("add", 3.0, 4.0)
    calculator.perform_operation("add", 5.0, 6.0)

    assert len(calculator.history) == 2
    assert calculator.history[0].result == 7.0
    assert calculator.history[1].result == 11.0

def test_calculator_save_history(calculator):
    """Test saving calculation history to CSV."""
    calculator.perform_operation("add", 2.0, 3.0)

    with patch("app.calculator.pd.DataFrame.to_csv") as mock_to_csv:
        calculator.save_history()

        mock_to_csv.assert_called_once()

def test_calculator_save_empty_history(calculator):
    """Test saving an empty calculation history."""
    with patch("app.calculator.pd.DataFrame.to_csv") as mock_to_csv:
        calculator.save_history()

        mock_to_csv.assert_called_once()

def test_calculator_load_history(calculator):
    """Test loading calculation history from CSV."""
    timestamp = datetime.datetime.now().isoformat()

    data = pd.DataFrame({
        "operation": ["add"],
        "operand1": ["2.0"],
        "operand2": ["3.0"],
        "result": ["5.0"],
        "timestamp": [timestamp]
    })

    with patch("app.calculator.pd.read_csv", return_value=data):
        with patch.object(Path, "exists", return_value=True):
            calculator.load_history()

    assert len(calculator.history) == 1
    assert calculator.history[0].operation == "add"
    assert calculator.history[0].operand1 == 2.0
    assert calculator.history[0].operand2 == 3.0
    assert calculator.history[0].result == 5.0

def test_calculator_load_empty_history(calculator):
    """Test loading an empty CSV file."""
    with patch(
        "app.calculator.pd.read_csv",
        return_value=pd.DataFrame()
    ):
        with patch.object(Path, "exists", return_value=True):
            calculator.load_history()

    assert calculator.history == []

def test_calculator_load_history_file_not_found(calculator):
    """Test loading history when the file does not exist."""
    with patch.object(Path, "exists", return_value=False):
        calculator.load_history()

    assert calculator.history == []

def test_calculator_save_history_failure(calculator):
    """Test handling an error while saving history."""
    calculator.perform_operation("add", 2.0, 3.0)

    with patch(
        "app.calculator.pd.DataFrame.to_csv",
        side_effect=Exception("save failed")
    ):
        with pytest.raises(OperationError, match="Failed to save history"):
            calculator.save_history()

def test_calculator_load_history_failure(calculator):
    """Test handling an error while loading history."""
    with patch.object(Path, "exists", return_value=True):
        with patch(
            "app.calculator.pd.read_csv",
            side_effect=Exception("read failed")
        ):
            with pytest.raises(OperationError, match="Failed to load history"):
                calculator.load_history()

def test_calculator_load_history_invalid_operation(calculator):
    """Test loading history containing an unsupported operation."""
    data = pd.DataFrame({
        "operation": ["unknown"],
        "operand1": ["2.0"],
        "operand2": ["3.0"],
        "result": ["5.0"],
        "timestamp": [datetime.datetime.now().isoformat()]
    })

    with patch.object(Path, "exists", return_value=True):
        with patch("app.calculator.pd.read_csv", return_value=data):
            with pytest.raises(OperationError):
                calculator.load_history()

    assert calculator.history == []   

def test_calculator_get_history_dataframe(calculator):
    """Test converting calculation history into a DataFrame."""
    calculator.perform_operation("add", 2.0, 3.0)
    df = calculator.get_history_dataframe()

    assert isinstance(df, pd.DataFrame)
    assert len(df) == 1
    assert df.iloc[0]["operation"] == "add"
    assert float(df.iloc[0]["operand1"]) == 2.0
    assert float(df.iloc[0]["operand2"]) == 3.0
    assert float(df.iloc[0]["result"]) == 5.0

def test_calculator_get_history_dataframe_multiple(calculator):
    """Test DataFrame containing multiple calculations."""
    calculator.perform_operation("add", 2.0, 3.0)
    calculator.perform_operation("multiply", 4.0, 5.0)
    df = calculator.get_history_dataframe()

    assert len(df) == 2
    assert list(df["operation"]) == ["add", "multiply"]
    assert float(df.iloc[0]["result"]) == 5.0
    assert float(df.iloc[1]["result"]) == 20.0

def test_calculator_get_history_dataframe_empty(calculator):
    """Test converting empty history into a DataFrame."""
    df = calculator.get_history_dataframe()

    assert isinstance(df, pd.DataFrame)
    assert df.empty

def test_calculator_multiple_redo(calculator):
    """Test redoing multiple undone calculations."""
    calculator.perform_operation("add", 2.0, 3.0)
    calculator.perform_operation("multiply", 4.0, 5.0)

    calculator.undo()
    calculator.undo()

    assert calculator.history == []

    calculator.redo()
    assert len(calculator.history) == 1
    assert calculator.history[0].result == 5.0

    calculator.redo()
    assert len(calculator.history) == 2
    assert calculator.history[1].result == 20.0

def test_calculator_clear_history_after_undo(calculator):
    """Test clearing history after an undo operation."""
    calculator.perform_operation("add", 2.0, 3.0)
    calculator.perform_operation("multiply", 4.0, 5.0)

    calculator.undo()
    calculator.clear_history()

    assert calculator.history == []
    assert calculator.undo_stack == []
    assert calculator.redo_stack == []

def test_calculator_history_preserves_order(calculator):
    """Test that calculations remain in the correct order."""
    calculator.perform_operation("add", 1.0, 2.0)
    calculator.perform_operation("subtract", 10.0, 4.0)
    calculator.perform_operation("multiply", 3.0, 5.0)

    assert len(calculator.history) == 3
    assert [calc.operation for calc in calculator.history] == [
        "add",
        "subtract",
        "multiply"
    ]

def test_calculator_numeric_string_inputs(calculator):
    """Test that valid numeric strings are accepted."""
    result = calculator.perform_operation("add", "2.5", "3.5")

    assert result == 6.0
    assert len(calculator.history) == 1
    assert calculator.history[0].operand1 == 2.5
    assert calculator.history[0].operand2 == 3.5
