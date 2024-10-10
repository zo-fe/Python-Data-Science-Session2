todo_list = []

def add_task(task):
    """Adds a task to the todo list."""
    todo_list.append(task)
    print(f"Task '{task}' added to the list.")

def show_tasks():
    """Prints all tasks in the todo list."""
    print("\nCurrent To-Do List:")
    if todo_list:
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")
    else:
        print("No tasks in the list.")

add_task("Buy groceries")
add_task("Read a book")
show_tasks()
