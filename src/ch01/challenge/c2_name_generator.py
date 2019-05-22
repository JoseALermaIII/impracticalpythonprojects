"""Generate random names from a list of names."""
import os
import random
import sys
from src.ch01.challenge import SPLIT_NAME_LIST_ERROR, SPLIT_NAME_EMPTY_ERROR,\
    ADD_NAME_TO_KEY_ERROR, GENERATE_NAME_ERROR, BUILD_LIST_ERROR


def read_from_file(filepath: str) -> list:
    """Read from file.

    Reads lines from text file and returns a :py:obj:`list`.

    Args:
        filepath (str): Path to file with names.

    Returns:
        List with each line from the file as an element.

    Note:
        Removes trailing whitespaces.

    """
    # Read lines from file and remove trailing whitespaces.
    with open(filepath, 'r') as file:
        file_data = [line.rstrip() for line in file]
    return file_data


def build_name_list(folderpath: str) -> list:
    """Build name list from folder.

    Builds list of names from name files in given folder.

    Args:
        folderpath (str): Path to folder with name files.

    Returns:
        List with names from **folderpath**.

    Raises:
        IndexError: If **folderpath** has no ``.txt`` files.

    """
    if not folderpath.endswith('/'):
        folderpath = folderpath + '/'
    files, name_list = [file for file in os.listdir(folderpath) if
                        file.endswith('.txt')], []
    if not files:
        raise IndexError(BUILD_LIST_ERROR)
    for file in files:
        name_list.extend(read_from_file(folderpath + file))
    return name_list


def add_name_to_key(name: str, dictionary: dict, key: str) -> None:
    """Add name to key in dictionary.

    Add **name** to **dictionary** under **key** if not already present.

    Args:
         name (str): Name to add to **dictionary**.
         key (str): Key to add **name** under.
         dictionary (dict): Dictionary to add **name** to.

    Returns:
        :py:obj:`None`. **name** is added under **key** if not present,
        **dictionary** is unchanged otherwise.

    Raises:
        TypeError: If **name** and **key** aren't :py:obj:`str` or if
            **dictionary** isn't a :py:obj:`dict`.

    """
    if not all([isinstance(name, str), isinstance(key, str),
                isinstance(dictionary, dict)]):
        raise TypeError(ADD_NAME_TO_KEY_ERROR)
    # Check for repeat names while adding.
    if name not in dictionary[key]:
        dictionary[key].append(name)


def split_names(name_list: list) -> dict:
    """Split names from list of names.

    Splits first, middle, and last names from a given list of names.

    Args:
        name_list (list): List with names as elements.

    Returns:
        Dictionary of lists with ``first``, ``middle``, and ``last`` as keys
        and names as values.

    Raises:
        TypeError: If given name list is not a :py:obj:`list` or
            :py:obj:`tuple`.
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
            add_name_to_key(nickname.strip(), names, 'middle')
            name = name.replace(nickname, '')

        # Drop suffix by dropping last name if less than 4 characters, has
        # a '.', or all uppercase.
        end = name.rfind(' ')
        suffix = name[end:]  # Include space for replace
        if len(suffix.strip()) < 4 and any(['.' in suffix, suffix.isupper()]):
            name = name.replace(suffix, '')

        # Check middle name by counting whitespace and add to middle names.
        if name.count(' ') >= 2:
            # For multi-name middle names
            start, end = name.find(' '), name.rfind(' ')
            middle = name[start:end]  # Include leading space for replace
            if middle.count(' ') > 1:
                end = middle.rfind(' ')
                middle1, middle2 = middle[:end], middle[end:]
                add_name_to_key(middle1.strip(), names, 'middle')
                add_name_to_key(middle2.strip(), names, 'middle')
            else:
                add_name_to_key(middle.strip(), names, 'middle')
            name = name.replace(middle, '')

        # Split and add first and last names.
        end = name.find(' ')
        first, last = name[:end], name[end + 1:]  # Exclude leading space
        add_name_to_key(first, names, 'first')
        add_name_to_key(last, names, 'last')
    return names


def generate_name(name_dict: dict) -> str:
    """Generate pseudo-random name.

    Use names in dictionary to generate a random name.

    Args:
        name_dict: Dictionary from split_names.

    Returns:
        String with a random name.

    Raises:
        KeyError: If there aren't three keys in the dictionary.

    Note:
        Only add middle name between 1/3 and 1/4 of the time.

    """
    # Raise error if there aren't three keys in dictionary.
    if not len(name_dict.keys()) == 3:
        raise KeyError(GENERATE_NAME_ERROR)

    keys = list(name_dict.keys())  # Make keys indexable. Python3.6 only?
    first, last = random.choice(name_dict[keys[0]]),\
        random.choice(name_dict[keys[2]])
    # Add middle name between 1/3 and 1/4 of the time.
    if 25 >= random.choice(range(100)) <= 33:
        middle = random.choice(name_dict[keys[1]])
        return ' '.join([first, middle, last])
    return ' '.join([first, last])


def name_generator(folderpath: str) -> str:
    """Wrap generate_name, split_names, and build_name_list.

    Passes given **folderpath** through :func:`build_name_list` to get the
    names in a :py:obj:`list`, then :func:`split_names` to split them into a
    :py:obj:`dict`, and finally through :func:`generate_name` to make the
    actual name.

    Args:
         folderpath (str): Path to folder with name files.

    Returns:
        String with pseudo-random name.

    """
    return generate_name(split_names(build_name_list(folderpath)))


def main():
    """Demonstrate name generator."""
    print('This is a random name generator.\n'
          'Similar to a character from a certain American detective\n'
          'comedy-drama television series.\n')
    folder = os.path.abspath('c2files')

    print(f'Generated name: {name_generator(folder)}',
          file=sys.stderr)  # Red output


if __name__ == '__main__':
    main()
