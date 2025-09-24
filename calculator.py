def three_number_calculator():
    """
    A calculator program that takes 3 numbers as input and performs various operations
    """
    print("=== Three Number Calculator ===")
    print("This calculator performs operations on 3 numbers")
    print()
    
    try:
        # Get input for 3 numbers
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        num3 = float(input("Enter the third number: "))
        
        print(f"\nYour first numbers are: {num1},\nYour second numbers are: {num2},\nYour third numbers are: {num3}")
        print("\nAvailable operations:")
        print("1. Add all three numbers")
        print("2. Multiply all three numbers")
        print("3. Find the average of three numbers")
        print("4. Find the maximum of three numbers")
        print("5. Find the minimum of three numbers")
        print("6. Subtract (num1 - num2 - num3)")
        print("7. Calculate (num1 + num2) * num3")
        print("8. Calculate (num1 * num2) / num3")
        
        choice = int(input("\nEnter your choice (1-8): "))
        
        if choice == 1:
            result = num1 + num2 + num3
            print("total is",result)
            
        elif choice == 2:
            result = num1 * num2 * num3
            print(f"Result: {num1} × {num2} × {num3} = {result}")
            
        elif choice == 3:
            result = (num1 + num2 + num3) / 3
            print(f"Result: Average of {num1}, {num2}, {num3} = {result}")
            
        elif choice == 4:
            result = max(num1, num2, num3)
            print(f"Result: Maximum of {num1}, {num2}, {num3} = {result}")
            
        elif choice == 5:
            result = min(num1, num2, num3)
            print(f"Result: Minimum of {num1}, {num2}, {num3} = {result}")
            
        elif choice == 6:
            result = num1 - num2 - num3
            print(f"Result: {num1} - {num2} - {num3} = {result}")
            
        elif choice == 7:
            result = (num1 + num2) * num3
            print(f"Result: ({num1} + {num2}) × {num3} = {result}")
            
        elif choice == 8:
            if num3 != 0:
                result = (num1 * num2) / num3
                print(f"Result: ({num1} × {num2}) ÷ {num3} = {result}")
            else:
                print("Error: Cannot divide by zero!")
        
        else:
            print("Invalid choice! Please select 1-8.")
            
    except ValueError:
        print("Error: Please enter valid numbers!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the calculator
three_number_calculator()