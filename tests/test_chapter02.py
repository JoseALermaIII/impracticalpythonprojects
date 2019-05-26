"""Test Chapter 2."""
import os
import unittest
import src.ch02.p1_cleanup_dictionary as cleanup_dictionary
import src.ch02.c1_recursive_palindrome as recursive_palindrome
from tests import random_string
from src.ch02 import CLEANUP_LIST_ERROR, RECURSIVE_ISPALINDROME_ERROR


class TestCleanupDictionary(unittest.TestCase):
    """Test Cleanup Dictionary."""

    def test_bad_index(self):
        """Test that it raises an error if word_list is empty."""
        with self.assertRaises(IndexError) as err:
            cleanup_dictionary.cleanup_list([])
            self.assertEqual(CLEANUP_LIST_ERROR, err.exception)

    def test_cleanup_list(self):
        """Test that it removes single letter words from a list of words."""
        random_list = [random_string(1) for _ in range(13)]
        random_list.extend([random_string(5) for _ in range(10)])
        clean_list = cleanup_dictionary.cleanup_list(random_list)
        self.assertEqual(len(clean_list), 10)
        for element in clean_list:
            self.assertEqual(len(element), 5)

    def test_cleanup_dict(self):
        """Test that it removes single letter words from a dictionary file."""
        dict_file = os.path.abspath('tests/data/ch02/dictionary.txt')
        clean_dict = cleanup_dictionary.cleanup_dict(dict_file)
        self.assertEqual(len(clean_dict), 52)  # 78 words - 26 letters
        for element in clean_dict:
            self.assertGreater(len(element), 1)


class TestRecursivePalindrome(unittest.TestCase):
    """Test Recursive Palindrome tester."""

    def test_bad_type(self):
        """Test that it raises an error if word is not a string."""
        with self.assertRaises(TypeError) as err:
            recursive_palindrome.recursive_ispalindrome(5)
            self.assertEqual(RECURSIVE_ISPALINDROME_ERROR, err.exception)


if __name__ == '__main__':
    unittest.main()
