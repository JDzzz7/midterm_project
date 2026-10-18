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

        if command == "help":
            print("\nAvailable commands:")
            print("  add, subtract, multiply, divide")
            print("  power, root, modulus, int_divide, percent, abs_diff")
            print("  history - Show calculation history")
            print("  clear - Clear calculation history")
            print("  undo  - Undo the last operation")
            print("  redo  - Redo the last undone operation")
            print("  save  - Save history to CSV")
            print("  load  - Load history from CSV")
            print("  help  - Display available commands")
            print("  exit  - Exit the calculator")
            continue

        try:
            """Ensure that the user can cancel the operation by typing 'cancel'."""
            a = input("Enter first number (or 'cancel'): ")

            if a.strip().lower() == "cancel":
                print("Operation cancelled.")
                continue

            b = input("Enter second number (or 'cancel'): ")

            if b.strip().lower() == "cancel":
                print("Operation cancelled.")
                continue

            result = calculator.perform_operation(command, a, b)
            print(f"Result: {result}")

        except (CalculatorError, ValueError, TypeError, ArithmeticError) as error:
            print(f"Error: {error}")
