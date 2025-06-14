while True:
    num1 = int(input("Enter first number "))
    num2 = int(input("Enter second number " ))
    
    case = input("\nEnter operation that you want to perform '+', '-', '/','*' ")
    
    if case == '+':
        res = num1 + num2
    
    elif case == '-':
        res = num1 -num2
        
    elif case == '*':
        res = num1 * num2
        
    elif case == '/':
        if num2 != 0:
            res = num1 / num2
        else: 
            res = "Number2 can't be zero"
            
    else:
        res = "\nInvalid operation!!! \n Please perform operation like '+', '-', '/','*' \n"
        
    print("Result!!! ",res)
        
    recase = input("\nDo you wnat to perform operation another time (yes/no)").lower()
    if recase== "no":
        print("End")
        break
        
            

            
            
        
    