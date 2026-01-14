name = input("Enter your Name: ")
email = input("Enter your Email: ").lower()
password = input("Enter your Password: ")
age = int(input("Enter your Age: "))

if age>= 18:
    print(f"Dear {name}, Welcome to Netflix")
    if email == "kulsoomhameed47@gmail.com" and password == "Admin123":
       print(f"Dear {name}, Welcome to Netflix Sessions, Please Select Category")
    elif email == "safiamaham@gmail.com" and password == "safia123":
       print(f"Dear {name}, Welcome to Netflix Sessions, Please Select Category")
    elif email == "warisha@gmail.com" and password == "warisha123":
       print(f"Dear {name}, Welcome to Netflix Sessions, Please Select Category")
    else:
        print(f"Dear {name}, YOur Login Credential in Invalid")
else:
    print(f"Dear {name}, You are not Eligible:")