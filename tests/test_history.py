
from unittest.mock import MagicMock, patch
import pytest
from app.history import (
    HistoryObserver,
    LoggingObserver,
    AutoSaveObserver,
)

"""Tests for calculator history observers."""

def test_history_observer_is_abstract():
    """Test that HistoryObserver cannot be instantiated."""
    with pytest.raises(TypeError):
        HistoryObserver()

def test_history_observer_update():
    """Test the abstract update method through a subclass."""

    class TestObserver(HistoryObserver):
        def update(self, calculation):
            return super().update(calculation)

    observer = TestObserver()
    assert observer.update("test") is None

def test_logging_observer_initialization():
    """Test LoggingObserver initialization."""
    with patch("app.history.Logger") as mock_logger:
        observer = LoggingObserver()

        mock_logger.assert_called_once()
        assert observer.logger == mock_logger.return_value

def test_logging_observer_update():
    """Test that calculations are logged."""
    with patch("app.history.Logger") as mock_logger:
        observer = LoggingObserver()
        calculation = MagicMock()

        observer.update(calculation)

        mock_logger.return_value.log_calculation.assert_called_once_with(
            calculation
        )

def test_logging_observer_none():
    """Test LoggingObserver with None."""
    observer = LoggingObserver()

    with pytest.raises(
        AttributeError,
        match="Calculation must not be None"
    ):
        observer.update(None)

def test_auto_save_observer_initialization():
    """Test AutoSaveObserver initialization."""
    calculator = MagicMock()
    observer = AutoSaveObserver(calculator)
    assert observer.calculator is calculator

def test_auto_save_observer_enabled():
    """Test automatic saving when enabled."""
    calculator = MagicMock()
    calculator.config.auto_save = True

    observer = AutoSaveObserver(calculator)
    calculation = MagicMock()
    observer.update(calculation)
    calculator.save_history.assert_called_once()

def test_auto_save_observer_disabled():
    """Test that history is not saved when disabled."""
    calculator = MagicMock()
    calculator.config.auto_save = False

    observer = AutoSaveObserver(calculator)
    calculation = MagicMock()
    observer.update(calculation)
    calculator.save_history.assert_not_called()

def test_auto_save_observer_none():
    """Test AutoSaveObserver with None."""
    calculator = MagicMock()
    observer = AutoSaveObserver(calculator)

    with pytest.raises(
        AttributeError,
        match="Calculation cannot be None"
    ):
        observer.update(None)
        