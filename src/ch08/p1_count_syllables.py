"""Test count_syllables with a word dictionary file.

Randomly select words from a word dictionary file and pass them through
:func:`count_syllables` to find their syllable counts. Output each word with
their respective syllable count.

Attributes:
    CMUDICT (dict): Dictionary of CMUdict's phonemes with the word as a key
        and its phonemes as a list of lists.
    MISSING_WORDS (dict): Dictionary with syllable counts of words
        missing from CMUdict's phoneme list where the word is the key and
        its syllable count as an integer value.

"""
import json
import os
from random import sample
from string import punctuation

import nltk
from nltk.corpus import cmudict

from src.ch02 import DICTIONARY_FILE_PATH
from src.ch02.p1_cleanup_dictionary import cleanup_dict

if not os.path.exists(
        os.path.expanduser('~/nltk_data/corpora/cmudict/cmudict')):
    # pylint: disable=fixme
    # FIXME: This is nearly impossible to test.
    #  Patching os affects every use of os in the module.
    nltk.download('cmudict')

# Convert CMUdict into a dictionary.
CMUDICT = cmudict.dict()

with open(os.path.join(os.path.dirname(__file__),
                       'p1files/missing_words.json')) as in_file:
    # Load local dictionary of words with syllable counts.
    # Words as strings are keys and integers are values.
    MISSING_WORDS = json.load(in_file)


def format_words(words: str) -> list:
    """Format words for processing.

    Remove hyphens, convert to lowercase, and strip both punctuation and
    possessives from word or phrase.

    Args:
        words (str): Word or phrase to format for processing.

    Returns:
        List of strings containing processed words.

    """
    words = words.replace('-', ' ')
    word_list = words.lower().split()
    for i, word in enumerate(word_list):
        word = word.strip(punctuation)
        if any([word.endswith("'s"), word.endswith("’s")]):
            word_list[i] = word[:-2]
        else:
            word_list[i] = word
    return word_list


def count_syllables(words: list) -> int:
    """Use CMUdict to count syllables in English word.

    Calculate sum of syllable counts for each word in **words**. Checks
    syllable counts in the :py:mod:`nltk.corpus` CMUdict phoneme list, if word
    is not found in CMUdict, also checks local dictionary with syllable
    counts.

    Args:
        words (list): List of strings to sum number of syllables.

    Returns:
        Integer representing number of syllables in **words**.

    Note:
        Defaults to first element in CMUdict phoneme list. So, multiple
        syllable counts are ignored.

    """
    syllables = 0
    for word in words:
        if word in MISSING_WORDS:
            syllables += MISSING_WORDS[word]
        else:
            for phonemes in CMUDICT[word][0]:
                for phoneme in phonemes:
                    if phoneme[-1].isdigit():
                        syllables += 1
    return syllables


def main():
    """Demonstrate count_syllables with a word dictionary file."""
    word_list = cleanup_dict(DICTIONARY_FILE_PATH)
    sample_list = sample(word_list, 15)
    for word in sample_list:
        try:
            syllables = count_syllables(format_words(word))
        except KeyError:
            # Skip words in neither dictionary.
            print(f'Not found: {word}')
            continue
        print(f'{word} {syllables}')


if __name__ == '__main__':
    main()
