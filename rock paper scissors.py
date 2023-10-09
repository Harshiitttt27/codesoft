#Rock paper scissor game in which winning is as follows:-
# rock vs scissor = rock wins
# scissor vs paper =  scissor win
# paper vs rock = paper win
# In this code we have used 


import random

list = ["rock", "paper", "scissor"]

def check(player, computer):
    if computer == player:
        return 0
    elif computer == 0 and player == 1:
        return -1
    elif computer == 1 and player == 2:
        return -1
    elif computer == 2 and player == 0:
        return -1
    else:
        return 1

while True:
    print(""" 
    0 for rock
    1 for paper 
    2 for scissor
    """)

    player = int(input("Enter your choice:\n"))
    computer = random.randint(0, 2)
    score = check(computer, player)
    
    print(f"You choose : {list[player]}")
    print(f"Comp choose : {list[computer]}")

    if score == 0:
        print("It's a tie!")
    elif score == -1:
        print("You lose!")
    else:
        print("You win!")

    again = input("Do you want to play again? (yes/no): ")
    if again.lower() != "yes":
        break
   