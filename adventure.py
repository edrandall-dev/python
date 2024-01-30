name = input("hello there traveler! whats your name? ")
print ("ah! nice to meet you, " + name)

while True:
    answer = input("are you new around here?")
    if answer == "yes":
        print ("well, you're going to love it here.")
        break
    elif answer == "no":
        print ("huh, how come I've never seen you before then?")
        break
    else:
        print ("hey, please answer my question. yes or no.")