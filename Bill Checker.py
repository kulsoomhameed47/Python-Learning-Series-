name = input("Enter Your Name: ")
customer_type = int(input("Which Customer are you? \nPress 1. For Commercial \nPress 2. For Domestic: \n"))

if customer_type ==1: #commercial
    print(f"Customer Type: Commercial \nInvoice Name: {name}")
    units = int(input("Number of units you consumed?:"))
    if units >=450 and units <800:
        print(f"Dear {name} \nAs per your {units} \nYou will be charged as RS100/Unit for Commercial \nYour Bill of Electicity for Current Month is \nRs{units*100}")
    elif units >=300 and units <450:
        print(f"Dear {name} \nAs per your {units} \nYou will be charged as RS85/Unit for Commercial \nYour Bill of Electicity for Current Month is \nRs{units*85}")
    elif units >=150 and units <450:
        print(f"Dear {name} \nAs per your {units} \nYou will be charged as RS65/Unit for Commercial \nYour Bill of Electicity for Current Month is \nRs{units*65}")
    else:
        print(f"Dear {name} \nAs per your {units} \nYou will be charged as RS150/Unit for Commercial \nYour Bill of Electicity for Current Month is \nRs{units*150}")

