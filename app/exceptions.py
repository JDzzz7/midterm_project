"""For handling exceptions in the calculator application."""

class CalculatorError(Exception):
    """Base exception for calculator errors."""
    pass


class ValidationError(CalculatorError):
    """Raised when calculator inputs are invalid."""
    pass


class OperationError(CalculatorError):
    """Raised when an arithmetic operation fails."""
    pass


class ConfigurationError(CalculatorError):
    """Raised when calculator settings are invalid."""
    pass
