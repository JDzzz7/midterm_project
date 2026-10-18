from app.operations import OperationFactory
from app.exceptions import CalculatorError

"""Command-line interface for the calculator application."""

def calculator_repl():
    """Run the calculator command-line interface."""

    print("Welcome to the Advanced Calculator Application!")
    print("Type 'exit' to quit.")

    while True:
        command = input("\nEnter operation: ").strip().lower()

        if command == "exit":
            print("Goodbye!")
            break

        try:
            operation = OperationFactory.create_operation(command)

            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = operation.execute(a, b)
            print(f"Result: {result}")

        except (CalculatorError, ValueError, TypeError, ArithmeticError) as error:
            print(f"Error: {error}")
