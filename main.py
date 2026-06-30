
#from functions import add_task, view_tasks, delete_task
#functions.py is for the first iteration without classes
from ToDoClass import TaskList, Task

""" Create two TaskList Objects
One to track completed tasks. active
will track all others. """

completedTaskList = TaskList()
activeTaskList = TaskList()

def main():
    while True:
        print("Welcome to the To-Do List App!")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            task_name = input("Enter the task name: ")
            
            if task_name:
                activeTaskList.add_task(task_name)
            else:
                print("Task name cannot be empty.")
        
        elif choice == "2":
            activeTaskList.view_tasks()
        
        elif choice == "3":
            TaskList.delete_task()
        elif choice == "4":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()