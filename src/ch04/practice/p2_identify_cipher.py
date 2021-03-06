"""Identify letter transposition or substitution cipher."""
from collections import Counter


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


def is_transposition(ciphertext: str) -> bool:
    """Identify letter transposition cipher.

    Wrapper for :func:`identify_cipher`. **threshold** defaults to ``0.75``.

    Args:
        ciphertext (str): Encrypted message to identify.

    Returns:
        :py:obj:`True` if the **ciphertext** is a letter transposition cipher.
        :py:obj:`False` otherwise.

    """
    return identify_cipher(ciphertext, 0.75)


def is_substitution(ciphertext: str) -> bool:
    """Identify letter substitution cipher.

    Wrapper for :func:`identify_cipher`. **threshold** defaults to ``0.45``.

    Args:
        ciphertext (str): Encrypted message to identify.

    Returns:
        :py:obj:`True` if the **ciphertext** is a letter substitution cipher.
        :py:obj:`False` otherwise.

    """
    return not identify_cipher(ciphertext, 0.45)


def main(ciphertext: str = None) -> None:
    """Demonstrate the cipher identifier.

    This is only supposed to be a demo, but coverage necessitates
    excessiveness.

    Args:
        ciphertext (str): Encrypted letter transposition or letter
            substitution cipher to demonstrate.

    Returns:
        :py:obj:`None`. Identifies **ciphertext**'s cipher.

    """
    print('I can tell the difference between a letter transposition cipher '
          'and a letter\nsubstitution cipher - like those used in decoder '
          'rings. Sorry-not-sorry that\nyou collected all those box tops.\n')

    if ciphertext is None:
        # Used key of XCTJYGPIUWMQBDESOLKZNHFRVA in Al Sweigart's
        # Cracking Codes with Python simpleSubCipher.py
        ciphertext = 'ziy yxpqy ixk qxdjyj cnz ziy dykz uk ybszv'

    print(f'Testing cipher: {ciphertext}\n')

    if is_substitution(ciphertext):
        print('I hereby decree that this is a pitiable attempt at a '
              'substitution cipher.\n')
    else:
        print('Hmm, I declare this is a pathetic attempt at a transposition '
              'cipher.\n')


if __name__ == '__main__':
    main()
