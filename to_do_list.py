tasks = []

while True:
    print("\n--- TO DO LIST ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, task)

    elif choice == "2":
        task = input("Enter new task: ")
        tasks.append(task)
        print("Task added successfully.")

    elif choice == "3":
        task_num = int(input("Enter task number to delete: "))
        if 0 < task_num <= len(tasks):
            tasks.pop(task_num - 1)
            print("Task deleted.")
        else:
            print("Invalid task number")

    elif choice == "4":
        print("Goodbye!")
        break
