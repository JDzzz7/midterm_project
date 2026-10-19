from unittest.mock import patch
from app.calculator_repl import calculator_repl

"""Test the calculator REPL (Read-Eval-Print Loop)."""

def test_repl_exit(monkeypatch, capsys):
    """Test exiting the calculator."""
    inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with patch("app.calculator.Calculator.save_history"):
        calculator_repl()
    output = capsys.readouterr().out

    assert "History saved successfully." in output
    assert "Goodbye!" in output

def test_repl_help(monkeypatch, capsys):
    """Test displaying the help menu."""
    inputs = iter(["help", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator_repl()
    output = capsys.readouterr().out

    assert "Available commands:" in output
    assert "add, subtract, multiply, divide" in output

def test_repl_unknown_command(monkeypatch, capsys):
    """Test entering an invalid command."""
    inputs = iter(["banana", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator_repl()
    output = capsys.readouterr().out

    assert "Unknown command: 'banana'" in output

def test_repl_addition(monkeypatch, capsys):
    """Test performing addition through the REPL."""
    inputs = iter(["add", "2", "3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator_repl()
    output = capsys.readouterr().out
    assert "Result: 5.0" in output

def test_repl_subtraction(monkeypatch, capsys):
    """Test performing subtraction through the REPL."""
    inputs = iter(["subtract", "10", "4", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator_repl()
    output = capsys.readouterr().out
    assert "Result: 6.0" in output

def test_repl_multiplication(monkeypatch, capsys):
    """Test performing multiplication through the REPL."""
    inputs = iter(["multiply", "4", "5", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator_repl()
    output = capsys.readouterr().out
    assert "Result: 20.0" in output

def test_repl_history_empty(monkeypatch, capsys):
    """Test displaying empty calculation history."""
    inputs = iter(["history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator_repl()
    output = capsys.readouterr().out
    assert "No calculations in history." in output

def test_repl_history_with_entry(monkeypatch, capsys):
    """Test displaying calculation history."""
    inputs = iter(["add", "2", "3", "history", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator_repl()
    output = capsys.readouterr().out
    assert "add(2.0, 3.0) = 5.0" in output

def test_repl_clear(monkeypatch, capsys):
    """Test clearing calculation history."""
    inputs = iter(["add", "2", "3", "clear", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator_repl()
    output = capsys.readouterr().out
    assert "History cleared." in output

def test_repl_undo_empty(monkeypatch, capsys):
    """Test undo when there is nothing to undo."""
    inputs = iter(["undo", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator_repl()
    output = capsys.readouterr().out
    assert "Nothing to undo." in output

def test_repl_undo_success(monkeypatch, capsys):
    """Test successfully undoing a calculation."""
    inputs = iter(["add", "2", "3", "undo", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator_repl()
    output = capsys.readouterr().out
    assert "Operation undone." in output

def test_repl_redo_empty(monkeypatch, capsys):
    """Test redo when there is nothing to redo."""
    inputs = iter(["redo", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator_repl()
    output = capsys.readouterr().out
    assert "Nothing to redo." in output

def test_repl_redo_success(monkeypatch, capsys):
    """Test successfully redoing a calculation."""
    inputs = iter(["add", "2", "3", "undo", "redo", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator_repl()
    output = capsys.readouterr().out
    assert "Operation redone." in output

def test_repl_cancel_first_number(monkeypatch, capsys):
    """Test cancelling at the first number."""
    inputs = iter(["add", "cancel", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator_repl()
    output = capsys.readouterr().out
    assert "Operation cancelled." in output

def test_repl_cancel_second_number(monkeypatch, capsys):
    """Test cancelling at the second number."""
    inputs = iter(["add", "2", "cancel", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator_repl()
    output = capsys.readouterr().out
    assert "Operation cancelled." in output

def test_repl_invalid_operand(monkeypatch, capsys):
    """Test invalid numeric input."""
    inputs = iter(["add", "abc", "3", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator_repl()
    output = capsys.readouterr().out
    assert "Error:" in output

def test_repl_division_by_zero(monkeypatch, capsys):
    """Test division by zero."""
    inputs = iter(["divide", "10", "0", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    calculator_repl()
    output = capsys.readouterr().out
    assert "Error:" in output

def test_repl_save_success(monkeypatch, capsys):
    """Test saving history through the REPL."""
    inputs = iter(["save", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with patch("app.calculator_repl.Calculator") as mock_calculator:
        calculator_repl()

        assert mock_calculator.return_value.save_history.call_count == 2
    output = capsys.readouterr().out
    assert "History saved successfully." in output

def test_repl_save_error(monkeypatch, capsys):
    """Test handling a save error."""
    inputs = iter(["save", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with patch("app.calculator_repl.Calculator") as mock_calculator:
        mock_calculator.return_value.save_history.side_effect = OSError(
            "Cannot save file"
        )

        calculator_repl()
    output = capsys.readouterr().out
    assert "Error saving history: Cannot save file" in output

def test_repl_load_success(monkeypatch, capsys):
    """Test loading history through the REPL."""
    inputs = iter(["load", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with patch("app.calculator_repl.Calculator") as mock_calculator:
        calculator_repl()

        mock_calculator.return_value.load_history.assert_called_once()
    output = capsys.readouterr().out
    assert "History loaded successfully." in output

def test_repl_load_error(monkeypatch, capsys):
    """Test handling a load error."""
    inputs = iter(["load", "exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    with patch("app.calculator_repl.Calculator") as mock_calculator:
        mock_calculator.return_value.load_history.side_effect = OSError(
            "Cannot load file"
        )

        calculator_repl()
    output = capsys.readouterr().out
    assert "Error loading history: Cannot load file" in output
