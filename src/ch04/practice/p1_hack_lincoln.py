"""Hack route cipher sent by Abraham Lincoln."""
from itertools import combinations
from src.ch03.c1_anagram_generator import split


def get_factors(integer: int) -> list:
    """Get factors of integer.

    Calculate factors of a given integer.

    Args:
        integer (int): Number to get factors of.

    Returns:
        List of integer factors of **integer**.

    """
    result = []
    # A factor will always be less than or equal to sqrt(integer).
    for i in range(1, int(integer ** 0.5) + 1):
        if integer % i == 0:
            result.append(i)
            # If you have one factor, the other is integer / factor
            result.append(integer // i)
    return sorted(list(set(result)))  # Eliminate perfect squares


def keygen(length: int) -> list:
    """Generate all possible route cipher keys.

    Generates a list of all possible route cipher keys of **length**.

    Args:
        length (int): Length of route cipher key.

    Returns:
        List of lists of integers representing all possible route cipher keys
        of **length**.

    Example:
        >>> from src.ch04.practice.p1_hack_lincoln import keygen
        >>> keygen(2)
        [[-1, 2], [1, -2], [1, 2], [-1, -2]]

    """
    result = []
    master_key = range(1, length + 1)
    # Get all possible combinations of direction (pos/neg) of length
    combs = set(combinations([-1, 1] * length, length))  # Remove repeats
    for comb in combs:
        result.append([sign * key for sign, key in zip(comb, master_key)])
    return result


def decode_route(keys: list, cipherlist: list) -> list:
    """Decode route cipher.

    Decode **cipherlist** encoded with a route cipher using **keys**.

    Args:
        keys (list): List of signed, integer keys.
        cipherlist (list): List of strings representing encoded message.

    Returns:
        List of strings representing plaintext message.

    Note:
        Assumes vertical encoding route.

    """
    message = []
    split_list = split(cipherlist, len(keys))
    for key in keys:
        if key < 0:
            # If negative, reverse direction
            message.extend(reversed(split_list[0]))
        else:
            message.extend(split_list[0])
        del split_list[0]
    return message


def hack_route(ciphertext: str) -> None:
    """Hack route cipher.

    Hack route cipher by using :func:`get_factors` to find all possible key
    lengths. Then use :func:`keygen` to generate all possible keys and pass
    each one through :func:`decode_route`.

    Args:
        ciphertext (str): Message encoded with route cipher.

    Returns:
        None. Prints all possible decoded messages.

    """
    cipherlist = ciphertext.split()
    # Get all possible key lengths.
    factors = get_factors(len(cipherlist))
    for factor in factors:
        # Get all possible keys.
        if any([factor == 1, factor == len(cipherlist)]):
            # Key length of 1 is the full cipherlist and key length of
            # cipherlist length is one word per column.
            continue
        keys = keygen(factor)
        for key in keys:
            # Use each key to decode route cipher.
            message = ' '.join(decode_route(key, cipherlist))
            print(f'Key: {key}\nDecoded message: {message}\n')


def main():
    """Demonstrate hack of Lincoln's route cipher."""
    print('I can do a brute-force hack of a route cipher sent by '
          'Abraham Lincoln,\nand I do a better job than he did in that dumb '
          'zombie movie.')
    print('\nNote: I only hack the route cipher. I leave the '
          'word-transposition\ncipher to you and your biochemical brain.\n')
    ciphertext = """THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT
    WHY AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEM CAN 
    UP"""
    print(f'Hacking: {ciphertext}\n')
    hack_route(ciphertext)


if __name__ == '__main__':
    main()
