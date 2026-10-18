from app.operations import OperationFactory
from app.exceptions import CalculatorError
from app.calculator import Calculator

"""Command-line interface for the calculator application."""

def calculator_repl():
    """Run the calculator command-line interface."""

    calculator = Calculator()

    print("Welcome to the Advanced Calculator Application!")
    print("Type 'exit' to quit.")

    while True:
        command = input("\nEnter operation: ").strip().lower()

        if command == "exit":
            print("Goodbye!")
            break

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = calculator.perform_operation(command, a, b)
            print(f"Result: {result}")

        except (CalculatorError, ValueError, TypeError, ArithmeticError) as error:
            print(f"Error: {error}")
