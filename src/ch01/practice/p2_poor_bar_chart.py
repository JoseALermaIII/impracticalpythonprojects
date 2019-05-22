"""Takes a sentence as input and returns a 'bar chart' of each letter."""
import pprint
from collections import defaultdict
from src.ch01.practice import FREQ_ANALYSIS_ERROR, PRINT_BAR_CHART_ERROR


def freq_analysis(sentence: str) -> dict:
    """Perform frequency analysis of letters in sentence.

    Iterate through each letter in the sentence and add it to a dictionary of
    lists using :py:class:`collections.defaultdict`.

    Args:
        sentence (str): String to count letters of.

    Returns:
        :py:class:`~collections.defaultdict` with each letter as keys and a
        :py:obj:`list` with letters repeated based on their frequency as
        values.

    Example:
        >>> from src.ch01.practice.p2_poor_bar_chart import freq_analysis
        >>> test = 'aaabbbccc'
        >>> freq_analysis(test)
        defaultdict(<class 'list'>, {'a': ['a', 'a', 'a'],
                                     'b': ['b', 'b', 'b'],
                                     'c': ['c', 'c', 'c']})

    Raises:
        TypeError: If **sentence** is not a string.

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

    Use :py:func:`pprint.pprint` to print dictionary with letter frequency
    analysis to terminal.

    Args:
        freq_dict (dict): Dictionary with frequency analysis from
            :func:`freq_analysis`.

    Returns:
        :py:obj:`None`. If recursive, prints a recursive-safe string,
        otherwise prints the dictionary.

    Raises:
        TypeError: If **freq_dict** is not a dictionary.

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
    print('\nIf you tilt your head to the right, the letter "s" is the most '
          'frequent, followed by "e" and "l".')


if __name__ == '__main__':
    main()
