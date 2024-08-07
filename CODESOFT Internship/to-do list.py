activity = []

def add_task():
    print("Add a Task to your list")
    task_name = input("Enter your Task ")
    task = {"name" : task_name,
            "status": False}
    activity.append(task)
    print(f"task {task_name} updated successfully")

def view_task():
    if not activity:
        print("No Tasks Found.")
    else:
        print("These are your tasks")
        for index,task in enumerate(activity,start=1):
            status = "Completed" if task["status"] else "Not Completed" 
            print("-" * 110)
            print("Number\t\tTask\t\tStatus")
            print("-" * 110)
            print(f"{index}\t\t{task['name']}\t\t{status}")
    
def update_task():
    task_name = input("Enter the Task name ")
    flag = False
    for task in activity:
        if task["name"] == task_name:
            task["status"] = True
            flag = True
            print(f"{task_name} updated successfully")
    if not flag:
        print("Such an activity does not exist.Enter 1 to add a new activity ")

while True:
    print("   ")
    print("Welcome to your To-Do List")
    print("Select the options either 1,2,3,4")
    print("1.Add Task")
    print("2.View Task")
    print("3.Update Task")
    print("4.Exit")
    choice = int(input("Enter a value "))
    if choice == 1:
        add_task()
    elif choice ==2:
        view_task()
    elif choice == 3:
        update_task()
    elif choice == 4:
        exit()
    else:
        print("Invalid number entered")
