# simple program to have a user guess a random number between 1-20

# import the random module
import random
number = random.randint(1, 21)

# Create a list of 20 random numbers between 1 and 20
random_numbers = [random.randint(1, 20) for _ in range(20)]
    

print("Guess a number between 1 and 20")
guess = int(input())
while guess != number:
    if guess < number:
        print("Too low. Try again.")
        guess = int(input())
    else:
        print("Too high. Try again.")
        guess = int(input())

print("Congratulations! You guessed the number correctly.")
print("The number was: ", number)
