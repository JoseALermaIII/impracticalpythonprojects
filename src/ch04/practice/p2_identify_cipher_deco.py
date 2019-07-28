# pylint: disable=all
"""Identify letter transposition or substitution cipher using decorator.

Note:
    **Not** part of the book, I was just curious about decorators and decided
    to tinker with them a bit.

"""
from collections import Counter
from functools import wraps


def identify_cipher(ciphertext: str, threshold: float) -> bool:
    """Identify letter transposition or substitution cipher.

    Compare most frequent letters in **ciphertext** with the most frequent
    letters in the English alphabet. If above **threshold**, it is a letter
    transposition cipher. If not, it is a letter substitution cipher.

    Args:
        ciphertext (str): Encrypted message to identify.
        threshold (float): Percent match in decimal form.

    Returns:
        :py:obj:`True` if the **ciphertext** is a letter transposition cipher.
        :py:obj:`False` otherwise.

    """
    most_freq = 'etaoinshrdlu'
    # Convert most frequent English letters into a Counter.
    english_freq = Counter(most_freq)
    # Identify most frequent letters in ciphertext and convert into Counter.
    ciphertext_freq = Counter([i[0] for i in
                               Counter(ciphertext.replace(' ', ''))
                               .most_common(len(most_freq))])
    # Find letters that they have in common.
    intersection = english_freq & ciphertext_freq
    # Count letters they had in common.
    count = len(intersection.keys())

    if count / len(most_freq) >= threshold:
        return True
    return False


def _identify_cipher(func):
    """Decorate function with identify_cipher.

    Replaces decorated function, **func**, with :func:`identify_cipher`. A
    bit like going around the world to cross the street, but at import time
    instead of runtime, so it doesn't matter.

    Luciano Ramalho's book *Fluent Python* appropriately calls decorators
    "syntactic sugar" when it isn't used in classes. It also references the
    ``wrapt`` module's `blog on GitHub`_ for a deeper explanation of
    decorators.

    Args:
        func (function): Function to replace with :func:`identify_cipher`.

    Returns:
        Whatever the output of :func:`identify_cipher` would be given the
        decorated function's input.

    Warning:
        Not intended to be used outside this module.

    .. _blog on GitHub:
        https://github.com/GrahamDumpleton/wrapt/tree/develop/blog

    """
    @wraps(func)  # Copy name and docstring of func.
    def _wrapper(ciphertext: str) -> bool:
        if func.__name__ == 'is_substitution':
            # If identifying substitution cipher, apply threshold of 0.45
            # and invert output.
            return not identify_cipher(ciphertext, 0.45)
        # If identifying transposition cipher, apply threshold of 0.75
        return identify_cipher(ciphertext, 0.75)
    return _wrapper


@_identify_cipher
def is_transposition(ciphertext: str) -> bool:
    """Identify letter transposition cipher.

    Empty function to wrap with :func:`identify_cipher` using
    :func:`_identify_cipher`. **threshold** defaults to ``0.75``.

    Args:
        ciphertext (str): Encrypted message to identify.

    Returns:
        :py:obj:`True` if the **ciphertext** is a letter transposition cipher.
        :py:obj:`False` otherwise.

    """


@_identify_cipher
def is_substitution(ciphertext: str) -> bool:
    """Identify letter substitution cipher.

    Empty function to wrap with :func:`identify_cipher` using
    :func:`_identify_cipher`. **threshold** defaults to ``0.45``.

    Args:
        ciphertext (str): Encrypted message to identify.

    Returns:
        :py:obj:`True` if the **ciphertext** is a letter substitution cipher.
        :py:obj:`False` otherwise.

    """


def main():
    """Demonstrate the cipher identifier."""
    print('I can tell the difference between a letter transposition cipher '
          'and a letter\nsubstitution cipher - like those used in decoder '
          'rings. Sorry-not-sorry that\nyou collected all those box tops.\n')

    # Used key of XCTJYGPIUWMQBDESOLKZNHFRVA in Al Sweigart's
    # Cracking Codes with Python simpleSubCipher.py
    ciphertext = 'ziy yxpqy ixk qxdjyj cnz ziy dykz uk ybszv'
    print(f'Testing cipher: {ciphertext}\n')

    if is_substitution(ciphertext):
        print('I hereby decree that this is a pitiable attempt at a '
              'substitution cipher.\n')
    else:
        print('No idea what this is - must be a user error.\n')


if __name__ == '__main__':
    main()
