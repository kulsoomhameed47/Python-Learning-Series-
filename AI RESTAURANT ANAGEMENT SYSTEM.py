print("********Welcome to AI Restaurant*******")

person=int(input("How many person you are? \n1. 8 to 15 \n2. 6 to 8 \n3. 4 to 6 \n4. 2 to 4 \nSelect any of the above?:\n"))
person2=int(input("Whats the Count of Person you have:\n"))

if person==1:
    #budget=int(input("Enter you budget:"))
    if person2>=8 and person<=15:
        version=int(input("What do you want us to do for you?: \n1. Something Special? \n2. Something in Mind? \nSelect any one?:\n"))
        print("\n*====================================*")
        if version==1:
            fav=int(input("what you eat commonly? \n1. Biryani \n2.Karahi \n3. BBQ \nSelect any one:\n"))
            print("\n*====================================*")
            if fav==1:
                time=int(input("How often do you eat Biryani \n1. Regularly? \n2. Weekly  \n3. Monthly?\n"))
                print("\n*====================================*")
                if time==1:
                    variant=int(input("Do you want: \n1. Chicken \n2. Mutton (Most Recommended) \n3. Beef (Most Recommended)\n"))
                    print("\n*====================================*")
                    if variant==1:
                        typ=int(input("Do you want to eat \n1. Bombay Biryaani \n2. Sindhi Biryaani \n3. Hyderabadi Biryani \n4.Type anything something Special in Rice \nSelect any specific from above: \n"))
                        print("\n*====================================*")
                        if typ==1:
                            print("*************Moving for Bombay Biryaani Lover*********")
                            bir_daigh=2200 #for Regularly chicken biryaani lover #16500
                            sajji_per=2000 #15000
                            kunaffa=1500 #11250
                            gulabj=100 #3000
                            special_dr=600 #9000 
                            meetha_p=100 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            daigh_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(bir_daigh*daigh_kg)+(sajji_per*quantity)+(kunaffa*quantity)+(gulabj*gulabj_per)+(special_dr*person2)+(meetha_p*person2) #calculation for bill
                            tax = bill /10
                            print("\n*====================================*")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here Confirmed \n1. {daigh_kg}KG Fresh Live Chicken Bombay Biryaani \n2. Fresh Live {quantity} Sajji \n3. {quantity}Kunafah \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Special Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {daigh_kg} KG Fresh Live Chicken Bombay Biryaani Rs.{bir_daigh*daigh_kg}/-  \n***********\n2. Fresh Live {quantity} Sajji Rs.{sajji_per*quantity}/- \n***********\n3. {quantity}Kunafah Rs.{kunaffa*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Special Drink Rs {special_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                            
                        elif typ==2:
                            print("*************Moving for Sindhi Biryaani Lover*********")
                            bir_daigh=2200 #for Regularly chicken biryaani lover #16500
                            tikka_per=1500 #15000
                            kunaffa=1500 #11250
                            gulabj=100 #3000
                            limca_dr=600 #9000 
                            meetha_p=100 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            daigh_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(bir_daigh*daigh_kg)+(tikka_per*quantity)+(kunaffa*quantity)+(gulabj*gulabj_per)+(limca_dr*person2)+(meetha_p*person2) #calculation for bill
                            tax = bill /10
                            print("\n*====================================*")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {daigh_kg}KG Fresh Live Hydrabadi Sindhi Biryaani \n2. Fresh Live {quantity} KG Lahori Tikka \n3. {quantity}Kunafah \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Limca Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {daigh_kg} KG Fresh Live Chicken Hydrabadi Biryaani Rs.{bir_daigh*daigh_kg}/-  \n***********\n2. Fresh Live {quantity} KG Lahori Tikka Rs.{tikka_per*quantity}/- \n***********\n3. {quantity}Rabri Rs.{rabri*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Limca Drink Rs {limca_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                      
                            
                        elif typ==3:
                            print("*************Moving for Hydrabadi Biryaani Lover*********")
                            bir_daigh=2200 #for Regularly chicken biryaani lover #16500
                            qeema_per=1500 #15000
                            rabri=1500 #11250
                            gulabj=100 #3000
                            limca_dr=600 #9000 
                            meetha_p=100 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            daigh_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(bir_daigh*daigh_kg)+(qeema_per*quantity)+(rabri*quantity)+(gulabj*gulabj_per)+(limca_dr*person2)+(meetha_p*person2) #calculation for bill
                            tax = bill / 10
                            print("\n*====================================*")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed \n1. {daigh_kg}KG Fresh Live Chicken Sindhi Biryaani \n2. Fresh Live {quantity} Dum Qeema \n3. {quantity} KG Rabri \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Limca Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {daigh_kg} KG Fresh Live Chicken Sindhi Biryaani Rs.{bir_daigh*daigh_kg}/-  \n***********\n2. Fresh Live {quantity} Dum Qeema Rs.{qeema_per*quantity}/- \n***********\n3. {quantity} KG Rabri Rs.{rabri*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Limca Drink Rs {limca_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                      
                        else:
                            print("*************Moving Towards Our Special Suggestion for you in Rice*********")
                            madbi_plate=6000 #for Regularly chicken biryaani lover #16500
                            dumpukht=2500 #15000
                            icecream_falooda=1200 #11250
                            gulabj=100 #3000
                            almond_milk=600 #9000 
                            fire_meetha_pan=150 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            platter=person2//3.5
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(madbi_plate*platter)+(dumpukht*quantity)+(icecream_falooda*person2)+(gulabj*gulabj_per)+(almond_milk*person2)+(fire_meetha_pan*person2) #calculation for bill
                            tax = bill / 10
                            print("\n*====================================*")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed \n1. {platter} Fresh Afghani Special platter \n2. Fresh Live {quantity} KG dumpukht \n3. {person2} Bowl of Ice Cream Falooda \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Almond Milk \n6. {person2} Special Fire Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {platter} Fresh Afghani Special platter Rs.{madbi_plate*platter}/-  \n***********\n2. Fresh Live {quantity} Dumpukht Rs.{dumpukht*quantity}/- \n***********\n3. {person2} Bowl of Ice Cream Falooda Rs.{icecream_falooda*person2}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Almond Milk Rs {almond_milk*person2}/- \n***********\n6. {person2} Special Fire Meetha Paan Rs {fire_meetha_pan*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")

                    elif variant==2:
                        print("")
                    elif variant==3:
                        print("")
                    else:
                        print("")
                    
                elif time==2:
                    print("")
                elif time==3:
                    print("")
                else:
                    print("")
            elif fav==2:
                print("")
            elif fav==3:
                print("")
            else:
                print("Wrong input, Please Try Again! Last Chance:") 
        else:
            print("")
        
#     elif budget>=10000 and budget<20000: #
#         print("")
#         
#     elif budget>=5000 and budget<10000:
#         print("")
#         
    else:
        print("Please Increase your budget as your count of person is huge!")
        budget2=int(input("Do you want to increase your budget? (\n1.Yes \n2. No):"))
        if budget2==1:
            budget_repeat=int(input("Enter your budget?:"))
            if budget_repeat>=20000:
                print("")
            elif budget_repeat>=10000 and budget_repeat<20000:
                print("")
            elif budget_repeat>=5000 and budget_repeat<10000:
                print("")
            else:
                print("Still You have'nt increased! Thank you for visiting us!")
        else:
            print("Thank you for visiting us!")
        
elif person==2:
    
    
    print("")
elif person==3:
    print("")
elif person==4:
    print("")
else:
    print("")
