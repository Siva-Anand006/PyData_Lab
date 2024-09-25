def add_to_list(item,shopping_list):
    if item not in shopping_list:
        shopping_list.append(item)
        print("Item added successfully")
    else:
        print("Item already in list")
        
def remove_item(item,shopping_list):
    if item in shopping_list:
        shopping_list.pop(item)
        print("Item removed from list")
    else:
        print("Item not in list")

def view_list(shopping_list):
    for index,items in enumerate(shopping_list,start=1):
        print(f"{index}. {items}")
        
def mark_item(item,shopping_list):
    try:
        shopping_list[item] = f"[Bought]{shopping_list[item]}"
    except IndexError:
        print("You entered the incorrect index of the item.")

def main():
    
    shopping_list = []
    
    while True:
        print("\n Shopping List Tracker")
        print("1. Add item to list")
        print("2. Remove Item from list")
        print("3. Show shopping list")
        print("4. Mark item")
        print("5. Exit program")
        
        choice = input("Select the index of what you want to do")
        
        if choice == "1":
            item = input("Please enter the Item you wish to add")
            add_to_list(item, shopping_list)
            
        elif choice == "2":
            item = input("Please enter the index of the iten you wish to remove") 
            remove_item(item,shopping_list)
            
        elif choice == "3":
            view_list(shopping_list)
        
        elif choice == "4":
            item = int(input("Enter the index of the item")) - 1
            mark_item(item,shopping_list)
        
        elif choice == "5":
            print("Exiting the program")
            break
        else:
            print("The option selected is invalid")
        
        

if __name__ == "__main__":  
    main()