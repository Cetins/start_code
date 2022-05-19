tasks = [
    { "description": "Wash Dishes", "completed": False, "time_taken": 10 },
    { "description": "Clean Windows", "completed": False, "time_taken": 15 },
    { "description": "Make Dinner", "completed": True, "time_taken": 30 },
    { "description": "Feed Cat", "completed": False, "time_taken": 5 },
    { "description": "Walk Dog", "completed": True, "time_taken": 60 },
]


# def get_tasks_by_status(list, status):

#     chosen_tasks = []
    
#     for index, task in enumerate(tasks):
#         if tasks[index]["completed"] == status:
#             chosen_tasks.append(tasks[index]["description"])
#     print(chosen_tasks)

# get_tasks_by_status(tasks, True)

def mark_task_complete(task):
    for item in tasks:
        if task == item["description"]:
            item["completed"] = True

mark_task_complete("Feed Cat")            
            
print(tasks)