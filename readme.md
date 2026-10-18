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

## Configuration

Create a `.env` file in the project folder to customize settings such as log and history directories, maximum history size, auto-save, and calculation precision. Default settings are used when values are not provided.

## Usage

Available commands:

- `add`, `subtract`, `multiply`, `divide`
- `power`, `root`, `modulus`, `int_divide`, `percent`, `abs_diff`
- `history`, `clear`, `undo`, `redo`
- `save`, `load`, `help`, `exit`

## Testing

Run the tests:

```bash
pytest
```

Check test coverage:

```bash
pytest --cov=app --cov-fail-under=100
```

## GitHub Actions

GitHub Actions runs tests and checks 100% test coverage on pushes and pull requests to the `main` branch.
