def invert(inp: dict[str, str]) -> dict[str, str]:
    """Inverts all values of the dict without any repeated keys"""
    inverted = {}
    duplicates: list[str] = []
    # Checks if the key is repeated and raises error and otherwise adds the key to duplicates for the next run through.
    # Inverts the value and adds it to a new dict if not a duplicate.
    for key in inp:
        if inp[key] in duplicates:
            raise KeyError(f"Duplicate key encountered in inversion: {key}")
        duplicates.append(inp[key])
        inverted[inp[key]] = key

    return inverted


def favorite_color(fav: dict[str, str]) -> str:
    """Counts the instances of colors and returns the most popular color found in the dict."""

    color_count: dict[str, int] = {}
    highest_count: int = 0
    most_color: str = ""
    # checks and keeps track of the favorite color of each person by storing all info in a dictionary
    for person in fav:
        if fav[person] in color_count:
            color_count[fav[person]] += 1
        else:
            color_count[fav[person]] = 1
    # Iterates through the counts for each number to find the highest count for any given color and stores and returns that color at the end
    for color in color_count:
        if color_count[color] > highest_count:
            most_color = color
            highest_count = color_count[color]
        elif color_count[color] == highest_count:
            continue
    return most_color


def count(items: list[str]) -> dict[str, int]:
    """Counts each item in dict and keeps track of them in a different dict that is returned at the end."""
    counts: dict[str, int] = {}
    # Checks if the item is in counts dict already and adds one or creates a new item in counts dict if it isn't.
    for item in items:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Checks the first lettter of each word in words and sorts the words based on that letter into a dict"""
    result = {}
    # Checks if the letter is already in the dict and creates a new value or adds onto existing list if it isn't.
    for word in words:
        first_letter = word[0].lower()
        if first_letter not in result:
            result[first_letter] = [word]
        else:
            result[first_letter].append(word)
    return result


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """Updates attendance for a given student."""
    # If the day is already in the attendance dict, adds the student to the list of students attending
    if day in attendance:
        if student not in attendance[day]:
            attendance[day].append(student)
    # Creates a day in the attendance dict and adds name to that day
    else:
        attendance[day] = [student]
