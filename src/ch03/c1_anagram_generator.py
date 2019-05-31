"""Generate phrase anagrams from a word or phrase."""
from collections import defaultdict
from string import ascii_lowercase


def get_primes(n: int = 26, max_prime: int = 101) -> list:
    """Get list of primes.

    Given a number and maximum prime number, return a list of prime numbers.

    Args:
        n (int): Number of prime numbers to return. Defaults to ``26``.
        max_prime (int): Largest prime number to return. Defaults to ``101``.

    Returns:
        :py:obj:`list` of **n** prime numbers with **max_prime** as the
        largest prime number in the list.

    """
    primes = [2]
    while len(primes) <= n:
        # Skip 2 and iterate over odd numbers.
        for num in range(3, max_prime + 1, 2):
            #  If num can't be divided by all odd numbers from 3 to sqrt(num),
            #  it's a prime.
            if all(num % i != 0 for i in range(3, int(num**.5) + 1, 2)):
                primes.append(num)
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
