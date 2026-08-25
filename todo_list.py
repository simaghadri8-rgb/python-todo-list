todo_list = []

def add_task():
    task =  input("Enter a Task: ")
    todo_list.append({"Task": task, "Status": "pending"})
    print("New Task Added Successfuly!\n")

def view_task():
    print("Your ToDo List: ")
    if len(todo_list) == 0:
        print("No pending tasks!")
    else:
        for index, task in enumerate(todo_list, 1):
            print(f"{index}: {task['Task']} - {task['Status']}")
    print("\n")


def remove_task():
    if len(todo_list) == 0:
        print("\n List is Empty")
    else:
        try:
            search_index = int(input("Enter the task number that you want to remove: ")) - 1
            if 0 <= search_index < len(todo_list):
                removed_task = todo_list.pop(search_index)
                print(f"Task removed: {removed_task['Task']}")
            else:
                print("Invalid Task Number.")
        except ValueError:
            print("Pleas Enter a Valid Task Number. ")


def mark_done():
    if len(todo_list) == 0:
        print("\n List is Empty")
    else:
        try:
            search_index = int(input("Enter the task number that you want to marke as complete")) - 1
            if 0 <= search_index < len(todo_list):
                todo_list[search_index]['Status'] = 'done'
                print(f"Task {todo_list[search_index]['Task']} has been marked as Done.")
            else:
                print("Invalid Task Number.")
        except ValueError:
            print("Pleas Enter a Valid Task Number. ")



def menu():
    while(True):

        print("*** Main Menu ***")
        print("1. Add a New Task")
        print("2. View All Tasks")
        print("3. Remove a Task")
        print("4. Mark a Task as Completed")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            view_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            mark_done()
        elif choice == "5":
            print("Exiting the application...")
            exit()

        else:
            print("Invalid choice! Try again!!! ")

menu()









