todo_art = '''𝕋𝕆-𝔻𝕆 𝕝𝕚𝕤𝕥'''
todo = []
flag = True
print(todo_art)
while flag:
    print("1.Enter a new task")
    print("2.View tasks")
    print("3.Delete a task")
    print("4.Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        task = input("Enter the task: ")
        todo.append(task)
        print("Task added successfully.")
    elif choice == 2:
        if len(todo) == 0:
            print("No tasks available.")
        else:
            print("Tasks:")
            for i, task in enumerate(todo):
                print(f"{i + 1}. {task}")
    elif choice == 3:
        if len(todo) == 0:
            print("No tasks available.")
        else:
            print("Tasks:")
            for i, task in enumerate(todo):
                print(f"{i + 1}. {task}")
            task_num = int(input("Enter the task number to delete: "))
            if 1 <= task_num <= len(todo):
                deleted_task = todo.pop(task_num - 1)
                print(f"Task '{deleted_task}' deleted successfully.")
            else:
                print("Invalid task number.")
    elif choice == 4:
        print("Bye, bye!!!")
        flag = False
    else:
        print("Invalid choice. Choose again.")
# # This code implements a simple to-do list application that allows users to add, view, and delete tasks.
# # It uses a list to store tasks and provides a menu for user interaction.