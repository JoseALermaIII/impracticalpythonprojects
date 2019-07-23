"""Identify letter transposition or substitution cipher."""
from collections import Counter


def is_transposition(ciphertext: str, threshold: float) -> bool:
    """Identify letter transposition cipher.

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
    return False


def main():
    """Demonstrate the cipher identifier."""


if __name__ == '__main__':
    main()
