"""Unit tests for calculator operations."""

import pytest
from app.exceptions import ValidationError
from app.operations import (
    Operation, OperationFactory,
    Addition, Subtraction, Multiplication,
    Division, Power, Root, Modulus,
    IntegerDivision, Percentage, AbsoluteDifference
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

class TestOperationFactory:
    """Test OperationFactory functionality."""

    @pytest.mark.parametrize(
        "name, expected_class",
        [
            ("add", Addition),
            ("subtract", Subtraction),
            ("multiply", Multiplication),
            ("divide", Division),
            ("power", Power),
            ("root", Root),
            ("modulus", Modulus),
            ("int_divide", IntegerDivision),
            ("percent", Percentage),
            ("abs_diff", AbsoluteDifference),
        ]
    )
    def test_create_valid_operations(self, name, expected_class):
        """Test creating all supported operations."""
        operation = OperationFactory.create_operation(name)

        assert isinstance(operation, expected_class)

    def test_case_insensitive_operations(self):
        """Test that operation names are case-insensitive."""
        operation = OperationFactory.create_operation("ADD")

        assert isinstance(operation, Addition)

    def test_create_invalid_operation(self):
        """Test that an unsupported operation raises ValueError."""
        with pytest.raises(ValueError, match="not supported"):
            OperationFactory.create_operation("invalid_op")

    def test_register_valid_operation(self):
        """Test registering a custom operation."""

        class NewOperation(Operation):
            def execute(self, a, b):
                return a + b

        OperationFactory.register_operation("new_op", NewOperation)
        operation = OperationFactory.create_operation("new_op")
        assert isinstance(operation, NewOperation)
        assert operation.execute(5, 3) == 8

    def test_register_invalid_operation(self):
        """Test rejecting a class that does not inherit from Operation."""

        class InvalidOperation:
            pass

        with pytest.raises(TypeError, match="Invalid operation class"):
            OperationFactory.register_operation("invalid", InvalidOperation)

class TestOperation:
    """Test base Operation class functionality."""

    def test_abstract_operation(self):
        """Test that Operation cannot be instantiated directly."""
        with pytest.raises(TypeError):
            Operation()

    def test_str_representation(self):
        """Test that string representation returns the class name."""
        operation = Addition()

        assert str(operation) == "Addition"    

def test_abstract_execute():
    """Test the abstract execute method through a subclass."""

    class TestOperation(Operation):
        def execute(self, a, b):
            return super().execute(a, b)

    operation = TestOperation()
    assert operation.execute(2, 3) is None

def test_validate_operands_success():
    """Test successful operand validation."""

    class TestOperation(Operation):
        def execute(self, a, b):
            return a + b

    operation = TestOperation()
    assert operation.validate_operands(2, 3) is None
    assert operation.validate_operands(2.5, -3.5) is None

def test_validate_operands_invalid_type():
    """Test that invalid operand types raise ValidationError."""

    with pytest.raises(
        ValidationError,
        match="Both operands must be valid numbers"
    ):
        Addition().validate_operands("invalid", 5)
       