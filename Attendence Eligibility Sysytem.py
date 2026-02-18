name=input("Enter Your Name:")
total_class=int(input("Enter A Number Of Total Classes:"))
attended_classes=int(input("Enter A Number Of Attendence / Classes Attended (Mention in Numbers):"))
percentage =(attended_classes/total_class)*100

if percentage >= 75:
    print(f"Dear {name}, You Are Allowed To Sit In Exam . No Medical Certificate Required.")
elif percentage>=20 and percentage<75:
    print(f"Dear {name}, Your Percentage Is Below 75%.")
    medical_certificate=int(input("Do You Have Medical Certificate? : \nPress 1.For Yes \nPress 2. For No:"))
    if medical_certificate == 1:
        print("Your Medical Certificate Is Proceed To Varification.")
        varification=int(input("Let Me Know Is It Signed And Stampped? : \nPress 1.For Yes \nPress 2. For No:"))
        if varification==1:
            print(f"Dear {name}, Despite Your Attendance Is Low , But Your Medical Certificate Is Verified And You Are Allowed To Sit In Exam.")
        elif varification==2:
            print(f"Dear {name}, Your Attendance Is Low , And Your Medical Certificate Is Not Verified And You Are Not Allowed To Sit In Exam.")
        else:
            print("Invalid Input.")
    else:
        print("You Are Not Allowed To Sit In Exam.")
else:
    print("Attendance Percentage Is Very Low ! You Are Not Allowed To Sit In Exam.")