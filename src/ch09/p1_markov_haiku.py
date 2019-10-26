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
# logging.disable()  # Disable logging. Comment out to enable.
LOG = logging.getLogger('markov_haiku')
LOG.setLevel(logging.DEBUG)
# Make file handler that logs everything.
FH = logging.FileHandler('markov_haiku.log')
FH.setLevel(logging.DEBUG)
# Make console handler that outputs INFO or above levels.
CH = logging.StreamHandler()
CH.setLevel(logging.INFO)
# Make formatter and add it to the handlers
formatter = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
CH.setFormatter(formatter)
FH.setFormatter(formatter)
# Add the handlers to log.
LOG.addHandler(CH)
LOG.addHandler(FH)


def main():
    """Demonstrate Markov haiku maker."""


if __name__ == '__main__':
    main()
