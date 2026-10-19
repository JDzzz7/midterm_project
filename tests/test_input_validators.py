import pytest
from unittest.mock import MagicMock
from app.input_validators import InputValidator
from app.exceptions import ValidationError

"""Tests for calculator input validation."""

@pytest.fixture
def config():
    """Create a mock calculator configuration."""
    mock_config = MagicMock()
    mock_config.max_input_value = 1000
    return mock_config

def test_validate_positive_number(config):
    """Test a positive number."""
    assert InputValidator.validate_number(10, config) == 10.0

def test_validate_negative_number(config):
    """Test a negative number."""
    assert InputValidator.validate_number(-10, config) == -10.0

def test_validate_zero(config):
    """Test zero."""
    assert InputValidator.validate_number(0, config) == 0.0

def test_validate_decimal(config):
    """Test a decimal number."""
    assert InputValidator.validate_number(3.14, config) == 3.14

def test_validate_numeric_string(config):
    """Test a numeric string."""
    assert InputValidator.validate_number("25.5", config) == 25.5

def test_validate_invalid_string(config):
    """Test an invalid numeric string."""
    with pytest.raises(ValidationError, match="Invalid number format"):
        InputValidator.validate_number("abc", config)

def test_validate_none(config):
    """Test None as input."""
    with pytest.raises(ValidationError, match="Invalid number format"):
        InputValidator.validate_number(None, config)

def test_validate_infinity(config):
    """Test positive infinity."""
    with pytest.raises(ValidationError, match="Input must be a finite number"):
        InputValidator.validate_number(float("inf"), config)

def test_validate_negative_infinity(config):
    """Test negative infinity."""
    with pytest.raises(ValidationError, match="Input must be a finite number"):
        InputValidator.validate_number(float("-inf"), config)

def test_validate_nan(config):
    """Test NaN."""
    with pytest.raises(ValidationError, match="Input must be a finite number"):
        InputValidator.validate_number(float("nan"), config)

def test_validate_exceeds_maximum(config):
    """Test a number exceeding the maximum."""
    with pytest.raises(ValidationError, match="Value exceeds maximum allowed"):
        InputValidator.validate_number(1001, config)

def test_validate_negative_exceeds_maximum(config):
    """Test a negative number exceeding the maximum."""
    with pytest.raises(ValidationError, match="Value exceeds maximum allowed"):
        InputValidator.validate_number(-1001, config)

def test_validate_at_maximum(config):
    """Test a number exactly at the maximum."""
    assert InputValidator.validate_number(1000, config) == 1000.0
    