"""Unit tests for calculator operations."""

import pytest
from app.exceptions import ValidationError
from app.operations import (
    Addition, Subtraction, Multiplication,
    Division, Power, Root, Modulus, IntegerDivision, Percentage, AbsoluteDifference
)

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

class TestDivision:
    """Test Division operation."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (6, 2, 3),
            (-6, -2, 3),
            (-6, 2, -3),
            (5.5, 2, 2.75),
            (0, 5, 0),
        ]
    )
    def test_valid_operations(self, a, b, expected):
        """Test division with different valid inputs."""
        operation = Division()
        result = operation.execute(a, b)
        assert result == pytest.approx(expected)

    def test_division_by_zero(self):
        """Test that division by zero raises ValidationError."""
        operation = Division()
        with pytest.raises(ValidationError):
            operation.execute(5, 0)

class TestPower:
    """Test Power operation."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (2, 3, 8),
            (5, 0, 1),
            (5, 1, 5),
            (2.5, 2, 6.25),
            (0, 5, 0),
            (2, -3, 0.125),
        ]
    )
    def test_valid_operations(self, a, b, expected):
        """Test power with different valid inputs."""
        operation = Power()
        result = operation.execute(a, b)
        assert result == pytest.approx(expected)

    def test_zero_to_negative_power(self):
        """Test that zero raised to a negative exponent is rejected."""
        operation = Power()
        with pytest.raises((ValidationError, ZeroDivisionError)):
            operation.execute(0, -2)

class TestRoot:
    """Test Root operation."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (9, 2, 3),
            (27, 3, 3),
            (16, 4, 2),
            (2.25, 2, 1.5),
            (-27, 3, -3),
            (0, 2, 0),
        ]
    )
    def test_valid_operations(self, a, b, expected):
        """Test root with different valid inputs."""
        operation = Root()
        result = operation.execute(a, b)
        assert result == pytest.approx(expected)

    @pytest.mark.parametrize(
        "a, b",
        [
            (-9, 2),
            (9, 0),
            (-16, 4),
            (-9, 2.5),
            (0, -2),
        ]
    )
    def test_invalid_operations(self, a, b):
        """Test that invalid roots raise ValidationError."""
        operation = Root()
        with pytest.raises(ValidationError):
            operation.execute(a, b)

class TestModulus:
    """Test Modulus operation."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (10, 3, 1),
            (15, 5, 0),
            (7, 2, 1),
            (-10, 3, 2),
            (10, -3, -2),
            (5.5, 2, 1.5),
        ]
    )
    def test_valid_operations(self, a, b, expected):
        """Test modulus with different valid inputs."""
        operation = Modulus()
        result = operation.execute(a, b)
        assert result == pytest.approx(expected)

    def test_modulus_by_zero(self):
        """Test that modulus by zero raises an error."""
        operation = Modulus()
        with pytest.raises((ValidationError, ZeroDivisionError)):
            operation.execute(10, 0)

class TestIntegerDivision:
    """Test Integer Division operation."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (10, 3, 3),
            (15, 5, 3),
            (7, 2, 3),
            (-10, 3, -4),
            (10, -3, -4),
            (5.5, 2, 2),
        ]
    )
    def test_valid_operations(self, a, b, expected):
        """Test integer division with different valid inputs."""
        operation = IntegerDivision()
        result = operation.execute(a, b)
        assert result == pytest.approx(expected)

    def test_integer_division_by_zero(self):
        """Test that integer division by zero raises an error."""
        operation = IntegerDivision()
        with pytest.raises((ValidationError, ZeroDivisionError)):
            operation.execute(10, 0)

class TestPercentage:
    """Test Percentage operation."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (25, 100, 25),
            (50, 200, 25),
            (75, 100, 75),
            (0, 100, 0),
            (100, 100, 100),
            (25, 50, 50),
            (12.5, 50, 25),
        ]
    )
    def test_valid_operations(self, a, b, expected):
        """Test percentage with different valid inputs."""
        operation = Percentage()
        result = operation.execute(a, b)
        assert result == pytest.approx(expected)

    def test_percentage_by_zero(self):
        """Test that percentage with a zero denominator raises an error."""
        operation = Percentage()
        with pytest.raises((ValidationError, ZeroDivisionError)):
            operation.execute(25, 0)

class TestAbsoluteDifference:
    """Test Absolute Difference operation."""

    @pytest.mark.parametrize(
        "a, b, expected",
        [
            (10, 5, 5),
            (5, 10, 5),
            (-10, 5, 15),
            (10, -5, 15),
            (-10, -5, 5),
            (5, 5, 0),
            (5.5, 3.3, 2.2),
        ]
    )
    def test_valid_operations(self, a, b, expected):
        """Test absolute difference with different valid inputs."""
        operation = AbsoluteDifference()
        result = operation.execute(a, b)
        assert result == pytest.approx(expected)
        