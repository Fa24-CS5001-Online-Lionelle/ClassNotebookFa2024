

def request_number(prompt: str) -> int:
    """Request a number from a client, converts it to an int.

        Note: this function does not do any error checking.
      Args:
        prompt (str): The prompt to display.

      Returns:
        int: the number.
    """
    value_str = input(prompt) 
    return int(value_str)   

def get_pluses(number : int) -> str:
    """Gets a string of pluses by size number.
        
        Args:
            number (int): The size number of the pluses.
        Returns:
            str: The number of pluses as full string."""
    return '+' * number

def main():
    """This is the main function where the program pluses starts running."""
    count = request_number("Enter the number of pluses you want to see: ")
    print(get_pluses(count))




# This block of "magic" informs the python interpreter to start executing code in the main() function
# when the file is loaded.
if __name__ == "__main__":
    main()

