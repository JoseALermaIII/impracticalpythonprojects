"""Encode a message in a list using a null cipher."""
import os
from src.ch01.challenge.c2_name_generator import build_name_list, split_names
from src.ch04.challenge.c1_encode_route import format_plaintext


def encode_null(message: str, name_list: list) -> list:
    """Encode plaintext message with null cipher.

    Embed **message** in a list of last names using **name_list**. First name
    in cipherlist shouldn't be used, then use second letter in second name of
    cipherlist, then third letter in third name of cipherlist, and repeat
    until **message** is embedded in cipherlist. Lastly, insert two unused
    last names near the start of the list.

    Args:
        message (str): Message to encrypt with null cipher. Spaces and
            punctuation are okay, but will be removed.
        name_list (list): List of last names to build cipherlist. The
             more the merrier.

    Returns:
        List of last names with **message** embedded as described. Context
        is *not* provided.

    """


def main():
    """Demonstrate null cipher encoder."""
    message = 'Say the word and we riot'
    folder = os.path.abspath('src/ch01/challenge/c2files')


if __name__ == '__main__':
    main()
