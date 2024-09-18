"""Challenge question 3 for while loops"""

__author__ = "730768373"


def num_instances(phrase: str, search_char: str) -> int:
    """Returns the number of times a letter appears in a given phrase"""
    count = 0
    index = 0
    """While loop to go through each letter in the phrase and check if it matches the letter bring searched for"""
    while index < len(phrase):
        if phrase[index] == search_char:
            count += 1
        index += 1
    return count


print(num_instances(phrase="HelloHeLloHEllo", search_char="e"))
print(num_instances(phrase="HelloHelloHello", search_char="e"))
print(num_instances(phrase="Happy Tuesday!", search_char="y"))
print(num_instances(phrase="Happy Tuesday!", search_char="z"))
