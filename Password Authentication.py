print("***PASSWORD AUTHENTICATION***")
user_name = input("Enter User Name: ").lower()
password= input("Enter Password: ")

if ( user_name == "kulsoom" or user_name == "kulsoomhameed47@gmail.com" or user_name == "03407834231") and (password == "password123"):
 print(f"Dear {user_name}, Welcome to the portal")
elif ( user_name == "safia" or user_name == "syedahmaham@gmail.com" or user_name == "03362327095") and (password == "password123"):
 print(f"Dear {user_name}, Welcome to the portal")
elif ( user_name == "warisha" or user_name == "warisha@gmail.com" or user_name == "03456734231") and (password == "password123"):
 print(f"Dear {user_name}, Welcome to the portal")
else:
    print(f"Dear {user_name}, Invalid user name or password")