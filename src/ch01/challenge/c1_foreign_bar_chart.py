"""Return letter 'bar chart' of a non-English sentence."""
import string
from src.ch01.challenge import ADD_KEYS_ERROR
from src.ch01.practice.p2_poor_bar_chart import freq_analysis, print_bar_chart


def add_keys_to_dict(dictionary: dict) -> dict:
    """Add keys to dictionary.

    Check keys of a letter dictionary and add missing letters.

    Args:
        dictionary (dict): Dictionary to check keys of.

    Returns:
        Dictionary with :py:obj:`string.ascii_lowercase` as keys.

    Raises:
        TypeError: If **dictionary** is not a :py:obj:`dict`.

    """
    if not isinstance(dictionary, dict):
        raise TypeError(ADD_KEYS_ERROR)

    for i in string.ascii_lowercase:
        if i not in dictionary:
            dictionary[i] = []

    return dictionary


def foreign_freq_analysis(sentence: str) -> dict:
    """Wrap freq_analysis and add_keys_to_dict.

    Passes given sentence through
    :func:`~src.ch01.practice.p2_poor_bar_chart.freq_analysis` then
    :func:`add_keys_to_dict` to fill in missing keys.

    Args:
        sentence (str): String to count letters of.

    Returns:
        Dictionary with :py:obj:`string.ascii_lowercase` as keys and a
        :py:obj:`list` with letters repeated based on their frequency as
        values.

    """
    return add_keys_to_dict(freq_analysis(sentence))


def main():
    """Demonstrates the Foreign Bar Chart."""
    print('Este es un gráfico de barras asequible para idiomas extranjeros.\n')
    trabalengua = 'Sally vende conchas al lado del orilla del mar.'
    print(f'Analizando: {trabalengua}\n')
    print_bar_chart(foreign_freq_analysis(trabalengua))
    print('\nSi inclina su cabeza hacia la derecha, la letra "l" es la más '
          'frecuente.')


if __name__ == '__main__':
    main()
