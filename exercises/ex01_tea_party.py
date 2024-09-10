"""
Tea party exercise for COMP 110, 
calculates number of tea bags needed, the number of treats needed,
and the expected cost of the party
"""

__author__: str = "730768373"


def tea_bags(people: int) -> int:
    """Calculates the number of teabags needed for the party"""
    return people * 2
    # Multiplies the variable people by two and returns it
    # This is because two teabags are needed per person


def treats(people: int) -> int:
    """Calculates the number of treats needed for the party"""
    return int(tea_bags(people=people) * 1.5)
    # Multiplies number of tea bags needed by 1.5 and returns it
    # Each person wants 1.5 treats to accompany tea


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the total cost of the treats and tea"""
    return tea_count * 0.5 + treat_count * 0.75
    # Adds together the cost for tea and treats and returns it
    # Each tea costs $0.50 and each treat costs $0.75
    # These values are multiplied by the variable to find cost


def main_planner(guests: int) -> None:
    """prints out the final cost and number of items in final formatting"""
    print("A Cozy Tea party for " + str(guests) + " people!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))
    # Prints out the information about the party in formatted form
    # Number of guests, teabags, treats and the total cost


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
    # Runs the code if the file is not imported from a module
    # The file must also be run as the main program
