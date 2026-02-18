owner = "Masooma"

print(f"--- {owner} Loan Portal ---")

age = int(input("Enter your age: "))
income = float(input("Monthly income in Rs: "))
job = input("Are you employed? (yes/no): ")
months = int(input("Months at current job: "))
loan = float(input("Desired loan amount in Rs: "))

status = "Pending"
rate = 0.0
cosigner = "Not Required"
error = ""

if age < 18:
    status = "Rejected"
    error = "Underage"
elif age > 70:
    status = "Rejected"
    error = "Overage"
elif job == "no":
    status = "Rejected"
    error = "Unemployed"
elif months < 6:
    status = "Rejected"
    error = "Job history too short"
else:
    if income < (loan * 0.2):
        status = "Rejected"
        error = "Income is too low compared to loan"
    else:
        status = "Approved"

if status == "Approved":
    if income >= 100000:
        rate = 0.05
    elif income >= 50000:
        rate = 0.10
    else:
        rate = 0.15
        cosigner = "Required"

print("\n--- Final Decision ---")
if status == "Approved":
    print(f"Result: {status}")
    
    interest = loan * rate
    final = loan + interest
    
    print(f"Interest Rate: {rate * 100}%")
    print(f"Co-signer: {cosigner}")
    print(f"Loan Amount: Rs {loan:.2f}")
    print(f"Total Interest: Rs {interest:.2f}")
    print(f"Total to Pay: Rs {final:.2f}")
else:
    print(f"Result: {status}")
    print(f"Reason: {error}")
print("-----------------------")