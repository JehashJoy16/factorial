print("\nLet's start the Fibonacci sequence")

while True:
    num_terms = int(input("\n\nSpecify the number of terms you want to view in the Fibonacci sequence : "))

    first_term = 0
    second_term = 1

   
    if num_terms <= 0:
        print("\nNext time, kindly input a digit higher than 0.")
    elif num_terms == 1:
        print("\nFibonacci Series:")
        print(first_term)
    else:
        
        print("\nFibonacci Series:")
        print(first_term)
        print(second_term)

       
        count = 2 

        while count < num_terms:
            next_term = first_term + second_term
            print(next_term)

            
            first_term = second_term
            second_term = next_term

            count += 1

   
    another_input = input("\n\nWould you like to calculate another Fibonacci Sequence? (yes/no) : ").lower()

    if another_input != 'yes':
        print("\nThank you for using this application. \nGoodbye!")
        break

