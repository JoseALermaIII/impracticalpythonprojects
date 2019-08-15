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
    message = ''.join(format_plaintext(message))
    cipherlist = []
    for letter in message:
        for name in name_list:
            if all([len(name) > 2, name not in cipherlist]):
                # Even numbered name, use second letter.
                if len(cipherlist) % 2 == 0 and \
                        name[1].lower() == letter:
                    cipherlist.append(name)
                    break
                # Odd numbered name, use third letter.
                elif len(cipherlist) % 2 != 0 and \
                        name[2].lower() == letter:
                    cipherlist.append(name)
                    break
            if name == name_list[-1]:
                if len(cipherlist) % 2 == 0:
                    place = 'second'
                else:
                    place = 'third'
                raise IndexError(f'Missing name with {place} letter of: '
                                 f'{letter}')
    # Insert unused last names near beginning of list.
    cipherlist.insert(0, name_list[0])
    cipherlist.insert(4, 'Scrooge')
    cipherlist.insert(7, 'Nero')
    return cipherlist


def main():
    """Demonstrate null cipher encoder."""
    message = 'Say the word and we riot'
    folder = os.path.abspath('src/ch01/challenge/c2files')


if __name__ == '__main__':
    main()
