"""Generate random names from a list of names."""
import os
import random
from src.ch01.challenge import READ_FROM_FILE_ERROR, SPLIT_NAME_LIST_ERROR, \
    SPLIT_NAME_EMPTY_ERROR


def read_from_file(filepath: str) -> list:
    """Read from file.

    Reads lines from text file and returns a list.

    Args:
        filepath (str): Path to file with names.

    Returns:
        List with each line from the file as an element.

    Raises:
        EOFError: If given file is empty.

    Note:
        Removes leading and trailing whitespaces.

    """
    # Read lines from file and remove trailing whitespaces.
    with open(filepath, 'r') as file:
        file_data = [line.rstrip() for line in file]
    if not file_data:
        raise EOFError(READ_FROM_FILE_ERROR)
    return file_data


def split_names(name_list: list) -> dict:
    """Split names from list of names.

    Splits first, middle, and last names from a given list of names.

    Args:
        name_list (list): List with names as elements.

    Returns:
        Dictionary of lists with ``first``, ``middle``, and ``last`` as keys
        and names as values.

    Raises:
        TypeError: If given name list is not a list or tuple.
        ValueError: If given name list is empty.

    Note:
        Drops suffix and adds nickname to middle names.

    """
    if not any([isinstance(name_list, list), isinstance(name_list, tuple)]):
        raise TypeError(SPLIT_NAME_LIST_ERROR)
    if not name_list:
        raise ValueError(SPLIT_NAME_EMPTY_ERROR)

    names = {'first': [], 'middle': [], 'last': []}
    for name in name_list:
        # Check for quotes for nicknames and add to middle names.
        if '"' in name:
            start = name.find('"')
            end = name.find('"', start + 1)
            nickname = name[start:end + 2]  # Include space for replace
            names['middle'].append(nickname.strip())
            name = name.replace(nickname, '')

        # Drop suffix by dropping last name if less than 4 characters, has
        # a '.', or all uppercase.
        end = name.rfind(' ')
        suffix = name[end:]  # Include space for replace
        if len(suffix.strip()) < 4 and any(['.' in suffix, suffix.isupper()]):
            name = name.replace(suffix, '')

        # TODO: Check middle name by counting whitespace and add to middle names.

        # TODO: Check for repeat middle names while adding.

        # TODO: Split and add first and last names.

        # TODO: Check for repeat first and last names while adding.
    return names


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
