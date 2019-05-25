"""Chapter 2.

Attributes:
    DICTIONARY_FILE_PATH (str): String with path to Ubuntu 18.04.2's
        American English dictionary file.

    CLEANUP_LIST_ERROR (str): String with :py:exc:`IndexError` for Cleanup
        Dictionary :func:`~p1_cleanup_dictionary.cleanup_list`.

    RECURSIVE_ISPALINDROME_ERROR (str): String with :py:exc:`TypeError` for
        Recursive Palindrome
        :func:`~c1_recursive_palindrome.recursive_ispalindrome`.

"""

# Constants
DICTIONARY_FILE_PATH = '/usr/share/dict/american-english'
CLEANUP_LIST_ERROR = 'List cannot be empty.'
RECURSIVE_ISPALINDROME_ERROR = 'Word must be a string.'
