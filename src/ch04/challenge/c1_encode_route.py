"""Encode a route cipher and replace code words."""
from src.ch04.practice.p3_get_keys import key_to_dict


def format_plaintext(plaintext: str) -> list:
    """Format plaintext message for encoding.

    Prepare **plaintext** for route cipher encoding. Convert to lowercase,
    remove punctuation.

    Args:
        plaintext (str): Plaintext message to format.

    Returns:
        List of strings of each word in plaintext message.

    """


def replace_words(plainlist: list) -> list:
    """Replace sensitive words with code words.

    Replace words that shouldn't be transmitted with code words.

    Args:
        plainlist (list): List of strings of each word in plaintext message.

    Returns:
        Same list, but with sensitive words replaced with code words.

    """
    CODE_WORDS = {'batteries': 'hounds', 'vicksburg': 'odor',
                  'april': 'clayton', '16': 'sweet', 'grand': 'tree',
                  'gulf': 'owl', 'forts': 'bailey', 'river': 'hickory',
                  '25': 'multiply', '29': 'add', 'admiral': 'hermes',
                  'porter': 'langford'}


def encode_route(plaintext: str, key: dict) -> list:
    """Encode plaintext message with route cipher.

    Clean **plaintext** with :func:`format_plaintext', replace sensitive
    intel with :func:`replace_words`, then encrypt with a route cipher
    using **key**.

    Args:
        plaintext (str): Plaintext message to encode with route cipher.
        key (dict): ``up``/``down`` dictionary with integers as column
            numbers.

    Returns:
        List of strings of transposed words.

    """
    # TODO: Prep plaintext message.

    # TODO: Add dummy words until message length is divisible evenly.

    # TODO: Build translation table.

    # TODO: For each column in the table, copy the relevant row, per the key.


def main():
    """Demonstrate the route cipher encoder."""
    plaintext = """We will run the batteries at Vicksburg the night of April
                    16 and proceed to Grand Gulf where we will reduce the
                    forts. Be prepared to cross the river on April 25 or
                    29. Admiral Porter."""
    key = [-1, 3, -2, 6, 5, -4]


if __name__ == '__main__':
    main()
