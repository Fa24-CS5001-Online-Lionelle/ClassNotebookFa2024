import unittest  # import the unittest module to test the code components
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

## much of this file is boilerplate code you can use in the future
## for now, you will just run the tests to see if your code is correct
## these tests mimic the autograder, so if you pass these tests,
## you should be *close* to the autograder - but if something
## works on your computer it doesn't always mean it works on ours


import star_rating  # type: ignore

class TestStarRating(unittest.TestCase):
  
    def test_one_star(self) -> None:
        """Testing that one_star() builds a single star string"""
        actual = star_rating.one_star()
        expected = "*"
        self.assertEqual(expected, actual, msg="Double check the number of stars")

    def test_two_star(self) -> None:
        """Testing that two_star() builds a two star string"""
        actual = star_rating.two_star()
        expected = "**"
        self.assertEqual(expected, actual, msg="Double check the number of stars")

    def test_three_star(self) -> None:
        """Testing that three_star() builds a three star string"""
        actual = star_rating.three_star()
        expected = "***"
        self.assertEqual(expected, actual, msg="Double check the number of stars")

    def test_four_star(self) -> None:
        """Testing that four_star() builds a four star string"""
        actual = star_rating.four_star()
        expected = "****"
        self.assertEqual(expected, actual, msg="Double check the number of stars")
    
    def test_five_star(self) -> None:
        """Testing that five_star() builds a five star string"""
        actual = star_rating.five_star()
        expected = "*****"
        self.assertEqual(expected, actual, msg="Double check the number of stars")

    def test_get_rating_block(self) -> None:
        """Tests the rating block is returned properly"""
        actual = star_rating.get_rating_block()
        expected = \
"""1 star rating: *
2 star rating: **
3 star rating: ***
4 star rating: ****
5 star rating: *****
""" # this is a multi-line string.
        self.assertEqual(expected, actual, msg="Double check the wording and spaces!")

if __name__ == '__main__':
    unittest.main()
