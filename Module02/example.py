

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