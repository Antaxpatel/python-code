y = 3
while y!=0:
    username = (input("enter your username")).lower()
    pin = int(input("enter your 4 digit pin"))
    if username == "a":
        if pin ==1234:
            print("login done")
            break
        else :
            print("pin is invaid")
            y -=1
            print("attempt left are:",y)
    else:
        print("invaid username")
        y -=1
        print("attempt left are:",y)
if y ==0 :
    print("attempt are closed")