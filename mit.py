x=3
while True:
    a=input("Enter your Username:")
    if a=="Mit":
        b=input("Enter your passcode:")
        if b=="1234":
            print("Welcome")
            break
        else:
            print("Invalid")
            x-=1
            print(f"you have {x} chances left")
    else:
        print("Invalid")
        x-=1
        print(f"you have {x} chances left")
    if x==0:
        print("You have no attempts left")
        break