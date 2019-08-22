"""Encode a message in a list using a null cipher."""
import os
from src.ch01.challenge.c2_name_generator import build_name_list, split_names
from src.ch04.challenge.c1_encode_route import format_plaintext


def encode_null(message: str, word_list: list) -> list:
    """Encode plaintext message with null cipher.

    Embed **message** in a list of words using **word_list**. Use second
    letter in first word of cipherlist, then third letter in second word of
    cipherlist, and repeat until **message** is embedded in cipherlist.

    Args:
        message (str): Message to encrypt with null cipher. Spaces and
            punctuation are okay, but will be removed. Uppercase converted
            to lowercase.
        word_list (list): List of words to build cipherlist. The
             more the merrier.

    Returns:
        List of words with **message** embedded as described. Context
        is *not* provided.

    Raises:
        ValueError: if the list of names doesn't have a name with the needed
            letter.

    """
    message = ''.join(format_plaintext(message))
    cipherlist = []
    for letter in message:
        for word in word_list:
            if all([len(word) > 2, word not in cipherlist]):
                # Even numbered word, use second letter.
                if len(cipherlist) % 2 == 0 and \
                        word[1].lower() == letter:
                    cipherlist.append(word)
                    break
                # Odd numbered word, use third letter.
                elif len(cipherlist) % 2 != 0 and \
                        word[2].lower() == letter:
                    cipherlist.append(word)
                    break
            if word == word_list[-1]:
                if len(cipherlist) % 2 == 0:
                    place = 'second'
                else:
                    place = 'third'
                raise ValueError(f'Missing word with {place} letter of: '
                                 f'{letter}')
    return cipherlist


def main():
    """Demonstrate null cipher encoder.

    Encode a message in a list of last names. First last name in list
    isn't used and some unused last names are added near the beginning
    of the list.

    Tip:
        The website `bestwordlist.com`_ helped with the missing names.

    .. _bestwordlist.com: https://www.bestwordlist.com

    """
    message = 'Say the word and we riot'
    # Build last names from Chapter 1 name generator.
    folder = os.path.abspath('../../src/ch01/challenge/c2files/')
    last_names = split_names(build_name_list(folder))['last']
    # Add missing names for message.
    last_names.extend(['Asher', 'Dwiles', 'Stone'])
    # Insert unused last names near beginning of cipherlist.
    cipherlist = encode_null(message, last_names)
    for name in last_names:
        if name not in cipherlist:
            cipherlist.insert(0, name)
            break
    cipherlist.insert(4, 'Scrooge')
    cipherlist.insert(7, 'Nero')

    # Output encrypted message with context.
    print('Hi Mom,\n\nPlease send me stamps, labels, and stationery to write '
          'thank you cards for the\nfollowing families:\n')
    print(*cipherlist, sep='\n')
    print('\nThanks so much for everything.\n\nLuv ya\' lots,\n\nJohn Doe')


if __name__ == '__main__':
    main()
