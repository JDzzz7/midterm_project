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
