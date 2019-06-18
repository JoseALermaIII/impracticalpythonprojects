"""Generate phrase anagrams from a word or phrase."""
from collections import defaultdict
from string import ascii_lowercase
from src.ch02 import DICTIONARY_FILE_PATH
from src.ch02.p1_cleanup_dictionary import read_from_file


def get_primes(length: int = 26, min_prime: int = 2,
               max_prime: int = 101) -> list:
    """Get list of primes.

    Given a number minimum and maximum prime number, return a list of prime
    numbers.

    Args:
        length (int): Number of prime numbers to return. Defaults to ``26``.
        min_prime (int): Smallest prime number to return. Defaults to ``2``.
        max_prime (int): Largest prime number to return. Defaults to ``101``.

    Returns:
        :py:obj:`list` of **n** prime numbers with **min_prime** as the
        smallest prime number and **max_prime** as the largest prime number
        in the list.

    """
    primes = []
    if min_prime <= 3:
        # If min_prime includes ``2``, skip it during calculations.
        min_prime, primes = 3, [2]
    elif min_prime % 2 == 0:
        # If min_prime is even, make exclusive odd.
        min_prime += 1

    while len(primes) < length:
        # Iterate over odd numbers.
        for num in range(min_prime, max_prime + 1, 2):
            #  If num can't be divided by all odd numbers from min_prime to
            #  sqrt(num), it's a prime.
            if all(num % i != 0 for i in range(3, int(num**.5) + 1, 2)):
                primes.append(num)
            if len(primes) == length:
                # Stop as soon as we have enough primes.
                break
    return primes


def get_id(word: str) -> int:
    """Get ID number of word.

    Assign a unique prime number to each letter in
    :py:obj:`~string.ascii_lowercase`. The product of each letter in **word**
    is its ID number.

    Args:
        word (str): Word to get ID of.

    Returns:
        :py:obj:`int` representing ID of **word**.

    """
    # Assign each ASCII lowercase letter a prime number.
    primes = get_primes()
    letter_id = dict(zip(ascii_lowercase, primes))
    # Find the product of each letter in the word.
    product = 1
    for letter in word:
        product *= letter_id[letter]
    return product


def get_anagram_dict(word_list: list) -> dict:
    """Get an anagram dictionary from word_list.

    Get the ID of each word in **word list** and add it to a dictionary with
    the ID as the key.

    Args:
        word_list (list): List of words to make into anagram dictionary.

    Returns:
        :py:class:`~collections.defaultdict` of :py:obj:`list` with an ID
        (:py:obj:`int`) as the key and words whose product of letters equal
        that ID as values.

    """
    anagram_dict = defaultdict(list)
    # Find the product of each letter for each word in a dictionary.
    for word in word_list:
        anagram_dict[get_id(word)].append(word)
    return anagram_dict


def find_anagrams(word: str, anagram_dict: dict) -> list:
    """Find anagrams in word.

    Find all anagrams in a given word (or phrase) using anagram dictionary.

    Args:
        word (str): Word to find anagrams of.
        anagram_dict: Dictionary from :func:`get_anagram_dict`.

    Returns:
        :py:obj:`list` of :py:obj:`str` with all anagrams in **word**.

    """
    if not word.islower():
        word = word.lower()
    if ' ' in word:
        # If word is a phrase with spaces, remove spaces.
        word = ''.join(word.split())
    anagrams = []
    id_num = get_id(word)
    keys = list(anagram_dict.keys())  # Make keys indexable. Python3.6 only?
    # If an anagram is IN the word, the modulo of the anagram's ID and the
    # word's ID will be 0.
    for key in keys:
        if id_num % key == 0:
            anagrams.extend(anagram_dict[key])
    # Remove duplicate
    if word in anagrams:
        anagrams.remove(word)
    return sorted(anagrams)


def anagram_generator(word: str) -> list:
    """Generate phrase anagrams.

    Make phrase anagrams from a given word or phrase.

    Args:
        word (str): Word to get phrase anagrams of.

    Returns:
        :py:obj:`list` of phrase anagrams of **word**.

    """
    # Given a word, build a list of anagrams.
    # For each anagram in the list, build a phrase anagram by getting the
    # anagram's anagrams.
    pass


def main():
    """Demonstrate the Anagram Generator."""
    print('I can find all phrase anagrams given a word or phrase.\n'
          'I\'m fun at parties.')
    # Print first 500 results.


if __name__ == '__main__':
    main()
