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

        if command == "history":
            history = calculator.show_history()

            if not history:
                print("No calculations in history.")
            else:
                for calculation in history:
                    print(calculation)

            continue

        if command == "clear":
            calculator.clear_history()
            print("History cleared.")
            continue

        if command == "undo":
            if calculator.undo():
                print("Operation undone.")
            else:
                print("Nothing to undo.")
            continue

        if command == "redo":
            if calculator.redo():
                print("Operation redone.")
            else:
                print("Nothing to redo.")
            continue

        if command == "save":
            try:
                calculator.save_history()
                print("History saved successfully.")
            except (OSError, ValueError) as error:
                print(f"Error saving history: {error}")
            continue

        if command == "load":
            try:
                calculator.load_history()
                print("History loaded successfully.")
            except (OSError, ValueError) as error:
                print(f"Error loading history: {error}")
            continue

        try:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            result = calculator.perform_operation(command, a, b)
            print(f"Result: {result}")

        except (CalculatorError, ValueError, TypeError, ArithmeticError) as error:
            print(f"Error: {error}")
