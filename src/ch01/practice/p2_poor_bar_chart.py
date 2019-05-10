"""Takes a sentence as input and returns a 'bar chart' of each letter."""
import pprint
from collections import defaultdict
from src.ch01.practice import FREQ_ANALYSIS_ERROR, PRINT_BAR_CHART_ERROR


def freq_analysis(sentence: str) -> dict:
    """Perform frequency analysis of letters in sentence.

    Iterate through each letter in the sentence and add it to a dictionary of
    lists using ``collections.defaultdict``.

    Args:
        sentence (str): String to count letters of.

    Returns:
        Dictionary with each letter as keys and list with letters repeated
        based on their frequency as values.

    Raises:
        TypeError: If `sentence` is not a string.

    """
    if not isinstance(sentence, str):
        raise TypeError(FREQ_ANALYSIS_ERROR)

    #  Add each letter to a list with collections.defaultdict
    output = defaultdict(list)

    for i in sentence:
        if not i.isalpha():
            continue

        if i.isupper():
            i = i.lower()

        output[i].append(i)

    return output


def print_bar_chart(freq_dict: dict) -> None:
    """Print dictionary to terminal.

    Use ``pprint`` to print dictionary with letter frequency analysis to
    terminal.

    Args:
        freq_dict (dict): Dictionary with frequency analysis from
        freq_analysis.

    Returns:
        If recursive, prints a recursive-safe string, otherwise prints the
        dictionary.

    Raises:
        TypeError: If `freq_dict` is not a dictionary.

    """
    if not isinstance(freq_dict, dict):
        raise TypeError(PRINT_BAR_CHART_ERROR)

    if pprint.isrecursive(freq_dict):
        return pprint.pprint(pprint.saferepr(freq_dict))

    return pprint.pprint(freq_dict)


def main():
    """Demonstrates the Poor Bar Chart."""
    print('This is an Affordable Bar Chart.\n')
    twister = 'Sally sells seashells by the seashore.'
    print(f'Analyzing: {twister}\n')
    print_bar_chart(freq_analysis(twister))


if __name__ == '__main__':
    main()
