"""Another way to hack a route cipher.

Already implemented in :py:mod:`~src.ch04.practice.p1_hack_lincoln`, but this
version will use the building blocks made in
:py:mod:`~src.ch04.practice.p2_identify_cipher`,
:py:mod:`~src.ch04.practice.p3_get_keys`, and
:py:mod:`~src.ch04.practice.p4_generate_keys`.

"""
from src.ch03.c1_anagram_generator import split
from src.ch04.practice.p2_identify_cipher import is_substitution
from src.ch04.practice.p3_get_keys import key_to_dict
from src.ch04.practice.p4_generate_keys import generate_keys


def decode_route(keys: dict, cipherlist: list) -> list:
    """Decode route cipher.

    Decode **cipherlist** encoded with a route cipher using **keys**.

    Args:
        keys (dict): ``up``/``down`` dictionary with column numbers as keys.
        cipherlist (list): List of strings representing encoded message.

    Returns:
        List of strings representing plaintext message.

    Note:
        Assumes vertical encoding route.

    """
    table, message = [], []
    split_list = split(cipherlist, len(keys))
    # Build translation table.
    for key, value in keys.items():
        if value == 'down':
            # If down, reverse direction
            split_list[key - 1].reverse()
        table.append(split_list[key - 1])
    # For each column in the table, copy the relevant row.
    rows = len(split_list[0])
    for row in range(rows):
        for column in table:
            message.append(column[row])
    return message


def hack_route(ciphertext: str, columns: int) -> None:
    """Hack route cipher using brute-force attack.

    Determine if **ciphertext** is a transposition cipher. If so, use
    **columns** to generate all possible keys. Convert each key to an
    ``up``/``down`` dictionary for each route to take, then print the
    result of each key.

    Args:
        ciphertext (str): Route cipher encoded string to hack.
        columns (int): Number route cipher columns.

    Returns:
        :py:obj:`None`. Prints all possible decoded messages.

    """
    if ciphertext.isupper():
        # Most functions assume lowercase, despite cryptographic convention.
        ciphertext = ciphertext.lower()
    if is_substitution(ciphertext):
        print('Hey, bub, I can\'t help you with substitution ciphers.')
        return None
    # Get all possible keys with given number of columns.
    keys = generate_keys(columns)
    # For each key, decode route cipher and print result.
    for key in keys:
        message = ' '.join(decode_route(key_to_dict(key), ciphertext.split()))
        print(f'Key: {key}\nDecoded message: {message}\n')
    return None


def main():
    """Demonstrate the route cipher hacker."""
    print('There\'s more than one way to hack a route cipher! I can also do a '
          'brute-force\nhack of a route cipher. Although, you\'ll have to '
          'tell me how many columns to\nuse.')
    print('\nNote: I only hack the route cipher. I leave the '
          'word-transposition cipher to\nyou and your biochemical brain.\n')
    # Four column route 'cyphertext' from book.
    ciphertext = """REST TRANSPORT YOU GODWIN VILLAGE
                 ROANOKE WITH ARE YOUR IS JUST SUPPLIES FREE SNOW
                 HEADING TO GONE TO SOUTH FILLER"""
    print(f'Hacking: {ciphertext}\n')
    hack_route(ciphertext, 4)


if __name__ == '__main__':
    main()
