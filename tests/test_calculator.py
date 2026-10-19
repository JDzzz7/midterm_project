import pytest

from app.calculator import Calculator
from app.calculator_config import CalculatorConfig

@pytest.fixture
def calculator(tmp_path):
    """Create a calculator with temporary storage directories."""
    config = CalculatorConfig()
    config.history_dir = str(tmp_path / "history")
    config.log_dir = str(tmp_path / "logs")
    config.auto_save = False

    return Calculator(config=config)

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