"""Encode message with a 3-rail fence cipher."""
from src.ch04.challenge.c1_encode_route import format_plaintext


def split_rails(plaintext: str) -> str:
    """Split plaintext into 3 rails for encryption.

     Split the rails where the top rail is every 4th letter, the middle rail
     is every other letter starting at 1, and the bottom rail is every 4th
     letter starting at 2. After splitting, concatenate each rail and
     return the result.

    Args:
        plaintext (str): Plain text message without spaces or punctuation.

    Returns:
        String with message encrypted using 3 rail fence cipher.

    """


def encode_rail(plaintext: str) -> str:
    """Encode rail fence cipher.

    Encode **plaintext** with a 3-rail fence cipher. Scrub the plaintext with
    :func:`~src.ch04.challenge.c1_encode_route.format_plaintext`, then encrypt
    it with :func:`split_rails`.

    Args:
        plaintext: Message to encrypt with 3-rail fence cipher.

    Returns:
        String of 5-letter chunks of encrypted message for easier
        transmission.

    """


def main():
    """Demonstrate 3-rail fence cipher encoder."""


if __name__ == '__main__':
    main()
