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
    top = plaintext[::4]
    middle = plaintext[1::2]
    bottom = plaintext[2::4]
    return top + middle + bottom


def encode_rail(plaintext: str, split: int = 5) -> str:
    """Encode rail fence cipher.

    Encode **plaintext** with a 3-rail fence cipher. Scrub the plaintext with
    :func:`~src.ch04.challenge.c1_encode_route.format_plaintext`, then encrypt
    it with :func:`split_rails`.

    Args:
        plaintext (str): Message to encrypt with 3-rail fence cipher.
        split (int): How many letter segments to split message into. Defaults
            to ``5``.

    Returns:
        String with encrypted message split into **split** chunks for easier
        transmission.

    """
    ciphertext = split_rails(''.join(format_plaintext(plaintext)))
    return ' '.join(ciphertext[i:i + split] for i in
                    range(0, len(ciphertext), split))


def main():
    """Demonstrate 3-rail fence cipher encoder."""
    print('I can encode a message using a 3-rail fence cipher. Don\'t get '
          'too\nexcited - it\'s trivial to brute-force; however, one can '
          'dream... one\ncan dream...')

    message = ('There is a fresh batch of cookies in the cereal box above\n'
               'the refrigerator. Keep them away from Debbie!')
    print(f'\nEncoding:\n{message}')
    print(f'\nEncrypted message:\n{encode_rail(message, 6)}')


if __name__ == '__main__':
    main()
