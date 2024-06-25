"""This module provides a simple CLI todo list application.
It allows users to add, show, edit, and complete tasks stored in a todo list.
"""

while True:
    user_action = input("Type add, show, edit, complete or exit: ")
    user_action = user_action.strip()
    if user_action.startswith("add"):
        with open("todos.txt", "r", encoding="utf-8") as file:
            todos = file.readlines()
        todos.append(user_action[4:] + "\n")
        with open("todos.txt", "w", encoding="utf-8") as file:
            file.writelines(todos)

    elif user_action.startswith("show"):
        with open("todos.txt", "r", encoding="utf-8") as file:
            todos = file.readlines()
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}-{item}")

    elif user_action.startswith("edit"):
        try:
            item_index = int(user_action[5:])
            with open("todos.txt", "r", encoding="utf-8") as file:
                todos = file.readlines()
            new_todo = input("Type the new value: ")
            todos[item_index - 1] = new_todo + "\n"
            with open("todos.txt", "w", encoding="utf-8") as file:
                file.writelines(todos)
        except ValueError:
            print("Your command is not valid!")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            with open("todos.txt", "r", encoding="utf-8") as file:
                todos = file.readlines()
            todo_to_remove = todos[number - 1].strip("\n")
            todos.pop(number - 1)
            with open("todos.txt", "w", encoding="utf-8") as file:
                file.writelines(todos)
            print(f"{todo_to_remove} was completed!")
        except IndexError:
            print("Please select a valid number!")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("Invalid command!")

print("Bye!")
