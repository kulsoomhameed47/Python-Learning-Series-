print("***Welcome to AI Restaurant")
name = input("Enter your Name: ")
person = int(input(f"How many Person are you? \n1. 8 to 15 \n2. 6 to 8 \n3. 4 to 6 \n4. 2 to 4 \n Select any one of the above: "))
if person == 1:
    budget = int(input("Enter your budget"))
    if budget >= 20000:
        version = int(input("What do you want us to do for you?: \n1. Something Special \n2. Somethig in mind? \n Select anyone"))
        if version == 1:
            fav = int(input("What do you eact commonly? \1. Biryani \n2. Karahi \n3. BBQ \n Select Anyone"))
            if fav == 1 :
                time = int(input("Do you eat Biryani: \n1. Regularly \n2. Weekly \n Monthly"))
                if time == 1:
                    variant = int(input("Do you want: \n1. Chicken \n2. Mutton (Most Recommended) \n3. Beef (Most Recommended)"))
                    if variant == 1:
                        typ = int(input("Do you want to eat \n1. Bombay Biryani \n2. Sindhi Biryani \n3. Hydrabadi Biryani \n4. Something Special in Rice \n5. Select any specific from above:"))
                        if typ == 1:
                        elif typ == 2:
                        elif typ == 3:
                        else:
                    elif variant == 2:
                    elif variant == 3:
                    else :
                        
                elif time == 2:
                elif time ==3:
                else:
            elif fav == 2::
            elif fav == 3:
            else:
                print("Wrong Input, Please Try again! Last Chance: ")
        else: 
    elif budget >= 10000 and budget < 20000:
    elif budget >= 5000 and budget < 10000:
    else:
        print("Please increase your budget as you count person is huge!")
        budget2 = int(input("Do you want to increase your budget? (\n1. Yes \n2. No):"))
        if budget2 == 1:
            budget_repeat = int(input("Enter Your Budget"))
            if budget_repeat >=20000:
            elif budget_repeat >= 10000 and budget <20000:
            elif budget_repeat >= 5000 and budget < 10000:
            else:
                print("Still You haven't increased! Thank you for visiting us!")
        else:
                print("Thank You for visiting us!")
elif person == 2 :
elif person == 3:
elif person == 4:
else :
    
             