def calc():
    while True:
        num1 = eval(input("Enter First number:\n"))
        num2 = eval(input("Enter Second number:\n"))
        select = int(input("Select \n1. Addition \n2. Subtraction \n3. Division \n4. Multiplication"))
        
        if select == 1:
            cal= num1+num2
            var = "Addition"
        elif select==2:
            cal = num1-num2
            var = "Subtraction"
        elif select == 3:
            cal = num1/num2
            var = "Division"
        elif select == 4:
            cal=num1*num2
            var = "Multiplication"
        else:
            cal = "Wrong Input"
        print(f"{var} of {num1} and {num2} is: {cal}")
        rerun = input("Do you want to continue? yes/no\n")
        if rerun=="yes":
            continue
        else:
            break

calc()