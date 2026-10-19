import pytest
from app.exceptions import (
    CalculatorError,
    ValidationError,
    OperationError,
    ConfigurationError,
)

"""Tests for calculator exceptions."""

def test_calculator_error():
    """Test the base calculator exception."""
    with pytest.raises(CalculatorError, match="Calculator error"):
        raise CalculatorError("Calculator error")

def test_validation_error():
    """Test the validation exception."""
    with pytest.raises(ValidationError, match="Invalid input"):
        raise ValidationError("Invalid input")

def test_operation_error():
    """Test the operation exception."""
    with pytest.raises(OperationError, match="Operation failed"):
        raise OperationError("Operation failed")

def test_configuration_error():
    """Test the configuration exception."""
    with pytest.raises(ConfigurationError, match="Invalid configuration"):
        raise ConfigurationError("Invalid configuration")

def test_validation_error_inheritance():
    """Verify ValidationError inherits from CalculatorError."""
    assert issubclass(ValidationError, CalculatorError)

def test_operation_error_inheritance():
    """Verify OperationError inherits from CalculatorError."""
    assert issubclass(OperationError, CalculatorError)

def test_configuration_error_inheritance():
    """Verify ConfigurationError inherits from CalculatorError."""
    assert issubclass(ConfigurationError, CalculatorError)