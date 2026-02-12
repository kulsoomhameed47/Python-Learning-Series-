print("****** Event Manager ************")
event=1
while event <2:
	check = input("Do you want Barat and Valima Event with us? (yes/no): \n").lower()
	if event == 1 and check == "yes":
		venue = input("Select Indoor / Outdoor\n").lower()
		if venue == "indoor":
			print("You Can Booked Our Villas.")
		else:
			print("You Can Booked Our Bali Resorts")
	
	else:
			print("You don't want anything with us: \nThank You for visiting")
			

	if check == "yes":
		cater = input("Do You Want Catering? (yes/no): \n")
		if cater == "yes":
			foods = ["Biryan", "Rabri Kheer", "Shahi Karahi", "Coldrink"]
			for food in foods:
				print(f"we will serve {food}")
		else:
			event +=1
			print("You don't want Cateringy with us.")
	else:
		event+=1
	break