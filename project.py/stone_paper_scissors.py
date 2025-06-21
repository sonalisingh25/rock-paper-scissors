
import random
options = [ "rock" , "paper","scissors"]
while True:
    user = input("enter your choice: ").lower()
    if user not in options:
        print("invalid choice!. try again!")
        continue
    computer = random.choice(options)
    print(f"the computer chose: {computer}")
    if (user == computer):
        print("its draw")
    elif(user == "rock" and computer == "scissor")or\
        (user == "scissor" and computer == "paper")or\
        (user =="paper" and computer =="rock"):
        print("you win!")
    else:
        print("computer win!")    

    play_again= input("play again? (yes or no:)").lower()
    if play_again!= "yes":
     break
