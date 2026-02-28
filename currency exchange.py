def usd(pkr):
    pk= pkr*280
    return pk
def euro(pkr):
    pk= pkr*330
    return pk
def riyal(pkr):
    pk= pkr*74
    return pk
def ringgit(pkr):
    pk= pkr*71
    return pk
def pound(pkr):
    pk= pkr*378
    return pk
def dirham(pkr):
    pk= pkr*76
    return pk
print("="*50,"CurrencyExchange","="*50)
while True:
    cur = eval(input("Enter the amount of Currency you have:"))
    select=int(input("Which currency do you want to exchage with pakistani rupee: \n1. USD \n2. Euro \n3. Riyal \n4. Ringgit \n5. Pound \n6. Dirham"))
    if select == 1:
        print(f"Here is your converted amount in $ USD {usd(cur)}")
        
    elif select == 2:
        print(f"Here is your converted amount in € Euro {euro(cur)}")
    elif select == 3:
        print(f"Here is your converted amount in ﷼ Riyal {riyal(cur)}")
    elif select == 4:
        print(f"Here is your converted amount in RM Ringgit {ringgit(cur)}")
    elif select == 5:
        print(f"Here is your converted amount in £ Pound{pound (cur)}")
    elif select == 6:
        print(f"Here is your converted amount in AED Dirham {dirham(cur)}")
    else:
        choose = input("Do you want to continue: yes/no")
        if choose == "yes":
            continue
        else:
            break
    
