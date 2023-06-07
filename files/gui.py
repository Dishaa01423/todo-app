import python12
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter todo", key = "todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values = python12.get_todos(), key ="todos",
                      enable_events=True, size=[45,10])
edit_button = sg.Button("Edit")
complete_button = sg.Button("Complete")
exit_button = sg.Button("Exit")

# button_labels = ["Close","Apply"]
#
# layout = []
# for bl in button_labels:
#     layout.append([sg.Button(bl)])
#
# layout = [[label] , [input_box, add_button],[list_box,edit_button]]

window = sg.Window("My To-Do App",
                   layout = [[label] ,
                             [input_box, add_button],
                             [list_box, edit_button, complete_button],
                             [exit_button]],
                   font = ('Helvetica',20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    print(values['todos'])
    match event:
        case 'Add':
            todos = python12.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            python12.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo']
            todos = python12.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            python12.write_todos(todos)
            window['todos'].update(values=todos)

        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = python12.get_todos()
            todos.remove(todo_to_complete)
            python12.write_todos(todos)
            window['todos'].update(values=todos)
            window['todo'].update(value='')

        case 'Exit':
            break

        case 'todos':
            window['todo'].update(value=values['todos'][0])

        case sg.WIN_CLOSED:
            break
print("hello")
window.close()
# label1 = sg.Text("Enter feel:")
# input1 = sg.Input()
# label2 = sg.Text("Enter inches:")
# input2 = sg.Input()
# convert_button = sg.FilesBrowse("Convert")
#
# windows = sg.Window("Convertor", layout = [[label1, input1],[label2, input2],[convert_button]])
# windows.read()
# windows.close()
