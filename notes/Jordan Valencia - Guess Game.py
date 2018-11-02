import random
random1 = (random.randint(0, 10))

guess_number = int(input("Guess a number between 0 to 10 "))

if guess_number > random1:
    print("You lose, %s was actually your number." % random1)
elif guess_number < random1:
    print("You lose, %s was actually your number." % random1)
elif guess_number == random1:
    print("You win!")
