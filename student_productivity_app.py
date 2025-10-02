#student productivity app

tasks = []
students = {}

def grade_checker():
    try:
        grade = int(input("Enter your grade (0-100): "))
        if grade >= 80:
            print("Grade: A")
        elif grade >= 70:
            print("Grade: B")
        elif grade >= 50:
            print("Grade: C")
        else:
            print("You Fail.")
    except ValueError:
        print("Invalid. Please enter number between 0-100.")

def todo_list():
    while True:
        print("\n--- To-Do List Manager ---")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Remove Task")
        print("5. Back to Main Menu")
        option = input("Choose an option: ")
        if option == '1':
            task = input("Enter new task: ")
            tasks.append({"task" : task, "done": False})
            print("Task added!")
        elif option == '2':
            if not tasks:
                print("No tasks yet.")
            else:
                for i, t in enumerate(tasks, start=1):
                    status = "✔ Done" if t["done"] else "✘ Not Done"
                    print(i, "-", t["task"], "-", status)
        elif option == '3':
            try:
                task_no = int(input("Enter task number to mark as done: "))
                tasks[task_no - 1]["done"] = True
                print("Task marked as done!")
            except (ValueError, IndexError):
                print("Invalid task number!")
        elif option == '4':
            try:
                task_no = int(input("Enter task number to remove: "))
                removed_task = tasks.pop(task_no - 1)
                print(f"Removed task: {removed_task['task']}")
            except (ValueError, IndexError):
                print("Invalid task number!")
        elif option == '5':
            break
        else:
            print("Invalid choice, Please Try again.")
    
def number_analyzer():
    try:
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            print(f"{num} is even.")
        else:
            print(f"{num} is odd.")
        if num > 0:
            print(f"{num} is positive.")
        elif num < 0:
            print(f"{num} is negative.")
        else:
            print("The number is zero.")
    except ValueError:
        print("Invalid. Please enter number.")

def student_score_manager():
    name = input("Enter student name: ")
    try:
        mark = int(input("Enter student mark (0-100): "))
        students[name] = mark
        print("Student added!")
        grade_checker_for_student(mark)
    except ValueError:
        print("Invalid. please enter number between 0-100.")

def grade_checker_for_student(mark):
    if mark >= 80:
        print("Grade A")
    elif mark >= 70:
        print("Grade B")
    elif mark >= 50:
        print("Grade C")
    else:
        print("You Fail")

#Main Menu
while True:
    print("\n--- Student Productivity App ---")
    print("1. Student Grade Checker")
    print("2. To-Do list Manager")
    print("3. Number Anzlyzer")
    print("4. Student Score Manager")
    print("5. Quit")

    choice = input("Select an option: ")

    if choice == '1':
        grade_checker()
    elif choice == '2':
        todo_list()
    elif choice == '3':
        number_analyzer()
    elif choice == '4':
        student_score_manager()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid. Please Try again!")