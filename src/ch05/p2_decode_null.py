"""Decode plaintext message from null cipher."""
from src.ch04.challenge.c1_encode_route import format_plaintext


def decode_null(place: int, ciphertext: str) -> str:
    """Decode message from null cipher.

    For every **place** word in **ciphertext**, generate a string using each
    **place** letter.

    Args:
        place (int): Which letter of every other word to form a string.
        ciphertext (str): String with null cipher encoded message. Spaces
            and punctuation are okay, but will be removed. Uppercase
            converted to lowercase.

    Returns:
        String containing **place** letter of every **place** word in
        **ciphertext**.

    Example:
        >>> from src.ch05.p2_decode_null import decode_null
        >>> ciphertext = 'national aeronautics space administration'
        >>> decode_null(1, ciphertext)
        'nasa'

    """
    plaintext = []
    clean_text = format_plaintext(ciphertext)
    for i, word in enumerate(clean_text):
        if i % place == 0:
            plaintext.append(word[place - 1])
    return ''.join(plaintext)


def main():
    """Demonstrate null cipher decoder."""


if __name__ == '__main__':
    main()
