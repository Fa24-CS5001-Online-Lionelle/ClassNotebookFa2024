

def request_number(prompt: str) -> int:
    """Request a number from a client, converts it to an int.

        Note: this function does not do any error checking.
      Args:
        prompt (str): The prompt to display.

      Returns:
        int: the number.
    """
    pass


def get_pluses(number : int) -> int:
    """Gets a string of pluses by size count.
        
        Args:
            number (int): The size count of the pluses.
        Returns:
            int: The number of pluses."""
    pass    



def main():
    """This is the main function where the program pluses starts running."""
    count = request_number("Enter the number of pluses you want to see: ")
    print(get_pluses(count))




# This block of "magic" informs the python interpreter to start executing code in the main() function
# when the file is loaded.
if __name__ == "__main__":
    main()

