import pytest
from app.calculator_config import CalculatorConfig
from app.exceptions import ConfigurationError

"""Tests for calculator configuration settings."""

def test_default_configuration(monkeypatch):
    """Test default configuration values."""
    monkeypatch.delenv("CALCULATOR_AUTO_SAVE", raising=False)
    monkeypatch.delenv("CALCULATOR_MAX_HISTORY_SIZE", raising=False)
    monkeypatch.delenv("CALCULATOR_PRECISION", raising=False)
    monkeypatch.delenv("CALCULATOR_MAX_INPUT_VALUE", raising=False)
    monkeypatch.delenv("CALCULATOR_DEFAULT_ENCODING", raising=False)

    config = CalculatorConfig()

    assert config.auto_save is True
    assert config.max_history_size == 1000
    assert config.precision == 10
    assert config.max_input_value == 1e100
    assert config.default_encoding == "utf-8"


def test_custom_configuration(monkeypatch):
    """Test configuration values from environment variables."""
    monkeypatch.setenv("CALCULATOR_AUTO_SAVE", "false")
    monkeypatch.setenv("CALCULATOR_MAX_HISTORY_SIZE", "500")
    monkeypatch.setenv("CALCULATOR_PRECISION", "5")
    monkeypatch.setenv("CALCULATOR_MAX_INPUT_VALUE", "10000")
    monkeypatch.setenv("CALCULATOR_DEFAULT_ENCODING", "utf-8")

    config = CalculatorConfig()

    assert config.auto_save is False
    assert config.max_history_size == 500
    assert config.precision == 5
    assert config.max_input_value == 10000.0
    assert config.default_encoding == "utf-8"

def test_log_directory(monkeypatch, tmp_path):
    """Test the log directory property."""
    monkeypatch.setenv("CALCULATOR_LOG_DIR", str(tmp_path / "logs"))

    config = CalculatorConfig()
    assert config.log_dir == (tmp_path / "logs").resolve()

def test_log_file(monkeypatch, tmp_path):
    """Test the log file property."""
    monkeypatch.setenv(
        "CALCULATOR_LOG_FILE",
        str(tmp_path / "logs" / "calculator.log")
    )

    config = CalculatorConfig()
    assert config.log_file == (
        tmp_path / "logs" / "calculator.log"
    ).resolve()

def test_history_directory(monkeypatch, tmp_path):
    """Test the history directory property."""
    monkeypatch.setenv(
        "CALCULATOR_HISTORY_DIR",
        str(tmp_path / "history")
    )

    config = CalculatorConfig()
    assert config.history_dir == (tmp_path / "history").resolve()

def test_history_file(monkeypatch, tmp_path):
    """Test the history file property."""
    monkeypatch.setenv(
        "CALCULATOR_HISTORY_FILE",
        str(tmp_path / "history" / "calculator_history.csv")
    )

    config = CalculatorConfig()
    assert config.history_file == (
        tmp_path / "history" / "calculator_history.csv"
    ).resolve()

def test_valid_configuration():
    """Test that valid settings pass validation."""
    config = CalculatorConfig()
    config.max_history_size = 100
    config.precision = 10
    config.max_input_value = 1000

    assert config.validate() is None

def test_invalid_max_history_size():
    """Test that maximum history size must be positive."""
    config = CalculatorConfig()
    config.max_history_size = 0

    with pytest.raises(
        ConfigurationError,
        match="max_history_size must be positive"
    ):
        config.validate()

def test_invalid_precision():
    """Test that precision must be positive."""
    config = CalculatorConfig()
    config.precision = 0

    with pytest.raises(
        ConfigurationError,
        match="precision must be positive"
    ):
        config.validate()

def test_invalid_max_input_value():
    """Test that maximum input value must be positive."""
    config = CalculatorConfig()
    config.max_input_value = 0

    with pytest.raises(
        ConfigurationError,
        match="max_input_value must be positive"
    ):
        config.validate()
