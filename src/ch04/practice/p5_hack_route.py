"""Another way to hack a route cipher.

Already implemented in :py:mod:`~src.ch04.practice.p1_hack_lincoln`, but this
version will use the building blocks made in
:py:mod:`~src.ch04.practice.p2_identify_cipher`,
:py:mod:`~src.ch04.practice.p3_get_keys`, and
:py:mod:`~src.ch04.practice.p4_generate_keys`.

"""
from src.ch04.practice.p2_identify_cipher import is_transposition
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


def main():
    """Demonstrate the route cipher hacker."""
    # Four column route 'cyphertext' from book.
    ciphertext = """REST TRANSPORT YOU GODWIN VILLAGE 
                 ROANOKE WITH ARE YOUR IS JUST SUPPLIES FREE SNOW
                 HEADING TO GONE TO SOUTH FILLER"""


if __name__ == '__main__':
    main()
