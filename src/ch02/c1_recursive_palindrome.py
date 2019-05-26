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


def main():
    """Demonstrate the recursive palindrome tester."""
    print('I\'m a recursive palindrome tester.\n'
          'I basically call on myself repeatedly to check if a string is a '
          'palindrome.\n'
          'Incidentally, my favorite food is Random Access Memory.\n')
    palindrome = 'rotor'
    print(f'Analyzing: {palindrome}\n')

    if recursive_ispalindrome(palindrome):
        print(f'I do declare that "{palindrome}" is a palindrome!')
    else:
        print(f'I\'m afraid that "{palindrome}" isn\'t a palindrome 😞')


if __name__ == '__main__':
    main()
