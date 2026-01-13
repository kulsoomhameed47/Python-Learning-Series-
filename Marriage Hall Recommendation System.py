print("\tMarriage Hall Recommendation system")
name=input("Please Enter Your Name: ")
print(f"Dear {name}, Please Enter Your Requirements: ")
budget = int(input("Please specify your Budget:  "))
guests = int(input("Number of Guest: "))
ac = input("Do you need Cooling System: ").lower()
parking = input("Do you need parking: ").lower()
hall_type = input("Do you need Indoor or Outdoor: ").lower()

if budget <= 500000 and guests <= 300 and ac == "no" and parking == "no" and hall_type == "outdoor":
 print(f"Dear {name} as per your requirements you can visit \n1. Local Marriage Lawn \n2. Community Center Hall \n3. Simple Banquet Lawn")

elif budget <= 1200000 and guests <= 500 and ac == "yes" and parking == "yes" and hall_type == "indoor":
 print(f"Dear {name} as per your requirements you can visit \n1. Royal Banquet  \n2. Pearl Wedding Hall \n3. Elegant Marquee")
 
elif budget <= 1200000 and guests <= 800 and ac == "yes" and parking == "yes" and hall_type == "indoor":
 print(f"Dear {name} as per your requirements you can visit 1. Dream Banquet  \n2. Grand Palace Hall \n3. Luxury Marquee")

else:
 print(f"Dear {name} as per your requirements you can visit \n1. Expo Center Banquet \n2. 5 Star Hotel Ballroom \n3. Premium Event Complex")