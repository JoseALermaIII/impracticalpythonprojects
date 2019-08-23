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

    """


def main():
    """Demonstrate null cipher decoder."""


if __name__ == '__main__':
    main()
