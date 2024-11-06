import random

answer = random.randrange (1, 30)

chance = 0
print("You only have 5 chances")
while chance < 5:
    guess = int(input("Guess a number from 1 to 30 "))
    if guess == answer:
        print("You guessed it!!")
    if guess > answer:
        print("Go lower")
        if guess<10:
            print("guess number between 1 to 10 ")
        if guess<20:
            print("guess number between 11 to 20")
        if guess<30:
            print("guess number between 21to 30 ")
    elif guess < answer:
        print("Go higher")
    chance += 1
    if chance == 5:
        print("Game Over")


print("The number was", answer)