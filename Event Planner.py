# welcome to event planner
print("***Welcome To Event Planner***")
name=input("Enter Your Name:")
mood=input("Enter Your Mood (Happy/Sad/Tired)?").lower()
budget=int(input("Enter Your Budget ($):"))
weather=input("Weather Today? (Sunny/Rainy/Cold):").lower()
company=input("Who Are You With? (Alone/Friends/Family):").lower()
print("\n Planning Weekend...\n")

if mood == "happy" :
    if budget > 1000 :
       if weather == "sunny" :
           if company == "friends" :
               print(f"Dear {name} , 😎 go for an outdoor movie + street food party :")
           else:
                print("Watch Block buster Movie !")
       else:
          print("Order Pizza + Netflix Movie")
    else :
        print("Watch Comedy movie on mobile with snacks !!!")
elif mood == "sad" :
    if company == "alone" :
        print("Watch Motivational Movie and order comfort food !")
    else :
        if budget > 500 :
            print("Ice- Cream + Feel - good movie with loved ones !")
        else :
            print("Team + old classic Movie !")
elif mood == "tired" :
    if weather == "cold" :
        print("Sleep Early + Light Music !")
    else :
        if budget > 300 :
            print("Fast Food + And Watch Comedy Show")
        else : 
            print("Relax With Music Or Book")
else:
    print("Mood Not Recognized , Just Relax and Enjoy")