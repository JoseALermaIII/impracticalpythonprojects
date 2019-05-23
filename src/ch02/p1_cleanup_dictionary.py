"""Remove single letter words from a word dictionary."""
from src.ch01.challenge.c2_name_generator import read_from_file
from src.ch02 import DICTIONARY_FILE_PATH


def cleanup_dict(filepath: str) -> list:
    """Cleanup dictionary.

    Remove single letter words from a word dictionary file.

    Args:
        filepath (str): String with path to dictionary file.

    Returns:
        List with words as elements excluding single letter words.

    """
    word_list = read_from_file(filepath)
    return [word for word in word_list if len(word) > 1]


def main():
    """Demonstrate cleanup dictionary."""
    print('I\'m a word dictionary cleaner.\n'
          'I remove those annoying one letter words.\n')
    word_list = read_from_file(DICTIONARY_FILE_PATH)
    word_list_len = len(word_list)
    clean_word_list = cleanup_dict(DICTIONARY_FILE_PATH)
    clean_word_list_len = len(clean_word_list)
    print(f'Original word list had {word_list_len} words.\n'
          f'Cleaned word list has {clean_word_list_len} words.\n'
          f'I cleaned up {word_list_len - clean_word_list_len} words! '
          f'Yay, me!')


if __name__ == '__main__':
    main()
