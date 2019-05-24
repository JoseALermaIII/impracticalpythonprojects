"""Test Chapter 2."""
import unittest
import src.ch02.p1_cleanup_dictionary as cleanup_dictionary
from src.ch02 import CLEANUP_LIST_ERROR


class TestCleanupDictionary(unittest.TestCase):
    """Test Cleanup Dictionary."""

    def test_bad_type(self):
        """Test that it raises an error if word_list is empty."""
        with self.assertRaises(IndexError) as err:
            cleanup_dictionary.cleanup_list([])
            self.assertEqual(CLEANUP_LIST_ERROR, err.exception)


if __name__ == '__main__':
    unittest.main()
