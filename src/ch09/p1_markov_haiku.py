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
    :func:`~src.ch08.p1_count_syllables.format_words` to get each word
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
    LOG.debug('get_markov_model number of keys: %s', len(markov_model.keys()))
    return markov_model


def random_word(word_list: list, max_syls: int = 4) -> tuple:
    """Get random word from word list.

    Get random word from **word_list** with a syllable count less than
    **max_syls**.

    Can generate seed word for :func:`get_markov_model`.

    Args:
        word_list (list): List of words to select from.
        max_syls (int): Maximum number of syllables word can be. Defaults
            to ``4``.

    Returns:
        :py:obj:`tuple` with word and syllable count as values.

    """
    word = random.choice(word_list)
    syllables = count_syllables(format_words(word))
    while syllables > max_syls:
        word = random.choice(word_list)
        syllables = count_syllables(format_words(word))
    LOG.debug('random_word: %s, %s', word, syllables)
    return word, syllables


def next_words(prefix: str, markov_model: dict, max_syls: int) -> list:
    """Get next usable words for prefix in Markov model.

    Get next words from **markov_model** given a **prefix** that will be
    less than or equal to **syllable_target** when added to **prefix**.

    Args:
        prefix (str): Word or phrase to find next usable words of.
        markov_model (dict): Markov model of order matching number of words
            in **prefix**.
        max_syls (int): Maximum number of total syllables.

    Return:
        List of usable words that can follow **prefix**.

    """
    usable_words = []
    syllable_count = count_syllables(format_words(prefix))
    suffixes = markov_model.get(prefix)
    if suffixes is None:
        # Prefix is last entry in word_list used to make markov_model and
        # also happens to be unique.
        LOG.warning('No suffixes for: %s', prefix)
        return usable_words
    for suffix in suffixes:
        syllables = count_syllables(format_words(suffix))
        if syllable_count + syllables <= max_syls:
            usable_words.append(suffix)
    LOG.debug('next_words for "%s": %s', prefix, usable_words)
    return usable_words


def haiku_line(prefix: str, word_list: list,
               target_syls: int, line: list = None,
               is_first_line: bool = False) -> str:
    """Make a line of haiku.

    Given a **prefix**, use **word_list** to make a Markov model
    of the needed order to make a line with a syllable count of
    **target_syls**.

    Args:
        prefix (str): Words to use as a seed for the Markov model.
        word_list (list): List of words from a training text.
        target_syls (int): Number of syllables to make **line**.
        line (list): List of words containing current state of the line
            of haiku. Defaults to :py:obj:`None`.
        is_first_line (bool): Boolean flag indicating that current haiku line
            is the first line of haiku. Used to initialize **line** with
            **prefix** if **line** is empty. Defaults to :py:obj:`False`.

    Returns:
        Line of haiku with **target_syls** syllables.

    """
    line = line or []
    words = format_words(prefix)
    if is_first_line and not line:
        line.extend(words)
    order_num = len(words)
    syllables = count_syllables(line)
    LOG.debug('syllables: %s', syllables)
    if order_num == 1:
        markov_model = get_markov_model(word_list, order_num)
        usable_words = next_words(prefix, markov_model, target_syls)
    else:
        # Prefix is more than one word, use last two words.
        markov_model = get_markov_model(word_list, 2)
        usable_words = next_words(' '.join(words[-2:]), markov_model,
                                  target_syls)
    if syllables == target_syls:
        return ' '.join(line)
    while not usable_words:
        # No usable words, randomly choose another prefix.
        new_prefix = random.choice(word_list)
        markov_model = get_markov_model(word_list, 1)
        LOG.debug('No usable_words. New prefix: %s', new_prefix)
        usable_words = next_words(new_prefix, markov_model, target_syls)
        if usable_words:
            line.append(new_prefix)
    while True:
        # Recursively build haiku line.
        next_word = random.choice(usable_words)
        next_word_syls = count_syllables(format_words(next_word))
        LOG.debug('Add "%s" to "%s"', next_word, line)
        if next_word_syls + syllables > target_syls:
            if sum([1 for word in usable_words if
                    count_syllables(format_words(word)) >= next_word_syls]) == len(usable_words):
                # All words in usable words go over syllable count.
                line = line[:-1]
                usable_words = []
                while not usable_words:
                    # No usable words, randomly choose another prefix.
                    new_prefix = random.choice(word_list)
                    markov_model = get_markov_model(word_list, 1)
                    LOG.debug('No usable_words and over count. New prefix: %s', new_prefix)
                    usable_words = next_words(new_prefix, markov_model, target_syls)
                    if usable_words:
                        line.append(new_prefix)
            continue
        line.append(next_word)
        if len(line) < 2:
            # Not enough words in line to form new prefix.
            new_prefix = ' '.join([words[-1], line[-1]])
        else:
            new_prefix = ' '.join(line[-2:])
        return haiku_line(new_prefix, word_list, target_syls, line)


def main():
    """Demonstrate Markov haiku maker."""


if __name__ == '__main__':
    main()
