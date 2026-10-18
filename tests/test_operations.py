"""Unit tests for calculator operations."""

import pytest
from app.operations import Addition, Subtraction, Multiplication

class TestAddition:
    """Test Addition operation."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (5, 3, 8),
            (-5, -3, -8),
            (-5, 3, -2),
            (5, -5, 0),
            (5.5, 3.3, 8.8),
        ]
    )
    def test_valid_operations(self, a, b, expected):
        """Test addition with different valid inputs."""
        operation = Addition()
        result = operation.execute(a, b)
        assert result == pytest.approx(expected)

class TestSubtraction:
    """Test Subtraction operation."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (5, 3, 2),
            (-5, -3, -2),
            (-5, 3, -8),
            (5, 5, 0),
            (5.5, 3.3, 2.2),
        ]
    )
    def test_valid_operations(self, a, b, expected):
        """Test subtraction with different valid inputs."""
        operation = Subtraction()
        result = operation.execute(a, b)
        assert result == pytest.approx(expected)

class TestMultiplication:
    """Test Multiplication operation."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (5, 3, 15),
            (-5, -3, 15),
            (-5, 3, -15),
            (5, 0, 0),
            (5.5, 3.3, 18.15),
        ]
    )
    def test_valid_operations(self, a, b, expected):
        """Test multiplication with different valid inputs."""
        operation = Multiplication()
        result = operation.execute(a, b)
        assert result == pytest.approx(expected)