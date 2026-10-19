# Python Calculator

A command-line calculator application built with Python. It features arithmetic operations, calculation history, undo/redo, logging, and saving history to CSV files.

## Features

- Basic arithmetic: add, subtract, multiply, divide
- Additional operations: power, root, modulus, integer division, percentage, absolute difference
- View, clear, undo, and redo calculation history
- Save and load history using CSV files
- Input validation, error handling, and logging
- Automated tests with pytest

## Installation and Setup Instructions

1. First Create a virtual environment:

   ```bash
   python -m venv venv
   ```

2. Then Activate it:

   ```bash
   source venv/bin/activate
   ```

3. Next Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration Setup

The calculator uses a `.env` file to manage application settings. The `python-dotenv` library loads these environment variables when the application starts.

### Create the `.env` File

In the project's root directory (if not present), create a `.env` file:

```bash
touch .env
```

Open the file and add the following configuration:

```
CALCULATOR_AUTO_SAVE=True
CALCULATOR_MAX_HISTORY_SIZE=1000
CALCULATOR_PRECISION=10
CALCULATOR_MAX_INPUT_VALUE=1e100
CALCULATOR_DEFAULT_ENCODING=utf-8
CALCULATOR_HISTORY_FILE=history/calculator_history.csv
```

### Configuration Variables

| Variable | Description |
|----------|-------------|
| `CALCULATOR_AUTO_SAVE` | Enables or disables automatic saving of calculation history. |
| `CALCULATOR_MAX_HISTORY_SIZE` | Maximum number of calculations stored in history. |
| `CALCULATOR_PRECISION` | Number of decimal places used when rounding results. |
| `CALCULATOR_MAX_INPUT_VALUE` | Maximum allowed absolute value for numeric inputs. |
| `CALCULATOR_DEFAULT_ENCODING` | Character encoding used for file operations. |
| `CALCULATOR_HISTORY_FILE` | Path where calculation history is saved as a CSV file. |

## Logging Configuration

The calculator uses Python's built-in `logging` module to record application activity and errors.

Logging is implemented in `app/logger.py` using a dedicated `Logger` class.

### How Logging Works

The application uses the Observer design pattern to automatically log calculations.

- `LoggingObserver` monitors completed calculations.
- When a calculation is performed, the observer calls the logger.
- The logger records calculation details in a log file.
- Logging also supports warning and error messages.

### Log File Location

Log files are stored in the directory configured by the application's `CalculatorConfig` class.

The logging directory and file path are managed through the `log_dir` and `log_file` configuration properties.

### Configuring Logging

1. Open `app/calculator_config.py` to review the logging configuration.
2. Check the configured log directory and filename.
3. Ensure the application has permission to write to the log directory.
4. Run the calculator using:

   ```bash
   python main.py
   ```

5. Perform a calculation and inspect the log file to verify that the activity was recorded.


## Design Patterns

The calculator application implements three software design patterns to improve code organization, maintainability, and extensibility.

### Factory Pattern

The Factory pattern is implemented in `app/operations.py` using the `OperationFactory` class.

- Creates arithmetic operation objects based on the user's selected command.
- Supports operations such as addition, subtraction, multiplication, and division.
- Allows new arithmetic operations to be added without significantly modifying existing code.
- Separates object creation from calculation execution.

### Observer Pattern

The Observer pattern is implemented in `app/history.py` and integrated into `app/calculator.py`.

- `HistoryObserver` defines the observer interface.
- `LoggingObserver` records completed calculations.
- `AutoSaveObserver` automatically saves calculation history when auto-save is enabled.
- The calculator notifies registered observers after a successful calculation.

This pattern separates logging and persistence responsibilities from the calculator's core logic.

### Memento Pattern

The Memento pattern is implemented in `app/calculator_memento.py`.

- `CalculatorMemento` stores snapshots of calculation history.
- The calculator maintains undo and redo stacks.
- Users can restore previous calculation history states using the `undo` and `redo` commands.
- History snapshots allow state restoration without exposing internal implementation details.


## Usage

To start the calculator, activate the virtual environment and run the following command from the project directory:

```bash
python main.py
```

The calculator starts an interactive command-line interface (REPL). Users can perform arithmetic operations, manage calculation history, save or load calculations, and exit the application. There is also a help command that users can utilize.

### Example Calculation

```text
Welcome to the Advanced Calculator Application!
Type 'exit' to quit. Type 'help' for commands.

Enter operation: add
Enter first number (or 'cancel'): 5
Enter second number (or 'cancel'): 3
Result: 8.0
```

### Available Commands

| Command | Description |
|---------|-------------|
| `add` | Addition |
| `subtract` | Subtraction |
| `multiply` | Multiplication |
| `divide` | Division |
| `power` | Exponentiation |
| `root` | Root calculation |
| `modulus` | Remainder after division |
| `int_divide` | Integer division |
| `percent` | Percentage calculation |
| `abs_diff` | Absolute difference |
| `history` | Display calculation history |
| `clear` | Clear calculation history |
| `undo` | Undo the last calculation |
| `redo` | Redo the last undone calculation |
| `save` | Save calculation history to CSV |
| `load` | Load calculation history from CSV |
| `help` | Display available commands |
| `exit` | Save history and exit the calculator |

Users can type `cancel` when prompted for either operand to cancel the current calculation.

### Color-Coded Outputs

- **Magenta:** Welcome messages and application introduction.
- **Cyan:** Informational messages, help menu, calculation history, and exit messages.
- **Green:** Successful calculations and completed actions.
- **Yellow:** Warnings, cancellations, and unavailable actions.
- **Red:** Errors, invalid commands, and failed operations.

## Testing

Run the tests:

```bash
pytest
```

Check test coverage:

```bash
pytest --cov=app --cov-fail-under=90
```

## GitHub Actions

The workflow succeeds if all tests pass and test coverage is at least 90%.
