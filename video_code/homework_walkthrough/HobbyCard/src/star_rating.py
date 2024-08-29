"""
Homework 1: Star Rating App
===========================
Course:   CS 5001
Semester: UPDATE
Student:  YOUR NAME

An assignment to practice string concatenation.
"""
# The block above is a docstring (short for document string).
# It starts at the triple double quote,
# and ends at the triple double quote
# Make sure you update it by modifying semester and your name


def one_star() -> str:
    """sets a single * to the variable stars."""
    stars = ''  # change me
    return stars


def two_star() -> str:
    """sets two * to the variable stars."""
    stars = ''  # change me, make sure to use the * operator
    return stars


def three_star() -> str:
    """sets three * to the variable stars."""
    stars = ''  # change me
    return stars


def four_star() -> str:
    """sets four * to the variable stars."""
    stars = ''  # change me
    return stars


def five_star() -> str:
    """sets five * to the variable stars."""
    stars = ''  # change me
    return stars


def get_rating_block() -> str:
    """Gets a block with the various ratings."""
    block = "1 star rating:" + one_star() + "\n"
    block += "2 star rating:" + two_star() + "\n"
    block += "3 star rating:" + three_star() + "\n"
    block += "3 star rating:" + four_star() + "\n"
    block += "3 star rating:  " + five_star() + "\n"
    return block


def main():
    print(get_rating_block())
    # also you could do the following
    rating = five_star()
    print(f"\nMy star rating is {rating}\n")  # look up format strings!
    # something cool about docstrings
    help(five_star)


# This block of "magic" informs the python interpreter to start
# executing code in the main() function
# when the file is loaded.
if __name__ == "__main__":
    main()
