control = True
while control:
    card = int(input("Insert your Card: \n1. Card Inserted \n2. Card Error"))
    if card == 1:
        chance = 3
        while chance >= 0:
            pin = int(input("Enter your Pin to proceed: "))
            if pin == 1234:
                print("Welcome to the ATM")
                balance = 5000
                select = int(input("Select any option \n1. Fast Cash \n2. Cash Withdrawl \n3. Balance Inquiry \n4. Type  anything for Exist\n"))
                if select ==1:
                    print("Prcoeeding to Fast Cash")
                elif select == 2:
                    print("Prcoeeding to Cash Withdrawl")
                elif select == 3:
                    print("Prcoeeding to Balance Inquiry")
                else:
                    print("Prcoeeding to Balance Inquiry")
                control = False
                break
            else:
                print(f"You have {chance} Chance Left!")
                chance = chance -1
                continue      
        else:
            print("Card has been Captured")
            break
    else :
        print("Car Error")
        rerun = int(input("Do ypu want to insert card again? \n1. Yes \n2. No :"))
        if rerun == 1:
            continue
        else:
            print("Thank You for Visiting")
            break
        
                    
                    
