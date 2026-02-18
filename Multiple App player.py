print("**** Multiple App Player ****")
select = int(input("Select an App you want to work: \n1. Calculator \n2. Student Marksheet \n3. Clothing Store \n4. Car Recommendation\n"))

if select == 1:
    name = input("Enter your Name: ")
    method = input("What do you want to do?: \n1. Addition \n2. Subtraction \n3. Division \n4. Multiply\n")
    num1 = eval(input("Enter Number 1 to proceed: "))
    num2 = eval(input("Enter Number 2 to proceed: "))
    if method == "1":
        print(f"This is your Addition: {num1+num2}")
    elif method == "2":
        print(f"This is your Subtraction: {num1-num2}")
    elif method == "3":
        print(f"This is your Division: {num1/num2}")
    elif method == "4":
        print(f"This is your Multiplication: {num1*num2}")
    else:
        print("Inavlid Input")
if select == 2:
    name = input("Enter your Name: ")
    english = eval(input("Enter Your English: "))
    maths = eval(input("Enter Your Maths: "))
    physics = eval(input("Enter Your Physics: "))
    obtainMarks = english+maths+physics
    percentage = (obtainMarks/300)*100
    method = input("What do you want to do?: \n1. See Subject Marks \n2. Obtain Marks \n3.Percentage \n4. Grade:  ")
    if method == "1":
        print(f"Dear {name}, Your English Marks is: {english} \nYour Maths Marks is: {maths} \nYour Physics Marks is: {physics}")
    elif method == "2":
        print(f"Your Obtain Marks is: {obtainMarks }")
    elif method == "3":
        print(f"You got {percentage}%")
    elif method == "4":
        if percentage >=80 :
            print("You got A+ Grade")
        elif percentage >=70:
            print("You got B Grade")
        elif percentage >=60:
            print("You got C Grade")
        elif percentage >=50:
            print("You got D Grade")
        elif percentage >=40:
            print("You got E Grade")
        elif percentage <40:
            print("You got Fail")
        else:
            print("Invalid Input by percentage")
    else:
        print("Inavlid Input by Method")
else:
    print("Inavlid Input by selection")
    