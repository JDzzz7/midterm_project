from unittest.mock import MagicMock
from app.logger import Logger

"""Test for calculator logging."""

def test_log_warning():
    """Test logging a warning message."""
    logger = Logger()
    logger.logger = MagicMock()

    logger.log_warning("Test warning message")
    logger.logger.warning.assert_called_once_with(
        "Test warning message"
    )
