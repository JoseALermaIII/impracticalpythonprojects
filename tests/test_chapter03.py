"""Test Chapter 3."""
import os
import unittest
from string import ascii_lowercase
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
        test_primes = anagram_generator.get_primes(n=1)
        self.assertListEqual(primes, test_primes)
        # Test capped primes.
        primes = [2, 3, 3]
        test_primes = anagram_generator.get_primes(n=3, max_prime=3)
        self.assertListEqual(primes, test_primes)
        # Test prime range.
        primes = [23, 29, 31]
        test_primes = anagram_generator.get_primes(n=3, min_prime=23)
        self.assertListEqual(primes, test_primes)
        # Test even min_prime.
        primes = [23, 29, 31]
        test_primes = anagram_generator.get_primes(n=3, min_prime=22)
        self.assertListEqual(primes, test_primes)
        # Test even min_prime near two odd primes.
        primes = [61, 67]
        test_primes = anagram_generator.get_primes(n=2, min_prime=60)
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


if __name__ == '__main__':
    unittest.main()
