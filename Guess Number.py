import random
num=random.randint(1,20)

while True:
    guess=int (input("Guess A Number Between 1 To 20 : "))
    if guess==num:
               print("You Guess A Correct Number")
               break
    elif guess>num:
                print ("You Guesses A Greater Number")
    elif guess<num:
                print("You Guesssed A Smaller Number")
