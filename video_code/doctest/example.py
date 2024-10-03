
def check_blue(low: int, high: int) -> bool:
    """
    Checks to see if the low is <= 0, and high is >= 50
    
    Examples:
        >>> check_blue(0, 50)
        True
        >>> check_blue(-100, 300)
        True
        >>> check_blue(0, 100)
        True
        >>> check_blue(0, 49)
        False

    Args:
        low (int): the low value
        high (int): the high value

    Returns:
        bool: True if the low is <= 0, and high is >= 50
    """
    return low <= 0 and high >= 50
   

def check_red(low: int, high: int) -> bool:
    """
    Checks to see if the low is <= 51, and high is >= 100

    Examples:
        >>> check_red(51, 100)
        True
        >>> check_red(50, 99)
        False
        >>> check_red(52, 101)
        False
        >>> check_red(0, 0)
        False
    
    Args:
        low (int): the low value
        high (int): the high value

    Returns:
        bool: True if the low is <= 51, and high is >= 100
    """
    if low <= 51 and high >= 100:
       return True
    else:
       return False


def check_yellow(low: int, high: int) -> bool:
    """
    Checks to see if the low is <= 0, and high is >= 200
    
    Examples:
        >>> check_yellow(0, 200)
        True
        >>> check_yellow(-100, 300)
        True
        >>> check_yellow(0, 100)
        False
        >>> check_yellow(0, 199)
        False


    Args:
        low (int): the low value
        high (int): the high value

    Returns:
        bool: True if the low is <= 0, and high is >= 200
    """
    return low <= 0 and high >= 200


def new_range_check(low: int, high: int) -> str:
    """
    Checks to see if blue, red, or yellow strings
    will be returned if a value is within a range.

     Examples:
        >>> range_check(0, 50)
        'blue,'
        >>> range_check(-100, 300)
        'blue,red,yellow,'
        >>> range_check(0, 100)
        'blue,red,'

    Args:
        low (int): the low value
        high (int): the high value

    Returns:
        str: a string separated by commas. Unknown if nothing falls in the range.
    """
    colors = ''
    if check_blue(low, high):
        colors += 'blue,'
    
    if check_red(low, high):
        colors += 'red,'

    if check_yellow(low, high):
        colors += 'yellow,'

    if not colors:
        colors = "Unknown"

    return colors



def range_check(low: int, high: int) -> str:
    """
    Checks a range and adds values based on the table below.
    
    | value   |  low   | high |
    |---------|--------|------|
    | blue    |  0     |  50  |
    | red     |  51    |  100 |
    | yellow  |  0     |  200 |
    
    It adds value if the low or high are both 'outside' the range.
    
    Examples:
        >>> range_check(0, 50)
        'blue,'
        >>> range_check(-100, 300)
        'blue,red,yellow,'
        >>> range_check(0, 100)
        'blue,red,'

    Args:
        low (int): low end of the range
        high (int): high end of the range

    Returns:
        str: the string of values
    """
    colors = ''
    if low <= 0 and high >= 50:
        colors += 'blue,'

    if low <= 51 and high >= 100:
        colors += 'red,'

    if low <= 0 and high >= 200:
        colors += 'yellow,'

    if colors == '':
        colors = "Unknown"

    return colors





def main():
    """Main function to run the program"""




if __name__ == "__main__":
    main()