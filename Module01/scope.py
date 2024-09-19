""" 
Examples going over scope
"""

girl_who_waited = "Amy Pond"  #DON"T DO THIS UNLESS
SEPARATOR = "\n"

print(girl_who_waited)
 



def people(someone: str) -> str:
    r"""Add's girl_who_waited to someone, returns both

    Examples:
        >>> people("Rory")
        'Rory\nAmy'
        >>> people("Who")
        'Who\nAmy'
        >>> people('')
        '\nAmy'
    
    Args:
        someone (str): name of person

    Returns:
        str: someone with girl_who_waited added
    """
    girl_who_waited = "Amy Pond"
    new_people = someone + SEPARATOR + girl_who_waited
    return new_people

print("--")
print(people("Rory"))

print("--")

girl_who_waited = "Amy Williams"
new_str = people("Who")
print(new_str)

print("--")

just_amy = people('')
print(just_amy)

print("--")
print(girl_who_waited) # Amy Williams

