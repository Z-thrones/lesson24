import random
playing = True
number = str(random.randint(0,9))
print("Guess a random nmber between 0 and 9")
while playing == True:
    guess = input("Enter your guess: ")
    if guess == number:
        print("You win!")
        print(number)
        break
    else:
        print("Try again")
        continue