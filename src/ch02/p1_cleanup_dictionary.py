"""Cleanup word dictionary.

Various functions for cleaning up a word dictionary.

Attributes:
    APPROVED_WORDS (list): Words that should always appear in a word
        dictionary.

"""
from string import ascii_lowercase
from src.ch01.challenge.c2_name_generator import read_from_file
from src.ch02 import DICTIONARY_FILE_PATH, CLEANUP_LIST_ERROR

APPROVED_WORDS = ['i', 'a', 'me', 'an', 'qi', 'at', 'to', 'as', 'am', 'ad',
                  'be', 'by', 'go', 'he', 'hi', 'if', 'in', 'is', 'it', 'my',
                  'no', 'of', 'oh', 'ox', 'so', 'up', 'us', 'we']


def cleanup_list(word_list: list) -> list:
    """Cleanup word list.

    Remove single letter words from a :py:obj:`list` of words.

    Args:
        word_list (list): List with words as elements.

    Returns:
        List with words as elements excluding single letter words.

    Raises:
        IndexError: If **word_list** is empty.

    """
    if not word_list:
        raise IndexError(CLEANUP_LIST_ERROR)
    return [word for word in word_list if len(word) > 1]


def cleanup_list_more(word_list: list) -> list:
    """Cleanup word list even more.

    First, remove words with apostrophes, double letter words, duplicates,
    and words with letters not in :py:obj:`string.ascii_lowercase` from a
    :py:obj:`list` of words. Then, add :py:const:`APPROVED_WORDS` back into
    list. Finally, sort list.

    Args:
        word_list (list): List with words as elements.

    Returns:
        Sorted list with words as elements excluding cleaned words and
        :py:const:`APPROVED_WORDS` added.

    Raises:
        IndexError: If **word_list** is empty.

    """
    if not word_list:
        raise IndexError(CLEANUP_LIST_ERROR)
    clean_list = []
    for word in word_list:
        if any(["'" in word, len(word) == 2]):
            # Skip words with apostrophes and double letter words.
            continue
        if any([letter not in ascii_lowercase for letter in word.lower()]):
            # Skip words with letters not in ascii_lowercase.
            continue
        clean_list.append(word.lower())
    # Add approved words to list if missing.
    for word in APPROVED_WORDS:
        if word not in clean_list:
            clean_list.append(word)
    # Remove duplicates and sort.
    clean_list = sorted(list(set(clean_list)))
    return clean_list


def cleanup_dict(filepath: str) -> list:
    """Wrap read_from_file and cleanup_list.

    Passes given **filepath** through
    :func:`~src.ch01.challenge.c2_name_generator.read_from_file`
    to get a list of words, then :func:`cleanup_list` to remove single letter
    words.

    Args:
        filepath (str): String with path to word dictionary file.

    Returns:
        List with words as elements excluding single letter words.

    """
    return cleanup_list(read_from_file(filepath))


def main():
    """Demonstrate cleanup dictionary."""
    print('I\'m a word dictionary cleaner.\n'
          'I remove those annoying one letter words.\n')
    word_list = read_from_file(DICTIONARY_FILE_PATH)
    word_list_len = len(word_list)
    clean_word_list = cleanup_dict(DICTIONARY_FILE_PATH)
    clean_word_list_len = len(clean_word_list)
    print(f'Original word list had {word_list_len} words.\n'
          f'Cleaned word list has {clean_word_list_len} words.\n'
          f'I cleaned up {word_list_len - clean_word_list_len} words! '
          f'Yay, me!')


if __name__ == '__main__':
    main()
