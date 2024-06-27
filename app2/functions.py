"""This module provides functions to manage a todo list."""

DEFAULT_FILEPATH = "todos.txt"


def get_todos(filepath=DEFAULT_FILEPATH):
    """Read the todo list from the file and return it as a list."""
    with open(filepath, "r", encoding="utf-8") as file_local:
        todos_local = file_local.readlines()
    return todos_local


def add_todos(todos_to_add, filepath=DEFAULT_FILEPATH):
    """Read the todo list from the file and return it as a list."""
    with open(filepath, "w", encoding="utf-8") as file_local:
        file_local.writelines(todos_to_add)
