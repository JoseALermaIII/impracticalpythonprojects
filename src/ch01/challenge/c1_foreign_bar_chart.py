"""Return letter 'bar chart' of a non-English sentence."""
import string
from src.ch01.challenge import ADD_KEYS_ERROR
from src.ch01.practice import FREQ_ANALYSIS_ERROR
from src.ch01.practice.p2_poor_bar_chart import freq_analysis, print_bar_chart


def add_keys_to_dict(dictionary: dict) -> dict:
    """Add keys to dictionary.

    Check keys of a letter dictionary and add missing letters.

    Args:
        dictionary (dict): Dictionary to check keys of.

    Returns:
        Dictionary with all ASCII lowercase letters as keys.

    Raises:
        TypeError: If `dictionary` is not a dictionary.

    """
    if not isinstance(dictionary, dict):
        raise TypeError(ADD_KEYS_ERROR)

    for i in string.ascii_lowercase:
        if i not in dictionary:
            dictionary[i] = []

    return dictionary


def foreign_freq_analysis(sentence: str) -> dict:
    """Wrap freq_analysis and add_keys_to_dict.

    Passes given sentence through freq_analysis then add_keys_to_dict to
    fill in missing keys.

    Args:
        sentence (str): String to count letters of.

    Returns:
        Dictionary with all ASCII lowercase letters as keys and list with
        letters repeated based on their frequency as values.

    Raises:
        TypeError: If `sentence` is not a string.

    """
    if not isinstance(sentence, str):
        raise TypeError(FREQ_ANALYSIS_ERROR)
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
