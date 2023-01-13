from functions import get_todo, write_todo

while True:
    user_input = input("Enter add, show, edit, complete or exit : ")
    user_input = user_input.strip()

    if user_input.startswith('add'):
        new_todo = user_input[4:] + "\n"

        todos = get_todo()

        todos.append(new_todo)

        write_todo(todos)

    elif user_input.startswith('show'):
        todos = get_todo()

        # new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f"{index+1}-{item}"
            print(row)

    elif user_input.startswith('edit'):
        try:
            edit_number = int(user_input[5:])
            edit_number -= 1
            new_todo = input("Enter new todo : ") + "\n"
            todos = get_todo()

            todos[edit_number] = new_todo
            print("Edited!")

            write_todo(todos)
        except ValueError:
            print("Enter the correct index.")
            continue

    elif user_input.startswith('complete'):
        try:
            number = int(user_input[9:])
            number -= 1

            todos = get_todo()

            deleted_todo = todos[number].strip('\n')
            todos.pop(number)

            write_todo(todos)
            message = f"todo {deleted_todo} was removed."
            print(message)
        except IndexError:
            print("Enter a valid index.")
            continue
    elif user_input.startswith('exit'):
        break
    else:
        print("Command not valid.")

print("Bye!")