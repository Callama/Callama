import random

#Get Random number between 1 and ten
randnum = random.randint(1,10)
#Set Win to false
win = False 




#Game Logic
print("Okay, I'm thinking of a Number bewteen 1 & 10!")
# As Long as player has not won, loop code 
while win == False:
    guess = int(input("Have a Guess.."))
    if guess == randnum:
        win = True
    elif guess < randnum:
        print("Guess Higher!")
    elif guess > randnum:
        print("Guess Lower!")
        #Once the Player wins the game!
if win == True:
    print("Yay! You got it!")


    


   