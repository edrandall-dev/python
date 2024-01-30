import sys
import random

def main():
    lower, upper = set_range()
    secret_number = random.randint(lower,upper)
    #print(secret_number)
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

def usage():
    print("Usage: " + sys.argv[0] + " [lower integer] [upper integer]")
    sys.exit(1)

def set_range():
    if len(sys.argv) == 3:
        try:
            lower = int(sys.argv[1])
            upper = int(sys.argv[2])
        except ValueError:
            usage()
    elif len(sys.argv) == 1:
        lower = 1
        upper = 100
    else:
        usage()

    if upper < lower:
        usage()
 
    if upper > 100:
       upper = 100
    
    if lower < 1:
       lower = 1

    return lower, upper
   

main()