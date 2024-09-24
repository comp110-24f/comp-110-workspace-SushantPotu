"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730768373"


def input_word() -> str:
    """Takes input for word that is being searched for given letter"""
    # Word input is taken.
    word_input: str = input("Enter a 5-character word: ")
    # Conditional to check if word is 5 characters and exits if it isn't.
    if len(word_input) != 5:
        print("Error: Word must contain 5 characters.")
        exit()
    # Returns the given word once it passes the 5 character condition.
    return word_input


def input_letter() -> str:
    """Takes input for the letter you want to find in the given word"""
    # Takes character input.
    character: str = input("Enter a single character: ")
    # Checks if the input is only one character and exits if it isn't.
    if len(character) != 1:
        print("Error: Character must be a single character.")
        exit()
    # Returns the given character once it is confirmed it is only one character.
    return character


def contains_char(word: str, letter: str) -> None:
    """Checks if the given character is in the selected 5 character word"""
    # Initiating variables for number of instances of the letter and whether the letter is found at all.
    instances: int = 0
    # Tells user that the letter is being searched for.
    print("Searching for", letter, "in", word)
    # Conditionals to check if each of the letters in the word match the given letter.
    if letter == word[0]:
        print(letter, "found at index", 0)
        instances += 1
    if letter == word[1]:
        print(letter, "found at index", 1)
        instances += 1
    if letter == word[2]:
        print(letter, "found at index", 2)
        instances += 1
    if letter == word[3]:
        print(letter, "found at index", 3)
        instances += 1
    if letter == word[4]:
        print(letter, "found at index", 4)
        instances += 1
    # Checks if the word has been found at all and returns statements based on that.
    if instances == 0:
        print("No instances of", letter, "found in", word)
    if instances > 1:
        print(instances, "instances of", letter, "found in", word)
    if instances == 1:
        print(instances, "instance of", letter, "found in", word)


def main() -> None:
    """Runs the contains character function with the other two functions as arguments to run the program"""
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    """Runs the main function if the file is being run as the main program"""
    main()
