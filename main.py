from functions import view_tasks, delete_task, add_task 



def main():
    while True:
        print("Welcome to the To-Do List App!")
        print("1. Add a task")
        print("2. View tasks")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()