name = input("Enter your Name:")
roll = int(input("Enter your roll number:"))
english = int(input("Subject English :"))
math = int(input("Subject Math :"))
comp = int(input("Subject Comp: "))
isl = int(input("Subject Islamiyat: "))
urdu = int(input("Subject Urdu:"))

obtain = english + math + comp + isl + urdu
print(f"Your obtain marks is: {obtain} ")
total = 500
percentage = (obtain/total)*100

if percentage >=80:
   print(f"Dear student {name}, your percentage is {percentage}%, \n congrats you get A+ Grade:")
elif percentage >=70:
   print(f"Dear student {name}, your percentage is {percentage}%, \n congrats you get B Grade:")

elif percentage >=60:
   print(f"Dear student {name}, your percentage is {percentage}%, \n congrats you get C Grade:")
   
elif percentage >=50:
   print(f"Dear student {name}, your percentage is {percentage}%, \n congrats you get D Grade:")
   
elif percentage >=40:
   print(f"Dear student {name}, your percentage is {percentage}%, \ congrats you get E Grade:")
   
else:
    print(f"Dear student{name}, we are sorry you fail")