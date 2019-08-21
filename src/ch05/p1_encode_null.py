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

    Raises:
        ValueError: if the list of names doesn't have a name with the needed
            letter.

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
                raise ValueError(f'Missing name with {place} letter of: '
                                 f'{letter}')
    # Insert unused last names near beginning of list.
    for name in name_list:
        if name not in cipherlist:
            cipherlist.insert(0, name)
            break
    cipherlist.insert(4, 'Scrooge')
    cipherlist.insert(7, 'Nero')
    return cipherlist


def main():
    """Demonstrate null cipher encoder.

    Note:
        The website `bestwordlist.com`_ helped with the missing names.

    .. _bestwordlist.com: https://www.bestwordlist.com

    """
    message = 'Say the word and we riot'
    # Build last names from Chapter 1 name generator.
    folder = os.path.abspath('../../src/ch01/challenge/c2files/')
    last_names = split_names(build_name_list(folder))['last']
    # Add missing names for message.
    last_names.extend(['Asher', 'Dwiles', 'Stone'])
    # Output encrypted message with context.
    print('Hi Mom,\n\nPlease send me stamps, labels, and stationery to write '
          'thank you cards for the\nfollowing families:\n')
    for name in encode_null(message, last_names):
        print(name)
    print('\nThanks so much for everything.\n\nLuv ya\' lots,\n\nJohn Doe')


if __name__ == '__main__':
    main()
