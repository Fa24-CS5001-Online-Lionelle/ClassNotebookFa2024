
def check_blue(low: int, high: int) -> bool:
    """

    Args:
        low (int): _description_
        high (int): _description_

    Returns:
        bool: _description_
    """
    return low <= 0 and high >= 50
   
 # | red     |  51    |  100 |
def check_red(low: int, high: int) -> bool:
     """_summary_

     Args:
         low (int): _description_
         high (int): _description_

     Returns:
         bool: _description_
     """
     if low <= 51 and high >= 100:
        return True
     else:
        return False

# | yellow  |  0     |  200 |
def check_yellow(low: int, high: int) -> bool:
    """_summary_

    Args:
        low (int): _description_
        high (int): _description_

    Returns:
        bool: _description_
    """
    return low <= 0 and high >= 200


def new_range_check(low: int, high: int) -> str:
    """_summary_

    Args:
        low (int): _description_
        high (int): _description_

    Returns:
        str: _description_
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