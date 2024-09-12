import unittest  # import the unittest module to test the code components
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))
import hobby_card  # type: ignore

# much of this file is boilerplate code you can use in the future
# for now, you will just run the tests to see if your code is correct
# these tests mimic the autograder, so if you pass these tests,
# you should be *close* to the autograder - but if something
# works on your computer it doesn't always mean it works on ours





class TestAsciiArt(unittest.TestCase):
    """Unit tests to test the formatting of hobby card and to make sure my_art.py file is submitted."""

    def setUp(self) -> None:
        self.card_lines = (
            hobby_card.hobby_card().strip().split("\n")
        )  # can use the same card for various tests
        length = len(self.card_lines)
        self.assertEqual(
            7, length, "Make sure you didn't add extra lines or have it missing lines."
        )
        return super().setUp()

    def test_first_last(self) -> None:
        """Tests to see if the first and last line of the hobby card follow the correct format."""
        card = "+" + "-" * 30 + "+"  # note \n removed as the card is split on them
        self.assertEqual(
            card,
            self.card_lines[0],
            "Double check your dash count for the fist line (hint use * 30).",
        )
        self.assertEqual(
            card,
            self.card_lines[6],
            "Double check your dash count for the last line (hint use * 30).",
        )

    def test_title(self) -> None:
        """Tests to make sure A Hobby Card is centered with 9 spaces before and after with bars."""
        correct = "|" + " " * 9 + "A Hobby Card" + " " * 9 + "|"  # new line removed
        self.assertEqual(
            correct,
            self.card_lines[1],
            "Maybe look at the spacing or spelling? Is it exact, case matters.",
        )

    def test_blank_lines(self) -> None:
        """Tests to make sure there is a blank line after name, and after hobbies."""
        correct = "|" + " " * 30 + "|"  # again \n removed
        self.assertEqual(
            correct,
            self.card_lines[3],
            "Line after your name. Double check the spaces or the bars. Total line is 32 characters long.",
        )
        self.assertEqual(
            correct,
            self.card_lines[5],
            "Line after your name. Double check the spaces or the bars. Total line is 32 characters long.",
        )

    def test_name_line(self) -> None:
        """Tests to make sure your name is correctly spaced."""
        start = self.card_lines[2].startswith("| ")
        self.assertTrue(
            start,
            f"Check to see if your name line starts with bar and a space. Found:\n'{self.card_lines[2]}' (quotes added for clarity)",
        )
        end = self.card_lines[2].endswith("|")
        self.assertTrue(
            end,
            f"Check to see if your name line ends with a bar. Found:\n'{self.card_lines[2]}' (quotes added for clarity)",
        )
        length = len(self.card_lines[2])
        self.assertEqual(32, length, "Make sure the total card with remains 32.")

    def test_hobby_line(self) -> None:
        """Tests to make sure your hobby exists, with 4 spaces before it."""
        start = self.card_lines[4].startswith("|    ")
        self.assertTrue(
            start,
            f"Check to see if your hobby line starts with bar and 4 spaces. Found:\n'{self.card_lines[4]}' (quotes added for clarity)",
        )
        length = len(self.card_lines[4])
        self.assertEqual(32, length, "Make sure the total card with remains 32.")


if __name__ == "__main__":
    unittest.main()
