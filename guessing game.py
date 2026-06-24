import random


jackpot = random .randint(1,100)


counter = 1
guess = int(input( "enter your guess number:"))
while guess != jackpot:
    if guess < jackpot:
        print("guess higher")
    else:
        print("guess lower")
    
    guess = int(input("enter your guess number:"))
    counter += 1

print("correct guess")
print("you took", counter,"attempts")
print("you win")        
