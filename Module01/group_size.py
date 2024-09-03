"""
This file is to demonstrate a small program using functions.
"""


def get_whole_number(prompt: str) -> int:
    """Gets a whole number from the client. 

    No error checking.

    Args:
        prompt (str): the prompt to display before getting the number.

    Returns:
        int: a whole number
    """
    num_str = input(prompt)
    return int(num_str)



def get_group_size(class_size: int, number_of_groups: int) -> int:
    """
    Gets the size of the groups given the number of groups.

    Args:
        class_size (int): the size of the class
        number_of_groups (int): number of groups to form

    Returns:
       (int) : the size of the groups. 
    """
    return class_size // number_of_groups


def get_overflow(class_size: int, group_size: int) -> int:
    """
        Gets the number of students that would overflow the group size.
        Or another way to look at it, the number of groups that would
        need to be size + 1.

    Args:
        class_size (int): total students
        group_size (int): the size of the groups

    Returns:
        int: the number of students not grouped
    """
    return class_size % group_size




def main():
    class_size = get_whole_number("Enter the class size: ")
    number_of_groups = get_whole_number("Enter the number of groups: ")

    group_size = get_group_size(class_size, number_of_groups)
    overflow = get_overflow(class_size, group_size)

    print(f"Group size: {group_size}")
    print(f"The number of groups that will need to be {group_size +1}: {overflow}")


if __name__ == "__main__":
    main()



