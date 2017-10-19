from random import randint

def numbercheck():
    number = randint(1, 100)
    guesses = 0
    correct = False
    while correct == False:
        guesses = guesses + 1
        guess = int(input("Guess a number between 1 and 100: "))
        if guess == number:
            print("You guessed correct.")
            print(f"It took you {guesses} guesses to get the right answer.")
            correct = True
        elif guess > number:
            print("You guessed too high.")
        elif guess < number:
            print("You guessed too low.")

numbercheck()
