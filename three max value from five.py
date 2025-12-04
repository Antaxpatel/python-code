num1=int(input("enter the first value:"))
num2=int(input("enter the second value:"))
num3=int(input("enter the third value:"))
num4=int(input("enter the four value:"))
num5=int(input("enter the five value:"))

num_final=[num1,num2,num3,num4,num5]
num_final.sort(reverse=True)
print_max=num_final[:3]
print(print_max)