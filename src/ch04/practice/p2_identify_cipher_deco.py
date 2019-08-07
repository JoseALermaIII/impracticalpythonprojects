# pylint: disable=unused-argument
"""Identify letter transposition or substitution cipher using decorator.

Note:
    **Not** part of the book, I was just curious about decorators and decided
    to tinker with them a bit.

"""
from functools import wraps
from src.ch04.practice.p2_identify_cipher import identify_cipher, main


def identify(threshold: float = 0.5):
    """Make decorator for identify_cipher.

    Decorator factory to replace a decorated function with
    :func:`~src.ch04.practice.p2_identify_cipher.identify_cipher`. A bit like
    going around the world to reach the teleporter across the street, but at
    import time instead of runtime, so it doesn't matter.

    Luciano Ramalho's book *Fluent Python* appropriately calls decorators
    "syntactic sugar" when it isn't used in classes. It also references the
    ``wrapt`` module's `blog on GitHub`_ for a deeper explanation of
    decorators.

    Not sure what a decorator factory would be called...syntactic caramel?

    Args:
        threshold (float): Percent match in decimal form.

    Returns:
        Whatever the output of :func:`identify_cipher` would be given the
        decorated function's input.

    .. _blog on GitHub:
        https://github.com/GrahamDumpleton/wrapt/tree/develop/blog

    """
    def decorator(func):
        """Decorate function with identify_cipher."""
        @wraps(func)  # Copy name and docstring of func.
        def _wrapper(ciphertext: str) -> bool:
            if threshold < 0.5:
                # If identifying substitution cipher, apply threshold of 0.45
                # and invert output.
                return not identify_cipher(ciphertext, threshold)
            # If identifying transposition cipher, apply threshold of 0.75
            return identify_cipher(ciphertext, threshold)
        return _wrapper
    return decorator


@identify(threshold=0.75)
def is_transposition(ciphertext: str) -> bool:
    """Identify letter transposition cipher.

    Empty function to wrap with
    :func:`~src.ch04.practice.p2_identify_cipher.identify_cipher` using
    :func:`identify`. **threshold** defaults to ``0.75``.

    Args:
        ciphertext (str): Encrypted message to identify.

    Returns:
        :py:obj:`True` if the **ciphertext** is a letter transposition cipher.
        :py:obj:`False` otherwise.

    """


@identify(threshold=0.45)
def is_substitution(ciphertext: str) -> bool:
    """Identify letter substitution cipher.

    Empty function to wrap with
    :func:`~src.ch04.practice.p2_identify_cipher.identify_cipher` using
    :func:`identify`. **threshold** defaults to ``0.45``.

    Args:
        ciphertext (str): Encrypted message to identify.

    Returns:
        :py:obj:`True` if the **ciphertext** is a letter substitution cipher.
        :py:obj:`False` otherwise.

    """


if __name__ == '__main__':
    main()
