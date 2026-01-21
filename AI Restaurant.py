print("***Welcome to AI Restaurant")
name = input("Enter your Name: ")
cusine = int(input(f"Dear {name}, \n Select Anyone From Below! \n1. Pakistani \n2. Chinese \n3.Italian \n4. Korean \n5.Thai \n6. Don't know, Suggest something special: "))
             
if cusine == 1 :
    print("Welcome to Pakistani Cuisine")
    budget = eval(input("Enter Your Budget: "))
    if budget >= 10000:
        fav = int(input(f"Dear {name}, \nWhat do you like most in normal days? \n1. Biryani \n2. Karahi \n3. Creamy Handi \n4. BBQ \n5. All of the above: "))
        if fav == 1 :
             bill=8500
             r_amount = budget-bill
             print(f"Dear {name}, \nHave your special Mandi platter with Shamas Special Dumpukht! Along with jumbo Drink + 4 Yakhni Bowls + Raita + Special Salad. \n Your Total Bill is Rs:8500/- (Including Tax)")
             meetha = int(input((f"Dear {name}, Do you want sweet? As the remaining Amount is {r_amount} \n1. Kunafa \n2. Chocolate  Tart \n3. Suggest Something"))
             if meetha == 1 :
                          bill2 = 500
                          print(f"Here is Your Sweet (Kunafah) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount- bill2}")
             elif meetha == 2 :
                          bill2 = 1000
                          print(f"Here is Your Sweet (Chocolate Tart) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
             elif meetha == 3 :
                          bill2 = 850:
                          print(f"Here is the recommended Sweet (Kunafah Chocolate) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
             else:
                print(f"Your Total Bill is {bill} and Remaining amount is {r_amount}")
            
        elif fav ==2:
             bill=9000
             r_amount = budget-bill
             print(f"Dear {name}, \nHave your Shinwari Karahi with Shamas Special Brain Masala! Along with jumbo Drink + 4 Yakhni Bowls + Raita + Special Salad. \n Your Total Bill is Rs:8500/- (Including Tax)")
             meetha = int(input((f"Dear {name}, Do you want sweet? As the remaining Amount is {r_amount} \n1. Lava chocolate with premim Ice Cream \n2. Brownie \n3. Suggest Something"))
             if meetha == 1:
                          bill2 = 1200:
                          print(f"Here is Your Sweet (Lava chocolate with premim Ice Cream) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount- bill2}")
             elif meetha == 2:
                          bill2 = 1500:
                          print(f"Here is Your Sweet (Brownie) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
             elif meetha == 3:
                          bill2 = 2000:
                          print(f"Here is the recommended Sweet (Chocolate Dream Cake) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
             else:
                print(f"Your Total Bill is {bill} and Remaining amount is {r_amount}")
        elif fav ==3 :
             bill=11000
             r_amount = budget-bill
             print(f"Dear {name}, \nHave your special Mandi platter with Shamas Special Dumpukht! Along with jumbo Drink + 4 Yakhni Bowls + Raita + Special Salad. \n Your Total Bill is Rs:8500/- (Including Tax)")
             meetha = int(input((f"Dear {name}, Do you want sweet? As the remaining Amount is {r_amount} \n1. Kunafa \n2. Chocolate  Tart \n3. Suggest Something"))
             if meetha == 1:
                          bill2 = 1200:
                          print(f"Here is Your Sweet (Lava chocolate with premim Ice Cream) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount- bill2}")
             elif meetha == 2:
                          bill2 = 1500:
                          print(f"Here is Your Sweet (Brownie) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
             elif meetha == 3:
                          bill2 = 2000:
                          print(f"Here is the recommended Sweet (Chocolate Dream Cake) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
             else:
                print(f"Your Total Bill is {bill} and Remaining amount is {r_amount}")
        elif fav ==5:
             bill=9500
             r_amount = budget-bill
             print(f"Dear {name}, \nHave your Special Creamy Handi with Shamas Special Dumpukht! Along with jumbo Drink + 4 Yakhni Bowls + Raita + Special Salad. \n Your Total Bill is Rs:8500/- (Including Tax)")
             meetha = int(input((f"Dear {name}, Do you want sweet? As the remaining Amount is {r_amount} \n1. Ice Cake \n2. Three Milk Cake \n3. Suggest Something"))
             if meetha == 1:
                          bill2 = 1500:
                          print(f"Here is Your Sweet (Ice Cake) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount- bill2}")
             elif meetha == 2:
                          bill2 = 2000:
                          print(f"Here is Your Sweet (Three Milk Cake) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
             elif meetha == 3:
                          bill2 = 3000:
                          print(f"Here is the recommended Sweet (Cheese Cake) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
             else:
                print(f"Your Total Bill is {bill} and Remaining amount is {r_amount}")
        elif fav == 4:
             bill=9500
             r_amount = budget-bill
             print(f"Dear {name}, \nHave your Special BBQ Family platter with Mutton Champ! Along with jumbo Drink + 4 Yakhni Bowls + Raita + Special Salad. \n Your Total Bill is Rs:8500/- (Including Tax)")
             meetha = int(input((f"Dear {name}, Do you want sweet? As the remaining Amount is {r_amount} \n1. Rabri Kheer \n2. Meethay Dahi Bhallay \n3. Suggest Something"))
             if meetha == 1:
                          bill2 = 1000:
                          print(f"Here is Your Sweet (Rabri Kheer) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount- bill2}")
             elif meetha == 2:
                          bill2 = 700:
                          print(f"Here is Your Sweet (Meethay Dahi Bhallay) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
             elif meetha == 3:
                          bill2 = 1500:
                          print(f"Here is the recommended Sweet (Gulaab Jamun with rasmalai fusioned with Ice Cream) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
             else:
                print(f"Your Total Bill is {bill} and Remaining amount is {r_amount}")
        elif fav == 5:
             bill=20000
             r_amount = budget-bill
             print(f"Dear {name}, \nHave your Special Family platter with Mutton Dumpukht and BBQ Platter! Along with jumbo Drink + 4 Yakhni Bowls + Raita + Special Salad. \n Your Total Bill is Rs:8500/- (Including Tax)")
             meetha = int(input((f"Dear {name}, Do you want sweet? As the remaining Amount is {r_amount} \n1. platter of Jalebi with Gulab Jamun \n2. Meethay Dahi Bhallay \n3. Suggest Something"))
             if meetha == 1:
                          bill2 = 1000:
                          print(f"Here is Your Sweet (Rabri Kheer) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount- bill2}")
             elif meetha == 2:
                          bill2 = 700:
                          print(f"Here is Your Sweet (Meethay Dahi Bhallay) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
             elif meetha == 3:
                          bill2 = 1500:
                          print(f"Here is the recommended Sweet (Gulaab Jamun with Rasmalai fusioned with Ice Cream) \nYour Total Bill is {bill2+bill} \nHere is your Remaining Amount {r_amount}")
             else:
                print(f"Your Total Bill is {bill} and Remaining amount is {r_amount}")
        else:
                    print("")
    elif budget == 2:
    else
else:  