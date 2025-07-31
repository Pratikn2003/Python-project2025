todo_list = []

def add_task(task):
    todo_list.append({"task": task, "done": False})
    print("Task added!")

def delete_task(index):
    if 0 <= index < len(todo_list):
        removed = todo_list.pop(index)
        print(f"Deleted: {removed['task']}")
    else:
        print("Invalid index!")

def mark_done(index):
    if 0 <= index < len(todo_list):
        todo_list[index]["done"] = True
        print("Task marked as done!")
    else:
        print("Invalid index!")

def list_tasks():
    if not todo_list:
        print("No tasks.")
        return
    for i, item in enumerate(todo_list):
        status = "✓" if item["done"] else "✗"
        print(f"{i}. [{status}] {item['task']}")
while True:
    print("\nOptions: add, delete, done, list, quit")
    cmd = input("Enter command: ").strip().lower()

    if cmd == "add":
        task = input("Enter task: ")
        add_task(task)
    elif cmd == "delete":
        index = int(input("Enter task index to delete: "))
        delete_task(index)
    elif cmd == "done":
        index = int(input("Enter task index to mark as done: "))
        mark_done(index)
    elif cmd == "list":
        list_tasks()
    elif cmd == "quit":
        print("Goodbye!")
        break
    else:
        print("Unknown command.")
