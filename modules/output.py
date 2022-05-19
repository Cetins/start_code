# Functions to complete:

## Get a list of uncompleted tasks
def get_uncompleted_tasks(list):
    return get_tasks_by_status(list, False)
    

## Get a list of completed tasks
def get_completed_tasks(list):
    return get_tasks_by_status(list, True)
        
## Get tasks where time_taken is at least a given time
def get_tasks_taking_at_least(list, time):
    tasks_taking_at_least = []

    for index, task in enumerate(list):
        if time <= list[index]["time_taken"]:
            tasks_taking_at_least.append(list[index]["description"])

    print(tasks_taking_at_least)   
    

## Find a task with a given description
def get_task_with_description(list, description):
    
    for index, task in enumerate(list):
        if description == list[index]["description"]:
            print(list[index])
            break
            
# CHECK FOR THE RETURN NONE IN TERMINAL

# Extention (Function): 

## Get a list of tasks by status
def get_tasks_by_status(list, status):
    status = input("Check a task")
    chosen_tasks = []
    
    for index, task in enumerate(tasks):
        if tasks[index]["completed"] == status:
            chosen_tasks.append(tasks[index]["description"])
    print(chosen_tasks)
    
def mark_task_complete(task):
    for item in tasks:
        if task == item["description"]:
            item["completed"] = True
    

def create_task(description, time_taken):
    task = {}
    task["description"] = description
    task["completed"] = False
    task["time_taken"] = time_taken

    return task

def add_to_list(list, task):
    list.append(task)

def print_task(task):
    print(f'Description: { task["description"] }')
    print(f'Status: { "Completed" if task["completed"] else "Incomplete"}')
    print(f'Time Taken: {task["time_taken"]} mins')

def print_list(list):
    pass
    # for task in list:
    #     print_task(task)

def print_menu():
    print("Options:")
    print("1: Display All Tasks")
    print("2: Get Uncompleted Tasks")
    print("3: Get Completed Tasks")
    print("4: Mark Task as Complete")
    print("5: Get Tasks Which Take Longer Than a Given Time")
    print("6: Find Task by Description")
    print("7: Add a new Task to list")
    print("M or m: Display this menu")
    print("Q or q: Quit")