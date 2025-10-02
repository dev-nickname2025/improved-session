def grade_checker():
    mark = int(input("Enter your mark: "))
    if mark >= 80:
        print("Grade: A")
    elif mark >=  70:
        print("Grade: B")
    elif mark >= 60:
        print("Grade: C")
    elif mark >= 50:
        print("Grade: D")
    else:
        print("FaiL")
    
tasks = []
def todo_list():
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Delete Tasks")
        print("4. Back to Main Menu")

        choice = input("Select an Option: ")
        if choice == '1':
            task = input("Enter a task: ")
            tasks.append(task)
            print("Task added.")
        elif choice == '2':
            if not tasks:
                print("No tasks in the list.")
            else:
                for i, t in enumerate(tasks, start=1):
                    print(i, "-", t)
        elif choice == '3':
            if not tasks:
                print("The list is empty.")
            else:
                print("Your tasks: ")
                for i, t in enumerate(tasks, start=1):
                    print(i, "-", t)
                try:
                    index = int(input("Enter the task number to delete: "))
                    if 1 <= index <= len(tasks):
                        removed = tasks.pop(index - 1)
                        print(f"Deleted task: {removed}")
                    else:
                        print("Invalid task number.")
                except ValueError:
                    print("Please enter a valid number")
        elif choice == '4':
            break
        else:
            print("Invalid option. Please try again.")
    
def number_analyzer():
    num = int(input("Enter a number:"))
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
        
    if num > 0:
        print(f"{num} is positive.")
    else:
        print(f"{num} is negative.")

while True:
    print("\n--- Student Productivity App ---")
    print("1. Student Grade Checker")
    print("2. To-Do List Manager")
    print("3. Number Analyzer")
    print("4. Quit")

    choice = input("Select an Option: ")

    if choice == '1':
        grade_checker()
    elif choice == '2':
        todo_list()
    elif choice == '3':
        number_analyzer()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")

