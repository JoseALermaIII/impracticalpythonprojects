"""Test Chapter 2."""
import unittest
import src.ch02.p1_cleanup_dictionary as cleanup_dictionary
from tests import random_string
from src.ch02 import CLEANUP_LIST_ERROR


class TestCleanupDictionary(unittest.TestCase):
    """Test Cleanup Dictionary."""

    def test_bad_type(self):
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


if __name__ == '__main__':
    unittest.main()
