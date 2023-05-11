from Modules.functions import get_todos, write_todos
import time

now = time.strftime("%b %d, %Y %H:%M:%S")
print("It is", now)

while True:
    # Get user Input and remove space chars from data
    user_action = input("Type add, show, edit or exit:")
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]

        todos = get_todos()
        todos.append(todo + '\n')

        write_todos(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index + 1}: {item}"
            print(row)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo: ")
            todos[number] = new_todo + '\n'
            write_todos(todos)

        except ValueError:
            print("Your command is not valid")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            pending_todo_del = todos[index].strip('\n')
            todos.pop(index)

            write_todos(todos)

            message = f"Todo {pending_todo_del} was removed from the list"
            print(message)
        except IndexError:
            print("No Item")
            continue

    elif user_action.startswith('exit'):
        break
    else:
        print("Command is not valid")

print("Bye")
