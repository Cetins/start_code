import data.task_list, modules.output
import modules.input as user_input

while (True):
    print_menu()

    if (user_input.selected_option.lower() == 'q'):
        break
    if option == '1':
        print_list(tasks)
    elif option == '2':
        print_list(get_uncompleted_tasks(tasks))
    elif option == '3':
        print_list(get_completed_tasks(tasks))
    elif option == '4':
        
        task = get_task_with_description(tasks,user_input.task_description)
        if task is not None:
            mark_task_complete(task)
            print("Task marked complete")
        else:
            print("Task not found")
    elif option == '5':
        
        print_list(get_tasks_taking_at_least(tasks, user_input.task_duration))
    elif option == '6':
        print(get_task_with_description(tasks, user_input.task_description))
    elif option == '7':
       
        time_taken = int(input("Enter time taken: "))
        task = create_task(user_input.task_description, time_taken)
        tasks.append(task)
    else:
        print("Invalid Input - choose another option")