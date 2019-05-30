"""Counts the occurrence of all possible digrams of a word in a dictionary."""
from itertools import permutations
from collections import Counter
from src.ch01.practice.p2_poor_bar_chart import print_bar_chart
from src.ch02.p1_cleanup_dictionary import read_from_file
from src.ch02 import DICTIONARY_FILE_PATH
from src.ch03 import GET_DIGRAMS_ERROR, COUNT_DIGRAMS_ERROR


def get_digrams(word: str) -> set:
    """Get a set of digrams given a word.

    Generate all possible digrams of a given word.

    Args:
        word (str): String to get digrams of.

    Returns:
        Set of all possible digrams of the given word.

    Raises:
        TypeError: If **word** isn't a string.

    """
    if not isinstance(word, str):
        raise TypeError(GET_DIGRAMS_ERROR)
    # Generate all possible permutations of the word.
    # Crawl each permutation by pairs and add to digrams set.


def count_digrams(digrams: set, dict_list: list) -> dict:
    """Count digrams in word dictionary.

    Count frequency of each digram in the set in a word dictionary list.

    Args:
        digrams (set): Set of digrams to count frequency of.
        dict_list (list): Word dictionary list.

    Returns:
        :py:class:`~collections.Counter` with digrams as keys and their
        counts as values.

    Raises:
        TypeError: If **digrams** isn't a set or if **dict_list** isn't a
        list.

    """
    # Initialize Counter with the digram set.
    # Iterate through each digram in the set.
    # For each digram, iterate through dict_list to find the digram.
    # If found, increment counter.


def digram_counter(word: str, dict_file: str = DICTIONARY_FILE_PATH) -> dict:
    """Wrap get_digrams, count_digrams, and read_from_file.

    Send **word** through :func:`get_digrams` to get a set of digrams which
    is then passed through :func:`count_digrams` along with the list made by
    passing **dict_file** through
    :py:func:`~src.ch02.p1_cleanup_dictionary.read_from_file`.

    Args:
        word (str): Word to get digrams of.
        dict_file (str): Path of dictionary file to get a frequency analysis
            of each digram. Defaults to
            :py:const:`~src.ch02.DICTIONARY_FILE_PATH`.

    Returns:
        :py:class:`~collections.Counter` with digrams as keys and their
        counts as values.

    """
    return count_digrams(get_digrams(word), read_from_file(dict_file))


def main():
    """Demonstrate the digram counter."""
    print('I\'m a digram counter.\nIf you don\'t know what I can be used '
          'for, then you don\'t need me.\nSeriously, though, I can be used '
          'for cryptographic frequency analysis, which probably makes even '
          'less sense...\n')
    word = 'volvo'
    print(f'Analyzing: {word}\n')
    print_bar_chart(digram_counter(word))


if __name__ == '__main__':
    main()
