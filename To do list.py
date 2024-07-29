import sys

# Initialize an empty to-do list
todo_list = []

print("Welcome to the To-Do List Application") 

while True:
    print("\nMenu:")
    print("1. View To-Do List")
    print("2. Add a Task")
    print("3. Remove a Task")
    print("4. Mark Task as Done")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        if not todo_list:
            print("\nYour to-do list is empty.")
        else:
            print("\nTo-Do List:")
            for idx, task in enumerate(todo_list, start=1):
                status = "Done" if task['done'] else "Not Done"
                print(f"{idx}. {task['task']} [{status}]")

    elif choice == 2:
        task = input("Enter the task: ")
        todo_list.append({"task": task, "done": False})
        print(f"Task '{task}' added to the to-do list.")

    elif choice == 3:
        if not todo_list:
            print("\nYour to-do list is empty.")
        else:
            print("\nTo-Do List:")
            for idx, task in enumerate(todo_list, start=1):
                status = "Done" if task['done'] else "Not Done"
                print(f"{idx}. {task['task']} [{status}]")

            try:
                task_num = int(input("Enter the task number to remove: "))
                if 1 <= task_num <= len(todo_list):
                    removed_task = todo_list.pop(task_num - 1)
                    print(f"Task '{removed_task['task']}' removed from the to-do list.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == 4:
        if not todo_list:
            print("\nYour to-do list is empty.")
        else:
            print("\nTo-Do List:")
            for idx, task in enumerate(todo_list, start=1):
                status = "Done" if task['done'] else "Not Done"
                print(f"{idx}. {task['task']} [{status}]")

            try:
                task_num = int(input("Enter the task number to mark as done: "))
                if 1 <= task_num <= len(todo_list):
                    todo_list[task_num - 1]['done'] = True
                    print(f"Task '{todo_list[task_num - 1]['task']}' marked as done.")
                else:
                    print("Invalid task number.")
            except ValueError:
                print("Please enter a valid number.")

    elif choice == 5:
        print("Exiting the To-Do List application. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")