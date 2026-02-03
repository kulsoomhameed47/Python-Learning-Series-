import random
print("******Sport Tournament System******\n")

team_id = int(input("Enter your Team ID: \n1.khi-101 \n2.lhr-102 \n3.mul-103 \n4.que-104:\n"))
    
if team_id == 1:
    print("Team Name is: \nkhi-101 Karachi Kings:")
elif team_id == 2:
    print("Team Name is: \nlhr-102 Lahore Qalandars:")
elif team_id == 3:
    print("Team Name is: \nmul-103 Multan Sultan:")
elif team_id == 4:
    print("Team Name is: \nque-104 Quetta Gladiators:")
else:
    print("Team Not Recognized, You Can Check Other Team")
print("\n\nEnter Tournament Details:\n")

tournament_id = int(input("Enter Tournament ID (101 102 103 104): \n"))

if tournament_id == 101 or tournament_id == 102 or tournament_id == 103 or tournament_id == 104:
    
    tournament_name = input("Enter Tournament Name: (League/Knockout):\n ").lower
    
    if tournament_id == 101 or tournament_id == 102:
        print(f"Tournament {tournament_name} is in between Karachi Kings vs Lahore Qalandar")
    
        # Generate a random score between 70 to 200 (inclusive)
        score_khi = random.randint(70, 200)
        print(f"Karachi King score is {score_khi}")
        
        score_lhr = random.randint(50, 200)
        print(f"Lahore Qalandar score is {score_lhr}")
        
        if score_khi > score_lhr:
            win_score = (score_khi-score_lhr)
            print(f"Karachi King Win with score is {win_score}")
        elif score_lhr > score_khi:
            win_score = (score_lhr-score_khi)
            print(f"Lahore Qalandars Win with score is {win_score}")
        else:
            print(f"Match Tie {score_khi}")
    
    elif tournament_id == 101 or tournament_id == 103:
        print(f"Tournament {tournament_name} is in between Karachi Kings VS Multan Sultan: ")
        
        # Generate a random score between 70 to 200 (inclusive)
        score_khi = random.randint(70, 200)
        print(f"Karachi King score is {score_khi}")
        
        score_mul = random.randint(50, 200)
        print(f"Multan Sultan score is {score_mul}")
        
        if score_khi > score_mul:
            win_score = (score_khi-score_mul)
            print(f"Karachi King Win with score is {win_score}")
        
        elif score_mul > score_khi:
            win_score = (score_mul-score_khi)
            print(f"Lahore Qalandars Win with score is {win_score}")
        
        else:
            print(f"Match Tie {score_khi}")
    
    elif tournament_id == 101 or tournament_id == 104:
        print(f"Tournament {tournament_name} is in between Karachi Kings VS Quetta Gladiators: ")
        
        # Generate a random score between 70 to 200 (inclusive)
        score_khi = random.randint(70, 200)
        print(f"Karachi King score is {score_khi}")
        
        score_qld = random.randint(50, 200)
        print(f"Quetta Gladiators score is {score_qld}")
         
        if score_khi > score_qld:
            win_score = (score_khi-score_qld)
            print(f"Karachi King Win with score is {win_score}")
        
        elif score_qld > score_khi:
            win_score = (score_qld-score_khi)
            print(f"Quetta Gladiators Win with score is {win_score}")
        else:
            print(f"Match Tie {score_khi}")
            
    else:
        print("Invalid Tournament Id or Tournament Name:")
else:
    print("You are not Eligible for this Tournament")