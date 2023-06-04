from files.python12 import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)
while True:
    user_info = input("type add ,show ,edit ,complete or exit: ")
    user_info = user_info.strip()

    if user_info.startswith('add'):
        todo = user_info[4:]

        todos = get_todos()

        todos.append(todo + "\n")

        write_todos(todos)

    elif user_info.startswith('show'):
        todos = get_todos()

        for i,char in enumerate(todos):
            i += 1
            char = char.capitalize()
            char = char.strip('\n')
            print(i,'-',char)

    elif user_info.startswith('complete'):
        try:
            number = int(user_info[9:])

            todos = get_todos()
            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todo_to_remove.capitalize()
            todos.pop(index)

            write_todos(todos)

            message = f'\'{todo_to_remove}\' is removed from the todos list'
            print(message)
        except IndexError:
            print("Index entered is invalid")
            continue

    elif user_info.startswith('edit'):
        try:
            number = int(user_info[5:])
            print(number)
            number = number -1

            todos = get_todos()

            new_todo = input("Enter the new todo: ")
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("The command is not valid")
            continue

    elif user_info.startswith('exit'):
        break

    else:
        print("Command is not valid")

print("Bye!!!")