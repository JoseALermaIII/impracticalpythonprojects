"""Generate haiku with Markov chain analysis.

Generate Markov models of 1st and 2nd order from a training text of haiku
poems using a random word. Using these Markov models, select words that build
three lines following a haiku syllable structure: 5-7-5. As each word is
selected, the Markov chain is expanded to use the two preceding words to
generate new models.

If the word or phrase doesn't have a Markov model word that fits the syllable
count, generate a new Markov model using another random word and select a word
that does fit the syllable count.

"""
import sys
import logging
import random
from collections import defaultdict
from src.ch01.challenge.c2_name_generator import read_from_file
from src.ch08.p1_count_syllables import format_words, count_syllables

# Configure parent logger for ch09 module.
#
# NOTE: All modules that import this module and reference the same logger
# object, 'markov_haiku', will use this parent logger.
#
# logging.disable(logging.CRITICAL)  # Disable logging. Comment out to enable.
LOG = logging.getLogger('markov_haiku')
LOG.setLevel(logging.DEBUG)
# Make file handler that logs everything.
FH = logging.FileHandler('markov_haiku.log')
FH.setLevel(logging.DEBUG)
# Make console handler that outputs INFO or above levels.
CH = logging.StreamHandler()
CH.setLevel(logging.INFO)
# Make formatter and add it to the handlers
FORMATTER = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
CH.setFormatter(FORMATTER)
FH.setFormatter(FORMATTER)
# Add the handlers to log.
LOG.addHandler(CH)
LOG.addHandler(FH)


def prep_training(filepath: str) -> list:
    """Prepare training corpus from file.

    Use a training text from **filepath** to prepare a list of words
    to generate Markov models from.

    Pass **filepath** through
    :func:`~src.ch01.challenge.c2_name_generator.read_from_file` to
    get each line in a list of strings. Then, pass each line through
    :func:`src.ch08.p1_count_syllables.format_words` to get each word
    in a list of strings.

    Args:
        filepath (str): String with absolute path to training file.


    Returns:
        List of words from training file.

    Note:
        It is imperative that the words stay in order as read from the file
        so that the Markov models are accurate and consistent.

    """
    lines = read_from_file(filepath)
    word_list = []
    for line in lines:
        words = format_words(line)
        word_list.extend(words)
    LOG.debug('prep_training: %s words', len(word_list))
    return word_list


def get_markov_model(word_list: list, order_num: int) -> dict:
    """Get Markov model of nth order.

    Generate a dictionary representing a Markov model of **order_num** order.
    Take each word in **word_list** and add the next words up to length
    **order_num** to form the prefix. The suffixes are the very next string
    after the prefix.

    Args:
         word_list (list): List of strings of individual words from training
            text.
         order_num (int): Order of Markov model to generate.

    Returns:
        Dictionary of prefixes as strings and a list of suffixes as values.

    """
    end = len(word_list) - order_num
    markov_model = defaultdict(list)

    for index, word in enumerate(word_list):
        if index < end:
            if order_num == 1:
                prefix = word
            else:
                chain = [word_list[index + i] for i in range(order_num)]
                prefix = ' '.join(chain)
            suffix = word_list[index + order_num]
            markov_model[prefix].append(suffix)
    LOG.debug('get_markov_model keys: %s', markov_model.keys())
    return markov_model


def random_word(word_list: list, max_syls: int = 4) -> tuple:
    """Get random word from word list.

    Get random word from **word_list** with a syllable count less than
    **max_syls**.

    """
    word = random.choice(word_list)
    syllables = count_syllables(format_words(word))
    while syllables > max_syls:
        word = random.choice(word_list)
        syllables = count_syllables(format_words(word))
    LOG.debug('random_word: %s, %s', word, syllables)
    return word, syllables


def main():
    """Demonstrate Markov haiku maker."""


if __name__ == '__main__':
    main()
