


print("Aloha, World @@@@")

char_str = '@' * 4
print(f"Aloha, World {char_str}")

char_str = '@' * 5
print(f"Aloha, World {char_str}")

char_str = '@' * 6
print(f"Aloha, World {char_str}")

def build_char_str(number: int) -> str: 
    """It builds a character string of '+' of length number.

    Args:
        number (int): the total number of '+' in the string

    Returns:
        str: a string of '+' of length number.
    """
    line = '+' * number 
    return line

char_str = build_char_str(10)
print(f"Aloha, World {char_str}")

char_str = build_char_str(20)
print(f"Aloha, World {char_str}")

char_str = build_char_str(30)
print(f"Aloha, World {char_str}")
