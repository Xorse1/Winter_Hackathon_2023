"""Simple number guessing game
Ask user to guess a number between 1 and 100
Compare guess number with the generated number
Give user a nice gift if guess number is the generated number
"""

import random  # import random module, generate random number

# print welcome message
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 10.")
print("Make a guess and I'll tell you if you're right!\n")

# Generate randnom number between 1 and 10
computer_guess = random.randint(1, 10)

# Ask user for guess number
user_guess = int(input("Guess a number between 1 and 10: "))

while user_guess != computer_guess:
  if user_guess > computer_guess:
      print("Your Guess is too big")
  else:
    print("Your Guess is too small")
  user_guess = int(input("Guess a number between 1 and 10: "))

print("You won AZUBI PENGUIN!")