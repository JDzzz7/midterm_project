"""Command-line interface for the calculator application."""

from app.exceptions import CalculatorError
from app.calculator import Calculator
from colorama import Fore, init

init(autoreset=True)

"""
Color-Coded Terminal Outputs:

Color meanings:
    MAGENTA - Welcome messages and application introduction.
    CYAN    - Informational messages, help menu, history, and exit messages.
    GREEN   - Successful calculations and completed actions.
    YELLOW  - Warnings, cancellations, and unavailable actions.
    RED     - Errors, invalid commands, and failed operations.
    
"""

def calculator_repl():
    """Run the calculator command-line interface."""

    calculator = Calculator()

    print(Fore.MAGENTA + "Welcome to the Advanced Calculator Application!")
    print(Fore.CYAN + "Type 'exit' to quit. Type 'help' for commands.")

    try:
        while True:
            command = input("\nEnter operation: ").strip().lower()

            if command == "exit":
                try:
                    calculator.save_history()
                    print(Fore.GREEN + "History saved successfully.")
                except (OSError, ValueError) as error:
                    print(Fore.RED + f"Error saving history: {error}")

                print(Fore.CYAN + "Goodbye!")
                break

            if command == "history":
                history = calculator.show_history()

                if not history:
                    print(Fore.YELLOW + "No calculations in history.")
                else:
                    for calculation in history:
                        print(Fore.CYAN + calculation)

                continue

            if command == "clear":
                calculator.clear_history()
                print(Fore.GREEN + "History cleared.")
                continue

            if command == "undo":
                if calculator.undo():
                    print(Fore.GREEN + "Operation undone.")
                else:
                    print(Fore.YELLOW + "Nothing to undo.")
                continue

            if command == "redo":
                if calculator.redo():
                    print(Fore.GREEN + "Operation redone.")
                else:
                    print(Fore.YELLOW + "Nothing to redo.")
                continue

            if command == "save":
                try:
                    calculator.save_history()
                    print(Fore.GREEN + "History saved successfully.")
                except (OSError, ValueError) as error:
                    print(Fore.RED + f"Error saving history: {error}")
                continue

            if command == "load":
                try:
                    calculator.load_history()
                    print(Fore.GREEN + "History loaded successfully.")
                except (OSError, ValueError) as error:
                    print(Fore.RED + f"Error loading history: {error}")
                continue

            if command == "help":
                print(Fore.CYAN + "\nAvailable commands:")
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

            # Check if the command is a valid operation. If not, inform the user and continue the loop."""
            valid_operations = [
                "add", "subtract", "multiply", "divide",
                "power", "root", "modulus", "int_divide",
                "percent", "abs_diff"
            ]

            if command not in valid_operations:
                print(Fore.RED + f"Unknown command: '{command}'. Type 'help' for available commands.")
                continue

            try:
                # Allow the user to cancel the operation.
                a = input("Enter first number (or 'cancel'): ")

                if a.strip().lower() == "cancel":
                    print(Fore.YELLOW + "Operation cancelled.")
                    continue

                b = input("Enter second number (or 'cancel'): ")

                if b.strip().lower() == "cancel":
                    print(Fore.YELLOW + "Operation cancelled.")
                    continue

                result = calculator.perform_operation(command, a, b)
                print(Fore.GREEN + f"Result: {result}")

            except (CalculatorError, ValueError, TypeError, ArithmeticError) as error:
                print(Fore.RED + f"Error: {error}")

    except KeyboardInterrupt:
        print(Fore.CYAN + "\nCalculator interrupted. Goodbye!")

    except EOFError:
        print(Fore.CYAN + "\nInput terminated. Goodbye!")
