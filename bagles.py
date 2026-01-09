# Bagles by DAYVIS,
# A deductive logic game where you guess a number based on clues.
# Tags:short,game, puzzle


import random

NUM_DIGITS = 4
MAX_GUESSES = 3


def main():
    print(
        f"""Bagles, a deducive logic game.
By DAYVIS

I am thinking of a 3- digit number. Try and guess what it is.
Here are some  clues:
When i say:         That means:
    Pico            One digit is correct but in the wrong position.
    Fermi           One digit is correct and in the right position.
    Bagles           No digit is correct.
For example if the secret number 248 and your guess was 843,the
clues would be Fermi Pico.""".format(
            NUM_DIGITS
        )
    )

    while True:  # main loop
        secretNum = getSecretNum()
        print("I have thought up a number.")
        print("you have {} guesses to get it.".format(MAX_GUESSES))

        numguesses = 1
        while numguesses <= MAX_GUESSES:  # LOOPS TILL VALID GUESS
            guess = ""
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print("Guess {}:".format(numguesses))
                guess = input("> ")

            clues = getclues(guess, secretNum)
            print(clues)
            numguesses += 1

            if guess == secretNum:

                break  # break loop
        if numguesses > MAX_GUESSES:
            print("YOU RAN OUT OF GUESSES")
            print("THE ANSWER WAS{}.".format(secretNum))

            print("DO YOU WANT TO PLAY AGAIN? (YES or NO)")
        if not input("> ").lower().startswith("y"):
            break


print("THANKS FOR PLAYING")


def getSecretNum():  # string of random digits
    numbers = list("0123456789")
    random.shuffle(numbers)  # shuffle them into random other

    secretNum = " "
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])

    return secretNum


def getclues(guess, secretNum):
    if guess == secretNum:
        return "YOU GOT IT"

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            # A correct digit is in the correct place
            clues.append("Fermi")
        elif guess[i] in secretNum:  # A correct digit is in the incorrect place
            clues.append("Pico")
    if len(clues) == 0:
        return "Bagles"
    else:
        # sort the clues into alphabetical order so their original order
        # doesn't give information away.
        clues.sort()
        # makes a single string from the list of string clues
        return "".join(clues)


# if the program is run, instead of imported , run the game:
if __name__ == "__main__":
    main()
