a = float(input("enter your first number:"))
b = float(input("enter your second number:"))
c = float(input("enter your third number:"))
print("your choose number are :",a,b,c)

print("choice from below")
print("1. sum of all number")
print("2. minimum from all number")
print("3. maxmimum from all number")
print("4. average of all number")
choose = int(input("enter your choice from 1 to 4"))

if choose ==1:
    result = a+b+c
    print("your result are:",result)
elif choose ==2:
    result = min(a,b,c)
    print("your result are:",result)
elif choose ==3:
    result = max(a,b,c)
    print("your result are:",result)
elif choose ==4:
    result = (a+b+c)/3
    print("your result are:",result)
else:
    print("your choice number is invaild")