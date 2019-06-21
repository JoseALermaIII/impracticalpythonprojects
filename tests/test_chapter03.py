"""Test Chapter 3."""
import os
import unittest
from string import ascii_lowercase
from src.ch02.p1_cleanup_dictionary import cleanup_dict, cleanup_list_more
import src.ch03.p1_digram_counter as digram_counter
import src.ch03.c1_anagram_generator as anagram_generator
from src.ch03 import GET_DIGRAMS_ERROR, COUNT_DIGRAMS_ERROR
from tests import random_string
from tests.data.ch03.ch03 import LETTER_PRIME_DICT


class TestDigramCounter(unittest.TestCase):
    """Test Digram Counter."""

    def test_bad_type(self):
        """Test that it raises its errors."""
        with self.assertRaises(TypeError) as err:
            digram_counter.get_digrams(5)
            self.assertEqual(GET_DIGRAMS_ERROR, err.exception)
            digram_counter.count_digrams(6, [])
            self.assertEqual(COUNT_DIGRAMS_ERROR, err.exception)
            digram_counter.count_digrams(set(), 7)
            self.assertEqual(COUNT_DIGRAMS_ERROR, err.exception)

    def test_get_digrams(self):
        """Test that it can make a set of digrams."""
        digrams = {'ol', 'vo', 'ov', 'oo', 'vl', 'lo', 'vv', 'lv'}
        test_word = 'volvo'
        test_digrams = digram_counter.get_digrams(test_word)
        self.assertSetEqual(digrams, test_digrams)

    def test_count_digrams(self):
        """Test that it can count digrams in a word list."""
        word_list = ['tom', 'morrow', 'moon', 'light']
        digrams = {'to', 'mo', 'on', 'gh', 'li', 'bo'}
        digram_count = {'mo': 2, 'gh': 1, 'li': 1, 'to': 1, 'on': 1, 'bo': 0}
        test_count = digram_counter.count_digrams(digrams, word_list)
        self.assertDictEqual(digram_count, test_count)

    def test_digram_counter(self):
        """Test that it can count digrams in a word dictionary file."""
        test_dict_path = os.path.abspath('tests/data/ch02/dictionary.txt')
        word = 'abracadabra'
        count = {'ra': 4, 'ar': 4, 'ac': 3, 'ca': 3, 'br': 2, 'ab': 1,
                 'da': 1, 'ad': 1, 'rd': 1, 'dr': 1, 'bb': 1, 'rr': 1,
                 'aa': 1, 'bc': 0, 'dc': 0, 'cd': 0, 'ba': 0, 'db': 0,
                 'bd': 0, 'cr': 0, 'rb': 0, 'cb': 0, 'rc': 0}
        test_count = digram_counter.digram_counter(word, test_dict_path)
        self.assertDictEqual(count, test_count)


class TestAnagramGenerator(unittest.TestCase):
    """Test Anagram Generator."""

    def test_get_primes(self):
        """Test that it can make a list of primes."""
        # Test default primes.
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                  59, 61, 67, 71, 73, 79, 83, 89, 97, 101]
        test_primes = anagram_generator.get_primes()
        self.assertListEqual(primes, test_primes)
        # Test single prime.
        primes = [2]
        test_primes = anagram_generator.get_primes(length=1)
        self.assertListEqual(primes, test_primes)
        # Test capped primes.
        primes = [2, 3, 3]
        test_primes = anagram_generator.get_primes(length=3, max_prime=3)
        self.assertListEqual(primes, test_primes)
        # Test prime range.
        primes = [23, 29, 31]
        test_primes = anagram_generator.get_primes(length=3, min_prime=23)
        self.assertListEqual(primes, test_primes)
        # Test even min_prime.
        primes = [23, 29, 31]
        test_primes = anagram_generator.get_primes(length=3, min_prime=22)
        self.assertListEqual(primes, test_primes)
        # Test even min_prime near two odd primes.
        primes = [61, 67]
        test_primes = anagram_generator.get_primes(length=2, min_prime=60)
        self.assertListEqual(primes, test_primes)

    def test_get_id(self):
        """Test that it can convert a word to an ID."""
        # Test a random letter.
        test_letter = random_string(1, ascii_lowercase)
        test_letter_id = anagram_generator.get_id(test_letter)
        self.assertEqual(LETTER_PRIME_DICT[test_letter], test_letter_id)
        # Test a random string.
        test_string = random_string(30, ascii_lowercase)
        test_string_id = anagram_generator.get_id(test_string)
        actual_id = 1
        for letter in test_string:
            actual_id *= LETTER_PRIME_DICT[letter]
        self.assertEqual(actual_id, test_string_id)

    def test_get_anagram_dict(self):
        """Test that it can make an anagram dictionary."""
        # Test a single element list.
        dictionary = {3715217: ['test']}
        test_list = ['test']
        test_dict = anagram_generator.get_anagram_dict(test_list)
        self.assertDictEqual(dictionary, test_dict)
        # Test a multiple element list with same ID.
        dictionary = {3715217: ['test', 'sett']}
        test_list = ['test', 'sett']
        test_dict = anagram_generator.get_anagram_dict(test_list)
        self.assertDictEqual(dictionary, test_dict)
        # Test a multiple element list with different IDs.
        dictionary = {3715217: ['sett', 'test'], 451: ['me'], 131387: ['pls']}
        test_list = ['sett', 'test', 'me', 'pls']
        test_dict = anagram_generator.get_anagram_dict(test_list)
        self.assertDictEqual(dictionary, test_dict)

    def test_split(self):
        """Test that it can split a list."""
        # Test that it can split an even list in half.
        test_list = ['test', 'split', 'a', 'list']
        test_split = anagram_generator.split(test_list, 2)
        split = [['test', 'split'], ['a', 'list']]
        self.assertListEqual(split, test_split)
        # Test that it can split an even list in thirds.
        test_split = anagram_generator.split(test_list, 3)
        split = [['test', 'split'], ['a'], ['list']]
        self.assertListEqual(split, test_split)
        # Test that it can split an odd list in half.
        test_list = ['test', 'split', 'an', 'odd', 'list']
        test_split = anagram_generator.split(test_list, 2)
        split = [['test', 'split', 'an'], ['odd', 'list']]
        self.assertListEqual(split, test_split)
        # Test that it can split an odd list in thirds.
        test_split = anagram_generator.split(test_list, 3)
        split = [['test', 'split'], ['an', 'odd'], ['list']]
        self.assertListEqual(split, test_split)

    def test_find_anagrams(self):
        """Test that it can find anagrams with a word or phrase."""
        dict_file = os.path.abspath('tests/data/ch03/dictionary.txt')
        word_list = cleanup_dict(dict_file)
        word_list = cleanup_list_more(word_list)
        anagram_dict = anagram_generator.get_anagram_dict(word_list)
        # Test a word without anagrams.
        anagrams = []
        test_list = anagram_generator.find_anagrams('ttr', anagram_dict)
        self.assertListEqual(anagrams, test_list)
        # Test a word with anagrams.
        anagrams = ['set', 'test', 'tet']
        test_list = anagram_generator.find_anagrams('test', anagram_dict)
        self.assertListEqual(anagrams, test_list)
        # Test a phrase.
        phrase = 'tip tap'
        anagrams = ['a', 'apt', 'at', 'i', 'it', 'pap', 'pat', 'patti', 'pip',
                    'pit', 'pita', 'pitt', 'tap', 'tat', 'tia', 'tip', 'tit']
        test_list = anagram_generator.find_anagrams(phrase, anagram_dict)
        self.assertListEqual(anagrams, test_list)
        # Test that it ignores uppercase.
        anagrams = ['joe', 'jose', 'so']
        test_list = anagram_generator.find_anagrams('Jose', anagram_dict)
        self.assertListEqual(anagrams, test_list)


if __name__ == '__main__':
    unittest.main()
