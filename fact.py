try:
    print("Welcome to the Factorial Calculator")

    while True:
        num = int(input("\nPlease enter a number to calculate its factorial: "))

        
        if num < 0:
            print("\nFactorial is not defined for Negative Numbers.")
        elif num == 0:
            print("\nThe Factorial of 0 is 1.")
        else:
            factorial = 1
            factorial_expression = "1"
            
            
            for i in range(2, num + 1):
                factorial *= i
                factorial_expression += f" * {i}"
            print("\nFormula for Calculating the Factorial Number")
            print(f"\n{num}! = {factorial_expression} \n\nThe Factorial of {num} is {factorial}")

        choice = input("\n\nDo you want to calculate another factorial? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("\nThank you for visiting the Factorial Calculator. \nGoodbye and Come again")
            break
        
except ValueError:
    print("\nInvalid Input. Please enter a number next time.")

