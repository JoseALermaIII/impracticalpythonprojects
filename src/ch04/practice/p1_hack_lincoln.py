"""Hack route cipher sent by Abraham Lincoln."""
from itertools import permutations


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
    return list(set(result))  # Eliminate perfect squares


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
    perms = set(permutations([-1, 1] * length, length))  # Remove repeats
    for perm in perms:
        result.append([sign * key for sign, key in zip(perm, master_key)])
    return result


def main():
    """Demonstrate hack of Lincoln's route cipher."""
    ciphertext = """THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT
    WHY AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEM CAN 
    UP"""
