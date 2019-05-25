"""Recursively determine if a word is a palindrome."""
from src.ch02 import RECURSIVE_ISPALINDROME_ERROR


def recursive_ispalindrome(word: str) -> bool:
    """Recursively check if a word is a palindrome.

    Args:
        word (str): String to check palindrome-ness.

    Returns:
        :py:obj:`True` is the word is a palindrome, :py:obj:`False` otherwise.

    Raises:
        TypeError: If **word** is not a string.

    """
    if not isinstance(word, str):
        raise TypeError(RECURSIVE_ISPALINDROME_ERROR)

    # Base case: if no letters or one letter, return True.

    # Recursive loop: if first and last letters are different, return False.
    # Otherwise, remove the first and last letters and call function again.


def main():
    """Demonstrate the recursive palindrome tester."""
    print('I\'m a recursive palindrome tester.\n'
          'I basically call on myself repeatedly to check if a string is a'
          'palindrome.\n'
          'Incidentally, my favorite food is Random Access Memory.\n')


if __name__ == '__main__':
    main()
