#Decisions in python!

#-- #If else elif

print("Car Recommendation system")

name=input("Enter your name:")
budget=int(input("Enter your budget:"))
cc=int(input("Enter engine capacity:"))
gear=input("Enter (Auto/Manual):").lower()
sunroof=input("Sunroof Available or not (yes/no):").lower()
seats=int(input("Enter Seating Capacity:"))
cartype=int(input("Enter Car Type: Press accordingly\n1. for suv \n2. For Sedan \nEnter preference:"))


if (budget >= 1000000 and budget<=1500000) and cc<=1000 and gear == "manual" and sunroof=="no" and seats <=5 and cartype==2:
    print(f"Dear {name}, Your Recommendations are \n1.Suzuki Alto \n2. Daihatsu \n3. Suzuki Mehran")
   
elif (budget >15000000 and budget<=3000000) and cc<=1300 and gear == "manual" and sunroof=="no" and seats <=5 and cartype==2:
    print(f"Dear {name}, Your Recommendations are \n1.Honda city(mouse) \n2. Toyota corrolla(saloon) \n3. Suzuki Liana")
   
elif (budget> 3000000 and budget<=4500000) and cc<=2000 and gear == "auto" and sunroof=="yes" and seats <=5 and cartype==2:
    print(f"Dear {name}, Your Recommendations are \n1.Honda Civic \n2. MG 5 \n3. Kia stonic")

elif (budget>=500000 and budget<1000000) and cc<=800 and gear == "manual" and sunroof=="no" and seats <=4 and cartype==2:
    print(f"Dear {name}, Your Recommendations are \n1.Charade \n2. FX \n3. coure ")
elif (budget<500000) and cc<600 and gear == "manual" and sunroof=="no" and seats <=4 and cartype==2:
    print(f"Dear {name}, Please increase your budget")        

else:
    print(f"Dear {name}, urf Baray log! Recommended Cars for you: \n1. Land cruiser \n2. Prado \n3.Lexus LX 570 \n4. Fortuner \n5. Pajero")