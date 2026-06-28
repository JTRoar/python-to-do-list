

#create the task list. We'll use a dict for now, class better long term
#we'll use a number as the key and the task name as the value
TASK_LIST = {
    1: "Task 1",
    2: "Task 2",
    3: "Task 3"
}

def view_tasks():
    """View all tasks in the task list."""
    if not TASK_LIST:
        print("No tasks available.")
    else:
        print("Tasks:")
        for key, value in TASK_LIST.items():
            print(f"{key}. {value}")

def delete_task():
    """Delete a task from the task list."""
    view_tasks()
    try:
        task_number = int(input("Enter the task number to delete: "))
        if task_number in TASK_LIST:
            del TASK_LIST[task_number]
            print(f"Task {task_number} deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def add_task():
    """Add a new task to the task list."""
    task_name = input("Enter the task name: ")
    if task_name:
        #use max() to find highest key currently in TASK_LIST dict and add 1
        #store that number as the new_task_number next
        new_task_number = max(TASK_LIST.keys(), default=0) + 1
        TASK_LIST[new_task_number] = task_name
        print(f"Task '{task_name}' added as Task {new_task_number}.")
    else:
        print("Task name cannot be empty.")


