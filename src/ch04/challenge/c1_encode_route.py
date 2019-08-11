"""Encode a route cipher and replace code words."""
from string import punctuation
from random import choice
from src.ch02.p1_cleanup_dictionary import cleanup_dict, DICTIONARY_FILE_PATH
from src.ch04.practice.p1_hack_lincoln import get_factors, split


def format_plaintext(plaintext: str) -> list:
    """Format plaintext message for encoding.

    Prepare **plaintext** for route cipher encoding. Convert to lowercase,
    remove punctuation.

    Args:
        plaintext (str): Plaintext message to format.

    Returns:
        List of strings of each word in plaintext message.

    """
    if not plaintext.islower():
        plaintext = plaintext.lower()
    for mark in punctuation:
        if mark in plaintext:
            plaintext = plaintext.replace(mark, '')
    return plaintext.split()


def replace_words(plainlist: list) -> list:
    """Replace sensitive words with code words.

    Replace words that shouldn't be transmitted with code words.

    Args:
        plainlist (list): List of strings of each word in plaintext message.

    Returns:
        Same list, but with sensitive words replaced with code words.

    """
    code_words = {'batteries': 'hounds', 'vicksburg': 'odor',
                  'april': 'clayton', '16': 'sweet', 'grand': 'tree',
                  'gulf': 'owl', 'forts': 'bailey', 'river': 'hickory',
                  '25': 'multiply', '29': 'add', 'admiral': 'hermes',
                  'porter': 'langford'}
    for word in code_words:
        while word in plainlist:
            index = plainlist.index(word)
            plainlist.insert(index, code_words[word])
            plainlist.remove(word)
    return plainlist


def fill_dummy(plainlist: list, factors: list,
               dummy_words: list = None) -> list:
    """Fill a plainlist with dummy words.

    Adds pseudorandom dummy words to the end until the factors of the length of
    **plainlist** includes **factors**.

    Args:
        plainlist (list): List of words of plaintext message.
        factors (list): List of integers that must be factors of the length of
            **plainlist**.
        dummy_words (list): List of dummy words to use as filler. If not
            provided, defaults to :const:`~src.ch02.DICTIONARY_FILE_PATH`
            using :func:`~src.ch02.p1_cleanup_dictionary.cleanup_dict`.

    Returns:
        Same list as **plainlist**, but with dummy words added.

    """
    if dummy_words is None:
        dummy_words = cleanup_dict(DICTIONARY_FILE_PATH)
    for factor in factors:
        while factor not in get_factors(len(plainlist)):
            plainlist.append(choice(dummy_words).lower())
    return plainlist


def encode_route(plaintext: str, keys: list, rows: int) -> list:
    """Encode plaintext message with route cipher.

    Clean **plaintext** with :func:`format_plaintext`, replace sensitive
    intel with :func:`replace_words`, fill with dummy words using
    :func:`fill_dummy` until **keys** and **rows** are factors, then encrypt
    with a route cipher using **keys**.

    Args:
        plaintext (str): Plaintext message to encode with route cipher.
        keys (list): List of positive/negative integers representing cipher
            route.
        rows (int): Number of rows to use in the route cipher table.

    Returns:
        List of strings of transposed words.

    Note:
        Assumes vertical encoding routes.

    """
    # Prep plaintext message.
    plainlist = replace_words(format_plaintext(plaintext))
    # Add dummy words until message length is divisible evenly.
    plainlist = fill_dummy(plainlist, [len(keys), rows])
    split_list = split(plainlist, rows)
    # Build translation table.
    #  Convert rows to columns in new list of lists.
    table = list(map(list, zip(*split_list)))
    # For each column in the table, follow the route, per the key.
    message = []
    for key in keys:
        if key < 0:
            # If negative, reverse direction
            table[abs(key) - 1].reverse()
        message.extend(table[abs(key) - 1])
    return message


def main():
    """Demonstrate the route cipher encoder."""
    print('There are two others that can hack a route cipher, but I\'m the '
          'only one\nthat can encode a route cipher.\nI can even '
          'automatically replace sensitive intel with code words and fill '
          'extra\nrows with dummy words.\n\nI bet I can encode a cipher the '
          'other two can\'t hack. ;-)\n')
    plaintext = """We will run the batteries at Vicksburg the night of April
        16 and proceed to Grand Gulf where we will reduce the
        forts. Be prepared to cross the river on April 25 or
        29. Admiral Porter."""
    key = [-1, 3, -2, 6, 5, -4]
    print(f'Encoding: {plaintext}\nWith key: {key} and using 7 rows.\n')
    print('Encrypted message:')
    print(' '.join(encode_route(plaintext, key, 7)))


if __name__ == '__main__':
    main()
