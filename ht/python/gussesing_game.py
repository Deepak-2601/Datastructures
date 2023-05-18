ans = 10
print("Please guess a number between 1 and 20: ")
guesses = int(input())
if guesses == ans:
    print("Congratulation you gussed it in first try")
else:
    if guesses < ans:
        print("Please guess higher")
    else:
        print("Please guess lower")
    guesses = int(input())
    if guesses == ans:
        print("Well done you guessed it correct")
    else:
        print("Sorry your guess was wrong and you have ran out of chance")

