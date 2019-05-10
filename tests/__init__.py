"""Test impractical python projects.

Attributes:
    RANDOM_STRING_ERROR (str): Error message for random_string function.

"""
import string
import random

# Constants
RANDOM_STRING_ERROR = 'Length must be an integer and characters must be a string.'

# Helper functions


def random_string(length: int = 10, characters: str = string.ascii_letters) -> str:
    """Generate random string.

    Generates a pseudo-random string of given length with given characters.

    Args:
        length (int): Length of random string to make. Defaults to ``10``.
        characters (str): String with letters to choose from.
            Defaults to ASCII uppercase and lowercase.

    Returns:
        String with random letters.

    Raises:
        TypeError: If ``length`` isn't an integer or if ``characters`` isn't
            a string.

    """
    if not all([isinstance(length, int), isinstance(characters, str)]):
        raise TypeError(RANDOM_STRING_ERROR)

    return ''.join(random.choice(characters) for _ in range(length))
