import random
print("welcome to the number gusing game")
lower=1
upper=10
attempt=0
while True:
    num =int(input("enter your number 1 to 10"))
    if lower<=num<=upper:
        secret=random.randint(lower,upper)
        attempt+=1
        if num<secret:
            print(f"{num} is lower then {secret}")
        elif num>secret:
            print(f"{num} is upper then {secret}")
        elif num==secret:
            print(f"congraes you guses correct in attempt:{attempt}")
            break
    else:
        print("invaid")
        break