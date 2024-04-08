'''
Let's simple project that involves lists, advanced slicing, and indexing. How about we create a program to manage a to-do list?

Here's a rough outline of what we can do:

Add tasks to the to-do list
Remove tasks from the to-do list
View the to-do list
Mark tasks as completed

'''


def add_task(task, todo_list):
    todo_list.append(task)
    print("Task added successfully!")
    
def view_todo_list(todo_list):
    print("To-Do List:")
    for index, task in enumerate(todo_list, start=1):
        print(f"{index}. {task}")

def remove_task(index,todo_list):
    try:
        todo_list.pop(index)
        print("Task removed sucessfully")
    except IndexError:
        print("You entered an index which is not valid")

def mark_completed(index,todo_list):
    try:
        task = todo_list[index]
        todo_list[index] = f"[Completed] {task}" #f"[Completed] {task}"
        print("Task marked as completed ")
    except IndexError:
        print("You entered an index which is not valid")

def main():

    
    todo_list = []
    
    while True: #In this program, while True: is used to create an infinite loop that keeps the program running until the user chooses to exit.
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. View To-Do List")
        print("4. Mark task as completed")
        print("5. Exit program")

        choice = input("Enter your choice (1-4): ") #Note that there was an issue that occured here because we forgot to convert the input to int.
        
        if choice == '1': 
            task = input("Enter the task")
            add_task(task,todo_list)
        
        elif choice == '2':
            index = int(input("Enter the input of the task you want to remove")) - 1
            remove_task(index, todo_list)
            
        elif choice == '3':
            view_todo_list(todo_list)
        
        elif choice == '4':
            view_todo_list(todo_list)
            index = int(input("Enter the index of the task of the task you want to mark as completed.")) - 1
            mark_completed(index, todo_list)
            
        elif choice == '5':
            print("Exiting program...")
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 5.")
            
        
                
    
if __name__ == "__main__":   # why we running this?
    main()