contactname_list=[]
contactnumber_list = []

def show():
    print("1. add contact")
    print("2. search contact")
    print("3. remove contact")
    print("choose number according to your work")

while True:
    show()
    choose = int(input("enter your number:"))
    
    if choose ==1:
            add1= (input("enter name:"))
            add2= (input("enter number:"))
            contactname_list.append(add1)
            contactnumber_list.append(add2)
            print("contact saved")
    if  len(contactname_list)>=1 and len(contactnumber_list)>=1:
            if choose==2:
                
                if True:
                    search=input("enter name to search for number:")
                    if True:
                        i=contactname_list.index(search)
                        j=contactnumber_list[i]
                        print(f"{j} is a save number")
            elif choose ==3:
                remove1= (input("enter name or number you want to remove:"))
                idx = contactname_list.index(remove1)
                contactname_list.pop(idx)
                contactnumber_list.pop(idx)
                print("contact is removed")
    else:
        print("no such information in contact list")
else:
    print("invaid")
