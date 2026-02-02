print("********Welcome to AI Restaurant*******")

person=int(input("How many person you are? \n1. 8 to 15 \n2. 6 to 8 \n3. 4 to 6 \n4. 2 to 4 \nSelect any of the above?:"))
person2=int(input("Whats the Count of Person you have:"))

if person==1:
    #budget=int(input("Enter you budget:"))
    if person2>=8 and person2<=15:
        version=int(input("What do you want us to do for you?: \n1. Something Special? \n2. Something in Mind? \nSelect any one?: "))
        print("\n*====================================*")
        if version==1:
            fav=int(input("what you eat commonly? \n1.biryani \n2.Karahi \n3.bbq: \nSelect any one:"))
            print("\n*====================================*")
            if fav==1:
                time=int(input("How often Do you eat Biryani \n1.regularly? \n2.weekly  \n3.monthly?"))
                print("\n*====================================*")
                if time==1:
                    variant=int(input("Do you want: \n1. Chicken \n2. Mutton (Most Recommended) \n3. (Type anything for) Beef (Most Recommended)"))
                    print("\n*====================================*")
                    if variant==1:
                        typ=int(input("Do you want to eat \n1. Bombay Biryaani \n2. Sindhi Biryaani \n3. Hyderabadi Biryani \n4.Type anything something Special in Rice \nSelect any specific from above: "))
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
                            tax=bill/10
                            print("\n*====================================*")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {daigh_kg}KG Fresh Live Chicken Bombay Biryaani \n2. Fresh Live {quantity} Sajji \n3. {quantity}Kunafah \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Special Drink \n6. {person2} Special Meetha Paan")
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
                            tax=bill/10
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {daigh_kg}KG Fresh Live Chicken Sindhi Biryaani \n2. Fresh Live {quantity} Lahori Tikka \n3. {quantity}Kunafah \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Limca Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {daigh_kg} KG Fresh Live Chicken Sindhi Biryaani Rs.{bir_daigh*daigh_kg}/-  \n***********\n2. Fresh Live {quantity} Lahori Tikka Rs.{tikka_per*quantity}/- \n***********\n3. {quantity}Kunafah Rs.{kunaffa*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Limca Drink Rs {limca_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                     
                        elif typ==3:
                            print("*************Moving for Hyderabaadi Biryaani Lover*********")
                            bir_daigh=2200 #for Regularly chicken biryaani lover #16500
                            qeema_per=1500 #15000
                            rabri=1500 #11250
                            gulabj=100 #3000
                            limca_dr=600 #9000 
                            meetha_p=100 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            daigh_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(bir_daigh*daigh_kg)+(qeema_per*quantity)+(rabri*person2)+(gulabj*gulabj_per)+(limca_dr*person2)+(meetha_p*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {daigh_kg}KG Fresh Live Chicken Hyderabaadi Biryaani \n2. Fresh Live {quantity}Kg Dum Qeema \n3. {quantity}kg Rabri \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Limca Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {daigh_kg} KG Fresh Live Chicken Hyderabaadi Biryaani Rs.{bir_daigh*daigh_kg}/-  \n***********\n2. Fresh Live {quantity} Kg Dum qeema Rs.{qeema_per*quantity}/- \n***********\n3. {quantity} Rabri Rs.{rabri*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Limca Drink Rs {limca_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                      
                        else:
                            print("*************Moving Towards Our Special Suggestion for you in rice*********")
                            madbi_plat=6000 #for Regularly chicken biryaani lover #16500
                            dumpukht=2500 #15000
                            icecream_falooda=1200 #11250
                            gulabj=100 #3000
                            almond_milk=600 #9000 
                            fire_meetha_pan=150 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            platter=person2//3.5
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(madbi_plat*platter)+(dumpukht*quantity)+(icecream_falooda*person2)+(gulabj*gulabj_per)+(almond_milk*person2)+(fire_meetha_pan*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            #print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {platter} Fresh Afghaani Special Platter \n2. Fresh Live {quantity} KG Dumpukht  \n3. {person2} Bowl Ice Cream Falooda \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Glass Almond Milk \n6. {person2} Special Fire Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {platter} Fresh Afghaani Special Platter Rs.{madbi_plat*platter}/-  \n***********\n2. Fresh Live {quantity} KG Dumpukht Rs.{dumpukht*quantity}/- \n***********\n3. {person2} Bowl Ice Cream Falooda Rs.{person2*icecream_falooda}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Glass Almond Milk Rs.{almond_milk*person2}/- \n***********\n6. {person2} Special Fire Meetha Paan Rs {fire_meetha_pan*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                    elif variant==2:
                        typ=int(input("Do you want to eat \n1. Moroccan Lamb Rice \n2. Classic Dumpukht mutton biryaani \n3. Mutton Kabbuli Pulao \n4.Type anything something Special in Rice \nSelect any specific from above: "))
                        print("\n*====================================*")
                        if typ==1:
                            print("*************Moving for Moroccan Lamb Rice Lover*********")
                            lamb_rice=3000 #for Regularly lamb rice lover #16500
                            saalam_lamb=3000 #15000
                            kunaffa=1500 #11250
                            gulabj=100 #3000
                            special_dr=600 #9000 
                            meetha_p=100 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            platter_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(lamb_rice*platter_kg)+(saalam_lamb*quantity)+(kunaffa*quantity)+(gulabj*gulabj_per)+(special_dr*person2)+(meetha_p*person2) #calculation for bill
                            tax=bill/10

                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {platter_kg}KG Fresh Live Morrocon Lamb rice \n2. Fresh Live {platter_kg} Lamb \n3. {quantity}Kunafah \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Special Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {platter_kg} KG Fresh Live Morrocon Lamb rice Rs.{lamb_rice*platter_kg}/-  \n***********\n2. Fresh Live {Platter_kg} Saalam Lamb Rs.{saalam_lamb*platter_kg}/- \n***********\n3. {quantity}Kunafah Rs.{kunaffa*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Special Drink Rs {special_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
         
                        elif typ==2:
                            print("*************Moving for Classic Dumpukht Mutton Biryaani Lover*********")
                            mutton_bir=4500 #for Regularly chicken biryaani lover #16500
                            mutton_rosh=3500 #15000
                            kunaffa=1500 #11250
                            gulabj=100 #3000
                            limca_dr=600 #9000 
                            meetha_p=100 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            mutton_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(mutton_bir*mutton_kg)+(mutton_rosh*mutton_kg)+(kunaffa*quantity)+(gulabj*gulabj_per)+(limca_dr*person2)+(meetha_p*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {mutton_kg}KG Fresh Live Classic Dumpukht Mutton Biryaani \n2. Fresh Live {mutton_kg} Mutton Rosh \n3. {quantity}Kunafah \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Limca Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {mutton_kg} KG Fresh Live Classic Dumpukht Mutton Biryaani Rs.{mutton_bir*mutton_kg}/-  \n***********\n2. Fresh Live {mutton_kg} kg Mutton Rosh Rs.{mutton_rosh*mutton_kg}/- \n***********\n3. {quantity}Kunafah Rs.{kunaffa*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Limca Drink Rs {limca_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                     
                        elif typ==3:
                            print("*************Moving for Mutton Kabbuli Pulao Lover*********")
                            kabuli_pulao=3000 #for Regularly chicken biryaani lover #16500
                            mutton_peti_kabab=2000 #15000
                            rabri=1500 #11250
                            gulabj=100 #3000
                            limca_dr=600 #9000 
                            meetha_p=100 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            kabuli_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(kabuli_pulao*kabuli_kg)+(mutton_peti_kabab*quantity)+(rabri*person2)+(gulabj*gulabj_per)+(limca_dr*person2)+(meetha_p*person2)
                            tax=bill/10
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {kabuli_kg}KG Fresh Live Chicken Hyderabaadi Biryaani \n2. Fresh Live {person2} Petti Kabaab  \n3. {quantity}kg Rabri \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Limca Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {kabuli_kg} KG Fresh Live Chicken Hyderabaadi Biryaani Rs.{kabuli_pulao*kabuli_kg}/-  \n***********\n2. Fresh Live {person2} Petti Kabaab Rs.{mutton_peti_kabab*person2}/- \n***********\n3. {quantity} Rabri Rs.{rabri*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Limca Drink Rs {limca_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")

                        else:
                            print("*************Moving Towards Our Special Suggestion for you in rice*********")
                            b_plat=6000 #for Regularly badshahi platter lover #16500
                            salim_dumba=4500 #15000
                            icecream_falooda=1200 #11250
                            gulabj=100 #3000
                            almond_milk=600 #9000 
                            fire_meetha_pan=150 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            platter=person2//3.5
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(b_plat*platter)+(salim_dumba*quantity)+(icecream_falooda*person2)+(gulabj*gulabj_per)+(almond_milk*person2)+(fire_meetha_pan*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            #print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {platter} Fresh Afghaani Special Platter \n2. Fresh Live {quantity} Salim Dumba \n3. {person2} Bowl Ice Cream Falooda \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Glass Almond Milk \n6. {person2} Special Fire Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {platter} Fresh Baadshahi Platter Rs.{b_plat*platter}/-  \n***********\n2. Fresh Live {quantity} KG Salim Dumba Rs.{salim_dumba*quantity}/- \n***********\n3. {person2} Bowl Ice Cream Falooda Rs.{person2*icecream_falooda}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Glass Almond Milk Rs.{almond_milk*person2}/- \n***********\n6. {person2} Special Fire Meetha Paan Rs {fire_meetha_pan*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
#                     elif variant==3:
#                         print("")
                    else:
                        #print("")
                        typ=int(input("Do you want to eat \n1. Classic Beef Special Daigh Biryaani \n2.Type anything something Special in Rice with beef \nSelect any specific from above: "))
                        print("\n*====================================*")
                        if typ==1:
                            print("*************Moving for Classic Beef Special Daigh Biryaani Lover*********")
                            classic_daig=1947 #for Regularly lamb rice lover #16500
                            bihaari_kabaab=1408 #15000
                            kunaffa=1499 #11250
                            gulabj=78 #3000
                            special_dr=547 #9000 
                            meetha_p=73 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            daigh_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(classic_daig*daigh_kg)+(bihaari_kabaab*person2*2)+(kunaffa*quantity)+(gulabj*gulabj_per)+(special_dr*person2)+(meetha_p*person2) #calculation for bill
                            tax=bill//14
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {daigh_kg}KG Fresh Live Classic Beef Special Daigh Biryaani rice \n2. Fresh Live {person2*2} Bihaari Kabaab \n3. {quantity}Kunafah \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Special Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {daigh_kg} KG Fresh Live Classic Beef Special Daigh Biryaani rice Rs.{classic_daig*daigh_kg}/-  \n***********\n2. Fresh Live {person2*2} Bihaari Kabaab Rs.{bihaari_kabaab*(person2*2)}/- \n***********\n3. {quantity}Kunafah Rs.{kunaffa*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Special Drink Rs {special_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
         
                    
                        else:
                            print("*************Moving Towards Our Special Suggestion for you in rice with beef*********")
                            beef_hyder_daigh=4359 #for Regularly badshahi platter lover #16500
                            beef_balochi_tikka=2569 #15000
                            icecream_falooda=1200 #11250
                            gulabj=100 #3000
                            almond_milk=600 #9000 
                            fire_meetha_pan=150 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            beef_daigh=person2//3.5
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(beef_hyder_daigh*beef_daigh)+(beef_balochi_tikka*quantity)+(icecream_falooda*person2)+(gulabj*gulabj_per)+(almond_milk*person2)+(fire_meetha_pan*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            #print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {beef_daigh} KG Live Fresh Special Beef Hyderabaadi Daighi Biryaani \n2. Fresh Live {quantity} Beef Balochi Tikka \n3. {person2} Bowl Ice Cream Falooda \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Glass Almond Milk \n6. {person2} Special Fire Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {beef_daigh} KG Live Fresh Special Beef Hyderabaadi Daighi Biryaani Rs.{beef_hyder_daigh*beef_daigh}/-  \n***********\n2. Fresh Live {quantity} Beef Balochi Tikka Rs.{beef_balochi_tikka*quantity}/- \n***********\n3. {person2} Bowl Ice Cream Falooda Rs.{person2*icecream_falooda}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Glass Almond Milk Rs.{almond_milk*person2}/- \n***********\n6. {person2} Special Fire Meetha Paan Rs {fire_meetha_pan*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                    
                elif time==2: #weekly
                    #print("")
                    variant=int(input("Do you want: \n1. Chicken \n2. Mutton (Most Recommended) \n3. (Type anything for) Beef (Most Recommended)"))
                    print("\n*====================================*")
                    if variant==1:
                        typ=int(input("Do you want to eat \n1. Biryaani \n2. Chinese \n3. Fast food \n4.Type anything something Special \nSelect any specific from above: "))
                        print("\n*====================================*")
                        if typ==1:
                            print("*************Moving for Biryaani Lover*********")
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
                            tax=bill/10
                            print("\n*====================================*")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {daigh_kg}KG Fresh Live Chicken Bombay Biryaani \n2. Fresh Live {quantity} Sajji \n3. {quantity}Kunafah \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Special Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {daigh_kg} KG Fresh Live Chicken Bombay Biryaani Rs.{bir_daigh*daigh_kg}/-  \n***********\n2. Fresh Live {quantity} Sajji Rs.{sajji_per*quantity}/- \n***********\n3. {quantity}Kunafah Rs.{kunaffa*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Special Drink Rs {special_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
         
                        elif typ==2:
                            print("*************Moving for Chineese Food Lover*********")
                            chinese_plat=2200 #for Regularly chicken biryaani lover #16500
                            chinese_bowl=1500 #15000
                            lotus_tofu_=1500 #11250
                            dumplings=200 #3000
                            bubble_tea=600 #9000 
                            moon_cake=100 #1500 
                            dumplings_per=person2*2 
                            chinese_per=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(chinese_plat*chinese_per)+(chinese_bowl*person2)+(lotus_tofu_*person2)+(dumplings*dumplings_per)+(bubble_tea*person2)+(moon_cake*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {chinese_per} Live Jumbo platter of Chinese Cuisine \n2. Fresh Live {person2} Chinese Bowl \n3. {person2} Lotus Tofu \n4.{dumplings_per} Dumplings \n5.{person2} Bubble Tea \n6. {person2} Moon Cake")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {chinese_per} Live Jumbo platter of Chinese Cuisine Rs.{chinese_plat*chinese_per}/-  \n***********\n2. Fresh Live {person2} Chinese Bowl Rs.{chinese_bowl*person2}/- \n***********\n3. {person2} Lotus Tofu  Rs.{lotus_tofu_*person2}/- \n***********\n4.{dumplings_per} Dumplings Rs {dumplings*dumplings_per}/- \n***********\n5.{person2} Bubble Tea Rs {bubble_tea*person2}/- \n***********\n6. {person2} Moon Cake Rs {moon_cake*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                     
                        elif typ==3:
                            print("*************Moving for Fast Food  Lover*********")
                            bir_daigh=2200 #for Regularly chicken biryaani lover #16500
                            qeema_per=1500 #15000
                            rabri=1500 #11250
                            gulabj=100 #3000
                            limca_dr=600 #9000 
                            meetha_p=100 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            daigh_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(bir_daigh*daigh_kg)+(qeema_per*quantity)+(rabri*person2)+(gulabj*gulabj_per)+(limca_dr*person2)+(meetha_p*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {daigh_kg}KG Fresh Live Chicken Hyderabaadi Biryaani \n2. Fresh Live {quantity}Kg Dum Qeema \n3. {quantity}kg Rabri \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Limca Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {daigh_kg} KG Fresh Live Chicken Hyderabaadi Biryaani Rs.{bir_daigh*daigh_kg}/-  \n***********\n2. Fresh Live {quantity} Kg Dum qeema Rs.{qeema_per*quantity}/- \n***********\n3. {quantity} Rabri Rs.{rabri*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Limca Drink Rs {limca_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                      
                        else:
                            print("*************Moving Towards Our Special Suggestion for you in rice*********")
                            madbi_plat=6000 #for Regularly chicken biryaani lover #16500
                            dumpukht=2500 #15000
                            icecream_falooda=1200 #11250
                            gulabj=100 #3000
                            almond_milk=600 #9000 
                            fire_meetha_pan=150 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            platter=person2//3.5
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(madbi_plat*platter)+(dumpukht*quantity)+(icecream_falooda*person2)+(gulabj*gulabj_per)+(almond_milk*person2)+(fire_meetha_pan*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            #print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {platter} Fresh Afghaani Special Platter \n2. Fresh Live {quantity} KG Dumpukht  \n3. {person2} Bowl Ice Cream Falooda \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Glass Almond Milk \n6. {person2} Special Fire Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {platter} Fresh Afghaani Special Platter Rs.{madbi_plat*platter}/-  \n***********\n2. Fresh Live {quantity} KG Dumpukht Rs.{dumpukht*quantity}/- \n***********\n3. {person2} Bowl Ice Cream Falooda Rs.{person2*icecream_falooda}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Glass Almond Milk Rs.{almond_milk*person2}/- \n***********\n6. {person2} Special Fire Meetha Paan Rs {fire_meetha_pan*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                    elif variant==2:
                        typ=int(input("Do you want to eat \n1. Moroccan Lamb Rice \n2. Classic Dumpukht mutton biryaani \n3. Mutton Kabbuli Pulao \n4.Type anything something Special in Rice \nSelect any specific from above: "))
                        print("\n*====================================*")
                        if typ==1:
                            print("*************Moving for Moroccan Lamb Rice Lover*********")
                            lamb_rice=3000 #for Regularly lamb rice lover #16500
                            saalam_lamb=3000 #15000
                            kunaffa=1500 #11250
                            gulabj=100 #3000
                            special_dr=600 #9000 
                            meetha_p=100 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            platter_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(lamb_rice*platter_kg)+(saalam_lamb*quantity)+(kunaffa*quantity)+(gulabj*gulabj_per)+(special_dr*person2)+(meetha_p*person2) #calculation for bill
                            tax=bill/10

                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {platter_kg}KG Fresh Live Morrocon Lamb rice \n2. Fresh Live {platter_kg} Lamb \n3. {quantity}Kunafah \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Special Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {platter_kg} KG Fresh Live Morrocon Lamb rice Rs.{lamb_rice*platter_kg}/-  \n***********\n2. Fresh Live {Platter_kg} Saalam Lamb Rs.{saalam_lamb*platter_kg}/- \n***********\n3. {quantity}Kunafah Rs.{kunaffa*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Special Drink Rs {special_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
         
                        elif typ==2:
                            print("*************Moving for Classic Dumpukht Mutton Biryaani Lover*********")
                            mutton_bir=4500 #for Regularly chicken biryaani lover #16500
                            mutton_rosh=3500 #15000
                            kunaffa=1500 #11250
                            gulabj=100 #3000
                            limca_dr=600 #9000 
                            meetha_p=100 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            mutton_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(mutton_bir*mutton_kg)+(mutton_rosh*mutton_kg)+(kunaffa*quantity)+(gulabj*gulabj_per)+(limca_dr*person2)+(meetha_p*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {mutton_kg}KG Fresh Live Classic Dumpukht Mutton Biryaani \n2. Fresh Live {mutton_kg} Mutton Rosh \n3. {quantity}Kunafah \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Limca Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {mutton_kg} KG Fresh Live Classic Dumpukht Mutton Biryaani Rs.{mutton_bir*mutton_kg}/-  \n***********\n2. Fresh Live {mutton_kg} kg Mutton Rosh Rs.{mutton_rosh*mutton_kg}/- \n***********\n3. {quantity}Kunafah Rs.{kunaffa*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Limca Drink Rs {limca_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                     
                        elif typ==3:
                            print("*************Moving for Mutton Kabbuli Pulao Lover*********")
                            kabuli_pulao=3000 #for Regularly chicken biryaani lover #16500
                            mutton_peti_kabab=2000 #15000
                            rabri=1500 #11250
                            gulabj=100 #3000
                            limca_dr=600 #9000 
                            meetha_p=100 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            kabuli_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(kabuli_pulao*kabuli_kg)+(mutton_peti_kabab*quantity)+(rabri*person2)+(gulabj*gulabj_per)+(limca_dr*person2)+(meetha_p*person2)
                            tax=bill/10
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {kabuli_kg}KG Fresh Live Chicken Hyderabaadi Biryaani \n2. Fresh Live {person2} Petti Kabaab  \n3. {quantity}kg Rabri \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Limca Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {kabuli_kg} KG Fresh Live Chicken Hyderabaadi Biryaani Rs.{kabuli_pulao*kabuli_kg}/-  \n***********\n2. Fresh Live {person2} Petti Kabaab Rs.{mutton_peti_kabab*person2}/- \n***********\n3. {quantity} Rabri Rs.{rabri*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Limca Drink Rs {limca_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")

                        else:
                            print("*************Moving Towards Our Special Suggestion for you in rice*********")
                            b_plat=6000 #for Regularly badshahi platter lover #16500
                            salim_dumba=4500 #15000
                            icecream_falooda=1200 #11250
                            gulabj=100 #3000
                            almond_milk=600 #9000 
                            fire_meetha_pan=150 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            platter=person2//3.5
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(b_plat*platter)+(salim_dumba*quantity)+(icecream_falooda*person2)+(gulabj*gulabj_per)+(almond_milk*person2)+(fire_meetha_pan*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            #print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {platter} Fresh Afghaani Special Platter \n2. Fresh Live {quantity} Salim Dumba \n3. {person2} Bowl Ice Cream Falooda \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Glass Almond Milk \n6. {person2} Special Fire Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {platter} Fresh Baadshahi Platter Rs.{b_plat*platter}/-  \n***********\n2. Fresh Live {quantity} KG Salim Dumba Rs.{salim_dumba*quantity}/- \n***********\n3. {person2} Bowl Ice Cream Falooda Rs.{person2*icecream_falooda}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Glass Almond Milk Rs.{almond_milk*person2}/- \n***********\n6. {person2} Special Fire Meetha Paan Rs {fire_meetha_pan*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
#                     elif variant==3:
#                         print("")
                    else:
                        #print("")
                        typ=int(input("Do you want to eat \n1. Classic Beef Special Daigh Biryaani \n2.Type anything something Special in Rice with beef \nSelect any specific from above: "))
                        print("\n*====================================*")
                        if typ==1:
                            print("*************Moving for Classic Beef Special Daigh Biryaani Lover*********")
                            classic_daig=1947 #for Regularly lamb rice lover #16500
                            bihaari_kabaab=1408 #15000
                            kunaffa=1499 #11250
                            gulabj=78 #3000
                            special_dr=547 #9000 
                            meetha_p=73 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            daigh_kg=person2//3
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(classic_daig*daigh_kg)+(bihaari_kabaab*person2*2)+(kunaffa*quantity)+(gulabj*gulabj_per)+(special_dr*person2)+(meetha_p*person2) #calculation for bill
                            tax=bill//14
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {daigh_kg}KG Fresh Live Classic Beef Special Daigh Biryaani rice \n2. Fresh Live {person2*2} Bihaari Kabaab \n3. {quantity}Kunafah \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Special Drink \n6. {person2} Special Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {daigh_kg} KG Fresh Live Classic Beef Special Daigh Biryaani rice Rs.{classic_daig*daigh_kg}/-  \n***********\n2. Fresh Live {person2*2} Bihaari Kabaab Rs.{bihaari_kabaab*(person2*2)}/- \n***********\n3. {quantity}Kunafah Rs.{kunaffa*quantity}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Special Drink Rs {special_dr*person2}/- \n***********\n6. {person2} Special Meetha Paan Rs {meetha_p*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
         
                    
                        else:
                            print("*************Moving Towards Our Special Suggestion for you in rice with beef*********")
                            beef_hyder_daigh=4359 #for Regularly badshahi platter lover #16500
                            beef_balochi_tikka=2569 #15000
                            icecream_falooda=1200 #11250
                            gulabj=100 #3000
                            almond_milk=600 #9000 
                            fire_meetha_pan=150 #1500 
                            gulabj_per=person2*2 #for the purspose to calculate 2 gulab jamun per person
                            beef_daigh=person2//3.5
                            quantity=person2//2 #used for sajji and kunaffah
                            bill=(beef_hyder_daigh*beef_daigh)+(beef_balochi_tikka*quantity)+(icecream_falooda*person2)+(gulabj*gulabj_per)+(almond_milk*person2)+(fire_meetha_pan*person2) #calculation for bill
                            tax=bill/10
                            print("\n*====================================*")
                            #print("\n*====================================*")
                            print(f"Dear Customer! \nYour Order is here confirmed and here \n1. {beef_daigh} KG Live Fresh Special Beef Hyderabaadi Daighi Biryaani \n2. Fresh Live {quantity} Beef Balochi Tikka \n3. {person2} Bowl Ice Cream Falooda \n4.{gulabj_per} Gulaab Jamun \n5.{person2} Glass Almond Milk \n6. {person2} Special Fire Meetha Paan")
                            print("\n*====================================*")
                            print(f"Dear Customer! \nYour Total Bill is: \n***********\n1. {beef_daigh} KG Live Fresh Special Beef Hyderabaadi Daighi Biryaani Rs.{beef_hyder_daigh*beef_daigh}/-  \n***********\n2. Fresh Live {quantity} Beef Balochi Tikka Rs.{beef_balochi_tikka*quantity}/- \n***********\n3. {person2} Bowl Ice Cream Falooda Rs.{person2*icecream_falooda}/- \n***********\n4.{gulabj_per} Gulaab Jamun Rs {gulabj*gulabj_per}/- \n***********\n5.{person2} Glass Almond Milk Rs.{almond_milk*person2}/- \n***********\n6. {person2} Special Fire Meetha Paan Rs {fire_meetha_pan*person2}/- \n***********\nTotal Bill: Rs{bill} + Tax Rs.{tax}/- \n***********\nGrand Total: Rs.{bill+tax}/- ")
                    
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