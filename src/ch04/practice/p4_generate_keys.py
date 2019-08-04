"""Generate route cipher keys for brute-forcing a route cipher.

Already implemented with :func:`~src.ch04.practice.p1_hack_lincoln.keygen`,
but this version will return a list of tuples.

"""
from itertools import combinations


def generate_keys(length: int) -> list:
    """Generate all possible route cipher keys.

    Generates a list of all possible route cipher keys of **length**.

    Args:
        length (int): Length of route cipher key.

    Returns:
        List of tuples of integers representing all possible route cipher
        keys of **length**.

    """
    result = []
    master_key = range(1, length + 1)
    # Get all possible combinations of direction (pos/neg) of length
    combs = set(combinations([-1, 1] * length, length))  # Remove repeats
    for comb in combs:
        result.append(tuple(sign * key for sign, key in zip(comb, master_key)))
    return result


def main():
    """Demonstrate the key generator."""
    print('Given a key length, I can generate all possible route cipher '
          'keys of that\nlength. I have a lot of free time.\n')
    length = 3
    print(f'Making keys of length: {length}')
    print(generate_keys(length))


if __name__ == '__main__':
    main()
