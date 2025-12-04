todo_list =[]
def show():
    print("1.add")
    print("2. view")
    print("3. remve")
    print("4. exit")
    print("choose the number from above according to task")

while True:
    show()
    num=(int(input("enter your number:")))
    if num ==1:
        task = input("enter your task:")
        todo_list.append(task)
        print("task is added")
    elif num==2:
        if not todo_list:
            print("no task is availabe")
        else:
            for i,task in enumerate(todo_list, start=1):
                print(f"{i}. {task}")
    elif num==3:
        if not todo_list:
            print("no task is available")
        else:
            num1=int(input("enter the number of task which you want ou to remove:"))
            if 1<=(num1)<=len(todo_list):
                removed=todo_list.pop(num1-1)
                print(f"{removed} task is remove")
            else:
                print("invaid")
    elif num==4:
        print("exited the to do  manager")
        break
    else:
        print("invaid information added")
