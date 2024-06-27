"""This module provides a simple CLI todo list application.
It allows users to add, show, edit, and complete tasks stored in a todo list.
"""

import time
from functions import add_todos, get_todos

now = time.strftime("%Y-%m-%d %H:%M:%S")
print(f"It is {now}")


while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        todos = get_todos()
        todos.append(user_action[4:] + "\n")
        add_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}-{item}")

    elif user_action.startswith("edit"):
        try:
            item_index = int(user_action[5:])
            todos = get_todos()
            new_todo = input("Type the new value: ")
            todos[item_index - 1] = new_todo + "\n"
            add_todos(todos)
        except ValueError:
            print("Your command is not valid!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            todos = get_todos()
            todo_to_remove = todos[number - 1].strip("\n")
            todos.pop(number - 1)
            add_todos(todos)
            print(f"{todo_to_remove} was completed!")
        except IndexError:
            print("Please select a valid number!")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid command!")

print("Bye!")
