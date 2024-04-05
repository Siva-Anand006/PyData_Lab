def add_task(task, todo_list):
    todo_list.append(task)
    print("Task added successfully!")

def remove_task(index, todo_list):
    try:
        task = todo_list.pop(index)
        print(f"Task '{task}' removed successfully!")
    except IndexError:
        print("Invalid task index!")

def view_todo_list(todo_list):
    print("To-Do List:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")

def mark_completed(index, todo_list):
    try:
        task = todo_list[index]
        todo_list[index] = f"[Completed] {task}"
        print(f"Task '{task}' marked as completed!")
    except IndexError:
        print("Invalid task index!")

def main():
    todo_list = []

    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View To-Do List")
        print("4. Mark Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            task = input("Enter the task: ")
            add_task(task, todo_list)
        elif choice == '2':
            view_todo_list(todo_list)
            index = int(input("Enter the index of the task to remove: ")) - 1
            remove_task(index, todo_list)
        elif choice == '3':
            view_todo_list(todo_list)
        elif choice == '4':
            view_todo_list(todo_list)
            index = int(input("Enter the index of the task to mark as completed: ")) - 1
            mark_completed(index, todo_list)
        elif choice == '5':
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
