print("**** Eligibility for Exam ****")
print("**** It is mandatory to conduct 27 classes. Only 3 leave is allowed with valid Medical Certificate: ****")
total_class = int(input("Enter Total Number of class: "))
attended_class = int(input("Enter Total Number of class you Attended: "))
absent = total_class - attended_class
medical_certificate = input("Have you submitted Medical Certificate (yes/no): ")

if total_class == 30:
   if absent <= 3 and medical_certificate == "no":
       print("You can give exam:")
   elif absent <= 3 and medical_certificate == "yes":
       print("You can give exam:")
   elif absent <= 3 and medical_certificate == "no":
       print("You are not allowed to Sit because you have not submmitted Medical Certificate: ")
   elif absent > 3 and medical_certificate == "yes":
       print(f"You are not allowed to Sit because you have taken {absent} days off")
   else:
       print(f"You are not allowed to Sit because you have taken {absent} days off")
    
else:
       print("You are not allowed to Sit")