import FreeSimpleGUI as sg
import functions

label = sg.Text("Type in a to-do: ")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add", tooltip="Add todo")
list_box = sg.Listbox(
    values=functions.get_todos(), key="todos", enable_events=True, size=(45, 10)
)
edit_button = sg.Button("Edit", tooltip="Edit todo")

layout = [[label], [input_box, add_button], [list_box, edit_button]]
options = ("Helvetica", 12)

window = sg.Window(title="Todo List", layout=layout, font=options)
while True:
    event, values = window.read()
    match event:
        case "Add":
            todos = functions.get_todos()
            todos.append(values["todo"] + "\n")
            functions.add_todos(todos)
            window["todos"].update(values=todos)
        case "Edit":
            try:
                todo_to_edit = values["todos"][0]
                new_todo = values["todo"]
                todos = functions.get_todos()
                todo_to_edit_index = todos.index(todo_to_edit)
                todos[todo_to_edit_index] = new_todo + "\n"
                functions.add_todos(todos)
                window["todos"].update(values=todos)
            except IndexError:
                sg.popup("Please select a todo to edit")
        case "todos":
            window["todo"].update(value=values["todos"][0])
        case sg.WIN_CLOSED:
            break