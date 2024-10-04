__author__ = "730768373"


def input_guess(length: int) -> str:
    """Function to check the length of the guess and then return if it is a valid length guess"""
    guess = input(f"Enter a {length} character word: ")
    # Asks to re-enter the guess if it does not match the length of the secret word.
    while len(guess) != length:
        guess = input(f"That wasn't {length} chars! Try again: ")
    return guess


def contains_char(word: str, char_guess: str) -> bool:
    """Checks if the given character is in the selected 5 character word"""
    # Initiating variables for number of instances of the letter and whether the letter is found at all.
    assert len(char_guess) == 1
    # Conditionals to check if each of the letters in the word match the given letter.
    index: int = 0
    # Checks if a given letter is in a word anywhere.
    while index < len(word):
        if word[index] == char_guess:
            return True
        index += 1
    return False


def emojified(guess: str, secret: str) -> str:
    """Function to compare each letter of the guess to the secret and print out a certain colored box"""
    assert len(guess) == len(secret)

    # variables for the boxes
    WHITE_BOX = "\U00002B1C"
    GREEN_BOX = "\U0001F7E9"
    YELLOW_BOX = "\U0001F7E8"

    # intialize variables for iteration and result
    output = ""
    index = 0

    # loop to check each letter and assign a green, white or yellow box based on value.
    while index < len(guess):
        if guess[index] == secret[index]:
            output += GREEN_BOX
        elif contains_char(secret, guess[index]):
            output += YELLOW_BOX
        else:
            output += WHITE_BOX
        index += 1

    return output


def main(secret: str) -> None:
    """Main method to run all the functions so the program functions as a game"""
    # Initializing turn count variables (+1 to both for visual purposes)
    turns: int = 1
    max_turns: int = 7

    # Checking for turn count so that the game terminates after 6 turns.
    while turns < max_turns:

        print(f"=== Turn {turns}/6 ===")
        input: str = input_guess(len(secret))
        result: str = emojified(input, secret)
        print(result)

        if result == "\U0001F7E9" * len(secret):
            print(f"You won in {turns}/6 turns!")
            break
        else:
            if turns == 6:
                print("X/6 - Sorry, try again tomorrow!")
                break
            else:
                turns += 1


if __name__ == "__main__":
    """Checks if the code is being run directly as the main file without importing"""
    main(secret="codes")
