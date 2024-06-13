import functions
import PySimpleGUI as sg
import time
import os

if not os.path.exists("todos.txt"):
    with open("todos.txt", "w") as file:
        pass


sg.theme("Black")

clock = sg.Text('', key='clock')
label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button(key="Add", size=2, image_source="add.png", mouseover_colors="LightBlue2", tooltip="Add todo")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
close_button = sg.Button("Exit")
complete_button = sg.Button("Complete")
app_title = "My ToDo app"


layout = [[clock], [label], [input_box, add_button], [list_box, edit_button,complete_button], [close_button]]
window = sg.Window(app_title,
                   layout=layout,
                   font=('Helvetica', 20))
while True:
    event, values = window.read(timeout=500)
    window["clock"].update(value=time.strftime("%Y. %b %d. %H:%M:%S"))
    print("Event: ", event)
    print("-------------")
    print("Values: ", values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value="")
        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo'] + "\n"

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                window['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please select an item first!", title="Error", font=("Helvetica", 20))
                print("Please select an item first")
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Complete':
            try:
                todo_to_complete = values['todos'][0]
                todos = functions.get_todos()
                todos.remove(todo_to_complete)
                functions.write_todos(todos)
                window['todos'].update(values=todos)
                window['todo'].update(value="")
            except IndexError:
                sg.popup("Please select an item first!", title="Error", font=("Helvetica", 20))
                print("Please select an item first")
        case 'Exit':
            window.close()
        case sg.WIN_CLOSED:
            break
print("Bye")
window.close()
