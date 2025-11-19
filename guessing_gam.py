#Guess Game
import random

Target=random.randint(1,100)

while True:
    user_choice=(input("Guess The Target Or Quit : "))
    if(user_choice=="Quit"):
        break
    user_choice=int(user_choice)
    if(user_choice==Target):
        print("Success: Correct Guess!!")
        break
    elif(user_choice<Target):
        print("Your Number Was Too small .Take Bigger Guess..")
    else:
        print("Your Number Was Too Big .Take Smaller Guess..")

print("-------Game Over------")