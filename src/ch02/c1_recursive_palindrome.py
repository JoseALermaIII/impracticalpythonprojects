"""Recursively determine if a word is a palindrome."""
from src.ch02 import RECURSIVE_ISPALINDROME_ERROR


def recursive_ispalindrome(word: str) -> bool:
    """Recursively check if a word is a palindrome.

    Args:
        word (str): String to check palindrome-ness.

    Returns:
        :py:obj:`True` if the word is a palindrome, :py:obj:`False` otherwise.

    Raises:
        TypeError: If **word** is not a string.

    """
    if not isinstance(word, str):
        raise TypeError(RECURSIVE_ISPALINDROME_ERROR)

    # Base case: if no letters or one letter, return True.
    if len(word) <= 1:
        return True

    # Recursive loop: if first and last letters are different, return False.
    # Otherwise, remove the first and last letters and call function again.
    if word[0] == word[-1]:
        return recursive_ispalindrome(word[1:-1])
    return False


def main(word: str = None) -> None:
    """Demonstrate the recursive palindrome tester.

    This is only supposed to be a demo, but coverage necessitates
    excessiveness.

    Args:
        word (str): Word to test if it is a palindrome.

    Returns:
        :py:obj:`None`. Identifies **word** as a palindrome.

    """
    print('I\'m a recursive palindrome tester.\n'
          'I basically call on myself repeatedly to check if a string is a '
          'palindrome.\n'
          'Incidentally, my favorite food is Random Access Memory.\n')
    if word is None:
        word = 'rotor'
    print(f'Analyzing: {word}\n')

    if recursive_ispalindrome(word):
        print(f'I do declare that "{word}" is a palindrome!\n')
    else:
        print(f'I\'m afraid that "{word}" isn\'t a palindrome 😞')


if __name__ == '__main__':
    main()
