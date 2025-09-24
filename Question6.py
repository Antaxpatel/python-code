num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))


result = (num1 + num2 > num3) and (num3 % num2 == 0)


print("Result of the expression:", result)