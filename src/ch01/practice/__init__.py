"""Chapter 1 Practice Projects.

Attributes:
    VOWELS (tuple): Tuple containing characters of the English vowels
        (except for 'y')

    ENCODE_ERROR (str): String with :py:exc:`TypeError` for Pig Latin
        :func:`~p1_pig_latin.encode`.

    FREQ_ANALYSIS_ERROR (str): String with :py:exc:`TypeError` for Poor Bar
        Chart :func:`~p2_poor_bar_chart.freq_analysis`.

    PRINT_BAR_CHART_ERROR (str): String with :py:exc:`TypeError` for Poor
        Bar Chart :func:`~p2_poor_bar_chart.print_bar_chart`.

"""

# Constants
VOWELS = ('a', 'e', 'i', 'o', 'u')
ENCODE_ERROR = 'Word must be a string.'
FREQ_ANALYSIS_ERROR = 'Sentence must be a string.'
PRINT_BAR_CHART_ERROR = 'Object must be a dictionary.'
