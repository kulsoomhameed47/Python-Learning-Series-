print("**** Eectricity bill ****")
consumed_Unit = int(input("Enter Consumed Unit: "))
customer_type = input("Enter Your Consumer (domestic/commercial): ").lower()
if consumed_Unit <= 100:
    if customer_type == "domestic":
        bill = consumed_Unit * 10
        print(f"You bill is {bill} as you are {customer_type} customer \nyour Consumed unit is {consumed_Unit}")
    else:
        bill = consumed_Unit * 15
        print(f"You bill is {bill} as you are {customer_type} customer \nyour Consumed unit is {consumed_Unit}")
elif consumed_Unit <= 200:
    if customer_type == "domestic":
        bill = consumed_Unit * 15
        print(f"You bill is {bill} as you are {customer_type} customer \nyour Consumed unit is {consumed_Unit}")
    else:
        bill = consumed_Unit * 20
        print(f"You bill is {bill} as you are {customer_type} customer \nyour Consumed unit is {consumed_Unit}")
elif consumed_Unit < 300:
    if customer_type == "domestic":
        bill = consumed_Unit * 20
        print(f"You bill is {bill} as you are {customer_type} customer \nyour Consumed unit is {consumed_Unit}")
    else:
        bill = consumed_Unit * 25
        print(f"You bill is {bill} as you are {customer_type} customer \nyour Consumed unit is {consumed_Unit}")
else:
    if customer_type == "domestic":
        bill = consumed_Unit * 30
        print(f"You bill is {bill} as you are {customer_type} Customer \nyour Consumed unit is {consumed_Unit}")
    else:
        bill = consumed_Unit * 35
        print(f"You bill is {bill} as you are {customer_type} customer \nyour Consumed unit is {consumed_Unit}")
    
        

