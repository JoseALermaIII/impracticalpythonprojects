"""Generate phrase anagrams from a word or phrase."""
from collections import defaultdict, Counter
from os import cpu_count
from string import ascii_lowercase
from sys import setrecursionlimit
from threading import Thread
from src.ch02 import DICTIONARY_FILE_PATH
from src.ch02.p1_cleanup_dictionary import read_from_file

setrecursionlimit(9000)  # Default is 1000


def get_primes(length: int = 26, min_prime: int = 2,
               max_prime: int = 101) -> list:
    """Get list of primes.

    Given a length, minimum, and maximum prime number, return a list of prime
    numbers.

    Args:
        length (int): Number of prime numbers to return. Defaults to ``26``.
        min_prime (int): Smallest prime number to return. Defaults to ``2``.
        max_prime (int): Largest prime number to return. Defaults to ``101``.

    Returns:
        :py:obj:`list` of **length** prime numbers with **min_prime** as the
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


def split(a_list: list, parts: int) -> list:
    """Split a list into parts.

    Split given list into given number of parts.

    Args:
        a_list (list): List to split.
        parts (int): Number of parts to split list into.

    Returns:
        List of lists with **a_list** split into **parts**.

    Example:
        >>> import src.ch03.c1_anagram_generator.split as split
        >>> some_list = ['this', 'is', 'a', 'list']
        >>> split_list = split(some_list, 2)
        >>> print(split_list)
        [['this', 'is'], ['a', 'list']]

    """
    quotient, remainder = divmod(len(a_list), parts)
    return list((a_list[i * quotient + min(i, remainder):(i + 1) * quotient +
                        min(i + 1, remainder)] for i in range(parts)))


def extend_anagram_dict(word_list: list, dictionary: dict):
    """Extend an anagram dictionary.

    Adds words from given word list to a given anagram dictionary.

    Args:
        word_list (list): List of words to add to anagram dictionary.
        dictionary (dict): Anagram dictionary to add words to.

    Returns:
        None. If words in **word_list** are in **dictionary** they are not
        added. Otherwise, they are added.

    """
    new_anagram_dict = get_anagram_dict(word_list)
    for key, value in new_anagram_dict.items():
        for element in value:
            if element not in dictionary[key]:
                dictionary[key].extend(value)


def multi_get_anagram_dict(word_list: list) -> dict:
    """Multithreaded get anagram dictionary.

    Uses :py:meth:`os.cpu_count` and :py:class:`threading.Thread` to use
    all CPUs to make an anagram dictionary with the intent of being more
    efficient than :py:func:`~src.ch03.c1_anagram_generator.get_anagram_dict`.

    Args:
        word_list (list): List of words to make into anagram dictionary.

    Returns:
        :py:class:`~collections.defaultdict` of :py:obj:`list` with an ID
        (:py:obj:`int`) as the key and words whose product of letters equal
        that ID as values.

    Warning:
        Avoids race conditions by heavily relying on CPython's
        `Global Interpreter Lock`_. More info about `Thread Objects`_.

    .. _Global Interpreter Lock:
        https://docs.python.org/3/glossary.html#term-global-interpreter-lock
    .. _Thread Objects:
        https://docs.python.org/3/library/threading.html#thread-objects

    """
    super_dict = defaultdict(list)
    divisions = split(word_list, cpu_count())
    threads = []
    for division in divisions:
        thread = Thread(target=extend_anagram_dict, args=(division, super_dict))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    return super_dict


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
    return sorted(anagrams)


def remove_unusable_words(anagram_dict: dict, usable_letters: list) -> dict:
    """Remove unusable words from anagram dictionary.

    Creates new anagram dictionary by including only IDs that can be IN
    **usable_letters**.

    Args:
        anagram_dict (dict): Anagram dictionary to prune.
        usable_letters (list): List of letters that must be used.

    Returns:
        :py:class:`~collections.defaultdict` of :py:obj:`list` with an ID
        (:py:obj:`int`) as the key and words whose product of letters equal
        that ID as values.

    """
    new_word = ''.join(usable_letters)
    new_anagram_dict = defaultdict(list)
    id_num = get_id(new_word)
    keys = list(anagram_dict.keys())  # Make keys indexable. Python3.6 only?
    # If anagram can be IN new_word, add to new_anagram_dict.
    for key in keys:
        if id_num % key == 0:
            new_anagram_dict[key] = anagram_dict[key]
    return new_anagram_dict


def find_anagram_phrases(phrases: list, word: str, anagram_dict: dict, phrase: list) -> None:
    """Find anagram phrases.

    Recursively finds anagram phrases of **word** by removing unusable words
    from the **anagram_dict**, finding remaining anagrams given the
    **phrase**, then adding any found anagram phrases to **phrases**.

    Args:
        phrases (list): List of anagram phrases.
        word (str): Current word to find anagram phrases of.
        anagram_dict (dict): Current anagram dictionary to find anagrams with.
        phrase (list): Current anagram phrase candidate.

    Returns:
        None. **phrases** is updated with any found anagram phrases.

    """
    letters = Counter(word.replace(' ', ''))
    letters.subtract(''.join(phrase))
    letters_left = list(letters.elements())

    new_anagram_dict = remove_unusable_words(anagram_dict, letters_left)
    # Once the length is equal, we have an anagram phrase.
    if len(word.replace(' ', '')) == len(''.join(phrase)):
        if Counter(word.replace(' ', '')) == Counter(''.join(phrase)):
            # Add to phrases
            phrases.append(' '.join(phrase))
        return None
    # Find new anagrams and recurse.
    anagrams = find_anagrams(''.join(letters_left), anagram_dict)
    for anagram in anagrams:
        new_phrase = phrase[:]
        new_phrase.append(anagram)
        find_anagram_phrases(phrases, word, new_anagram_dict, new_phrase)


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
    word = 'see shells'
    print(f'\nAnalyzing: {word}\n')
    anagram_phrases = anagram_generator(word)
    for i in range(len(anagram_phrases)):
        if i > 500:
            break
        print(anagram_phrases[i])


if __name__ == '__main__':
    main()
