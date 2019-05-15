"""Generate random names from a list of names."""
import os
import random
from src.ch01.challenge import SPLIT_FROM_FILE_ERROR


def split_names_from_file(filepath: str) -> dict:
    """Split names from file.

    Splits first, middle, and last names from a given file.

    Args:
        filepath (str): Path to file with names.

    Returns:
        Dictionary of lists with ``first``, ``middle``, and ``last`` as keys
        and names as values.

    Raises:
        EOFError: If given file is empty.

    Note:
        Drops suffix and adds nickname to middle names.

    """
    # Read lines from file and remove trailing whitespaces.
    with open(filepath, 'r') as file:
        file_data = [line.rstrip() for line in file]
    if not file_data:
        raise EOFError(SPLIT_FROM_FILE_ERROR)

    # TODO: Raise error if empty file.

    # TODO: Check for quotes for nicknames and add to middle names.

    # TODO: Check middle name by counting whitespace and add to middle names.

    # TODO: Check for repeat middle names while adding.

    # TODO: Drop suffix by dropping last name if less than 4 characters,
    #  has a '.', or all uppercase.

    # TODO: Split and add first and last names.

    # TODO: Check for repeat first and last times while adding.


def generate_name(name_dict: dict) -> str:
    """Generate pseudo-random name.

    Use names in given dictionary to generate a random name.

    Args:
        name_dict: Dictionary from split_names_from_file.

    Returns:
        String with a random name.

    Note:
        Only add middle name between 1/3 and 1/4 of the time.

    """
    # TODO: Raise error if 'first', 'middle', and 'last' aren't keys.

    # TODO: Add middle name between 1/3 and 1/4 of the time.


def main():
    """Demonstrate name generator."""
    print('This is a random name generator.\n'
          'Similar to a certain American detective comedy-drama television\n'
          'series.')


if __name__ == '__main__':
    main()
