tasks = []

print("Simple To-Do List")
print("Commands: add, list, remove, quit")

while True:
    command = input("> ").strip().lower()

    if command == "add":
        task = input("Task: ").strip()
        if task:
            tasks.append(task)
    elif command == "list":
        if not tasks:
            print("No tasks.")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")
    elif command == "remove":
        try:
            index = int(input("Task number: ")) - 1
            print("Removed:", tasks.pop(index))
        except (ValueError, IndexError):
            print("Invalid task number.")
    elif command == "quit":
        break
    else:
        print("Unknown command.")
