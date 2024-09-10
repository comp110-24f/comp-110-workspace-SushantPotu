"""My first CQ in COMP110!"""

__author__ = "730768373"


def mimic(message: str) -> str:
    """Function that returns the exact message that you give it"""
    return message


def main() -> None:
    """Main function that returns nothing"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
