import os

FILE_NAME = 'mytasks.txt'
task_list = []
status = 'undone'
def write_task_to_file(user_task, status):
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME,'a',encoding='utf-8') as f:
            f.write(f"{user_task} || {status}\n")
    else:
        with open(FILE_NAME,'w',encoding='utf-8') as f:
            f.write(f"{user_task} || {status}\n")

def add_task(user_task):
    task_list.append({'text':user_task,'status':status})

    write_task_to_file(user_task, status)


def view_task():
    for i, item in enumerate(task_list):
        if item['status'] == 'undone':
            checkbox = "❌"
        else:
            checkbox = "✅"
        print(f"{i+1}: [{checkbox}]  -->  {item['text']}")


def mark_done(task_num):
    for i,item in enumerate(task_list):
        if i+1 == task_num:
            task_list[i]['status'] = 'done'
    with open(FILE_NAME,'w',encoding='utf-8') as f:
        for items in task_list:
            f.write(f"{items['text']} || {items['status']}\n")
    print("Marked successfuly")

def delete(task_num):
    del task_list[task_num-1]
    with open(FILE_NAME,'w',encoding='utf-8') as f:
        for items in task_list:
            f.write(f"{items['text']} || {items['status']}\n")

print('-' * 20 + 'Task manager' + '-' * 20)

while True:
    print("1. Add Task.")
    print("2. View Tasks.")
    print("3. Mark Task as Completed.")
    print("4. Delete Task.")
    print("5. Exit")
    choice = input("Enter your choice (1-5): ")
    match choice:
        case "1":
            user_task = input("Enter your task: ")
            add_task(user_task)
        case "2":
            view_task()
        case "3":
            task_num = input("Enter the number of task: ")
            if task_num.isdigit():
                if 1<= int(task_num) <= len(task_list):
                    mark_done(int(task_num))
                else:
                    print("Number out of range.")
                    continue
            else:
                print("Invalid entry.")
                continue
                
        case "4":
            task_num = input("Enter the number of task: ")
            if task_num.isdigit():
                if 1<= int(task_num) <= len(task_list):
                    delete(int(task_num))
                else:
                    print("Number out of range.")
                    continue
            else:
                print("Invalid entry.")
                continue
        case "5":
            os.remove(FILE_NAME)
            print("Exiting Task manager....Done")
            break
        case _:
            print("Invalid choice.")