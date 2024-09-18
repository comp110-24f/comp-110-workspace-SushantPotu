# CQ 2 for conditionals
__author__: str = "730768373"


def guess_a_number() -> None:
    """Function for guessing number"""

    # Number that needs to be guessed
    secret: int = 7

    # Variable for collecting user input
    x: int = int(input("Guess a number: "))

    # Prints out guess value
    print("Your guess was", x)

    # Checks if x is lower, higher or the same as the secret value
    if x == secret:
        print("You got it!")
    elif x < secret:
        print("Your guess was too low! The secret number is", secret)
    elif x > secret:
        print("Your guess was too high! The secret number is", secret)


# Runs the code if the file is not imported from a module (runs if the code is the main program)
if __name__ == "__main__":
    guess_a_number()
