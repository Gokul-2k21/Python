import random
computer = random.choice(["Rock","Paper","Scissor"])
user = input("Do you want Rock,Paper or Scissor ?\n") 

if computer == user :
    print("Tie")
elif computer == "Rock" and user == "Paper" :
    print("You Win !")   
elif computer == "Paper" and user == "Scissor" :
    print("You Win !")
elif computer == "Scissor" and user == "Rock" :
    print("You Win !")
else :
    print("You Loose !") 
print("\n")            