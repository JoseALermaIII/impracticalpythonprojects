"""Takes a sentence as input and returns a 'bar chart' of each letter."""
import collections
import pprint


def freq_analysis(sentence: str) -> dict:
    """Perform frequency analysis of letters in sentence.

    Iterate through each letter in the sentence and add it to a dictionary of
    lists using ``collections.defaultdict``.

    Args:
        sentence (str): String to count letters of.

    Returns:
        Dictionary with each letter as keys and list with letters repeated
        based on their frequency as values.

    """
    #  TODO: Add each letter to a list with collections.defaultdict


def print_bar_chart(freq_dict: dict) -> None:
    """Print dictionary to terminal.

    Use ``pprint`` to print dictionary with letter frequency analysis to
    terminal.

    Args:
        freq_dict (dict): Dictionary with frequency analysis from
        freq_analysis.

    Returns:
        None. Prints dictionary to terminal.

    """
    #  TODO: Display dictionary with pprint


def main():
    """Demonstrates the Poor Bar Chart."""


if __name__ == '__main__':
    main()
