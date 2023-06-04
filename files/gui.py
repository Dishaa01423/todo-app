import python12
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip = "Enter a To-Do", key = "todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App",
                   layout =[[label] , [input_box, add_button]],
                   font = ('Helvetica',20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = python12.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            python12.write_todos(todos)
        case sg.WIN_CLOSED:
            break
window.close()



# label1 = sg.Text("Select files to compress:")
# input1 = sg.Input()
# choose_button1 = sg.FilesBrowse("Choose")
# label2 = sg.Text("Select destination folder:")
# input2 = sg.Input()
# choose_button2 = sg.FilesBrowse("Choose")
# compress_button = sg.FilesBrowse("Compress")
#
# windows = sg.Window("File Zipper", layout =[[label1, input1, choose_button1],[label2, input2, choose_button2],[compress_button]])
# windows.read()
# windows.close()


# label1 = sg.Text("Enter feel:")
# input1 = sg.Input()
# label2 = sg.Text("Enter inches:")
# input2 = sg.Input()
# convert_button = sg.FilesBrowse("Convert")
#
# windows = sg.Window("Convertor", layout = [[label1, input1],[label2, input2],[convert_button]])
# windows.read()
# windows.close()
