
def groceryfunc(var):
    if var=="pulses":
        rate=500
    elif var=="spices":
        rate=150
    elif var=="dairy":
        rate=300
    elif var=="rice":
        rate=4000
    elif var=="wheat":
        rate=3000
    else:
        print("invalid value, please check your outer program!")
        rate=0
    return rate


def electronicfunc(var):
    if var=="computer":
        rate=20000
    elif var=="mobile_phone":
        rate=50000
    elif var=="led":
        rate=60000
    elif var=="graphic_card":
        rate=50000
    elif var=="charger":
        rate=1200
    else:
        print("invalid value, please check your outer program!")
        rate=0
    return rate

def fandvfunc(var):
    if var=="mango":
        rate=200
    elif var=="potato":
        rate=100
    elif var=="apple":
        rate=180
    elif var=="spinach":
        rate=250
    elif var=="tomato":
        rate=150
    elif var=="green_chilli":
        rate=100
    elif var=="grapes":
        rate=400
    elif var=="onion":
        rate=120
    else:
        print("invalid value, please check your outer program!")
        rate=0
    return rate



grocery=[]
electronic=[]
cart=[]
fandv=[]
total=[]

print("Welcome to ecomerce store!")

while True:
    select=input("Which category you want to buy? \n1.grocery \n2.electronic \n3.fruit and veg:")
    if select=="1":
        while True:
            bucket=["pulses","spices","dairy","rice","wheat"]
            for i in bucket:
                print(i)
            var=input("Please mention what your want to buy from above list?").lower()
            rates=groceryfunc(var)
            total.append(rates)
            if var in bucket:
                grocery.append(var)
                print(f"bought item {var}, Rs.{rates}, Your Total Items are {grocery} and total amount is {sum(total)}")
               
               
                rerun=input("Do you want to add more from grocery? (yes or no):").lower()
                if rerun=="yes":
                    continue
                else:
                    print("Ok Thank you for shopping grocery!")
                    break
            else:
                print("item not found in the bucket, Please select from below")
    elif select=="2":
        print("Welcome to electronics")
        while True:
           
            bucket=["computer","mobile_phone","led","graphic_card","charger"]
            for i in bucket:
                print(i)
            var=input("Please mention what your want to buy from above list? \nNote:Type Exactly what it is! \n").lower()
            rates=electronicfunc(var)
            total.append(rates)
            if var in bucket:
                electronic.append(var)
                print(f"bought item {var}, Rs.{rates}, Your Total Items are {electronic} and total amount is {sum(total)}")
                rerun=input("Do you want to add more from Electronic section? (yes or no):").lower()
                if rerun=="yes":
                    continue
                else:
                    print("Ok Thank you for shopping Electronics!")
                    break
            else:
                print("item not found in the bucket, Please add from below!")
                continue
    elif select=="3":
        print("Welcome to Fruits and vegetable")
        while True:
           
            bucket=["mango","potato","apple","spinach","tomato","green_chilli","grapes","onion"]
            for i in bucket:
                print(i)
            var=input("Please mention what your want to buy from above list? \nNote:Type Exactly what it is! \n").lower()
            rates=fandvfunc(var)
            total.append(rates)
            if var in bucket:
                fandv.append(var)
                print(f"bought item {var}, Rs.{rates}, Your Total Items are {fandv} and total amount is {sum(total)}")
                rerun=input("Do you want to add more from Fruit and Veg section? (yes or no):").lower()
                if rerun=="yes":
                    continue
                else:
                    print("Ok Thank you for shopping Fruits and Veg!")
                    break
            else:
                print("item not found in the bucket, Please add from below!")
                continue
    else:
        print("invalid input!")
        rerun=input("Do you want try again? (yes or no):").lower()
        if rerun=="yes":
            continue
        else:
            print("Thank you! Bye!")
            break
    rerun=input("Do you want to add more from store? (yes or no):").lower()
    if rerun=="yes":
        continue
    else:
        print("Thank you for Shopping!")
        break
       
   #break