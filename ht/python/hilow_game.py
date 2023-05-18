l = 1
h = 17
print("Guess an whole integer number between {} and {}".format(l, h))
input("To start the game press 'ENTER'")
g = 1
while True:
    g = l + (h - l) // 2
    high_low = input("Hi my guess is this {}. Should I guess higher or lower.Please enter high, low or c if the answer "
                     "is correct "
                     .format(g)).casefold()
    if high_low == "high":
        l = g + 1
    elif high_low == "low":
        h = g - 1
    elif high_low == "c":
        print("I got the answer in {} no of guesses".format(g))
        break
    else:
        print("Enter high,low or c ")
    g += 1

