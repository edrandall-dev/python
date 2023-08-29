#!/usr/bin/python3

secret_number = 128

def have_a_guess():
  global guess
  guess = int(input("Have a guess of the secret number: "))
  
have_a_guess()

while secret_number != guess:
  if secret_number > guess:
    print ("Your guess of " + str(guess) + " is too low")
  elif secret_number < guess:
    print ("Your guess of " + str(guess) + " is too high")
  have_a_guess()
  
print("You guessed it, it was " + str(secret_number)+ "!")