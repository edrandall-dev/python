#!/usr/bin/python3

import random

lower = 1
upper = 100

secret_number = random.randint(lower,upper)

print ("I have chosen a secret number between " + str(lower) + " and " + str(upper) + ". Let's see how quickly you can guess it.", end=" ")

tries = 0

while True:
  tries = tries + 1
  guess = int(input("Enter a guess: "))

  if guess > upper:
    print ("Guess number " + str(tries) + ": Remember that it's a number between " + str(lower) + " and " + str(upper), end=". ")
  elif guess < lower:
    print ("Guess number " + str(tries) + ": Remember that it's a number between " + str(lower) + " and " + str(upper), end=". ")
  else:
    if guess > secret_number:
      print ("Guess number " + str(tries) + ": Your guess of " + str(guess) + " is too high")
    elif guess < secret_number:  
      print ("Guess number " + str(tries) + ": Your guess of " + str(guess) + " is too low")
    else:  
      print("You guessed that it was " + str(secret_number) + " in " + str(tries) + " guesses!")
      break