"""Generate phrase anagrams from a word or phrase."""


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
