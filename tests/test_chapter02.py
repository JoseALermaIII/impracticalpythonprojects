"""Test Chapter 2."""
import os
import string
import unittest.mock
from io import StringIO
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
        with self.assertRaises(IndexError) as err:
            cleanup_dictionary.cleanup_list_more([])
            self.assertEqual(CLEANUP_LIST_ERROR, err.exception)

    def test_cleanup_list(self):
        """Test that it removes single letter words from a list of words."""
        random_list = [random_string(1) for _ in range(13)]
        random_list.extend([random_string(5) for _ in range(10)])
        clean_list = cleanup_dictionary.cleanup_list(random_list)
        self.assertEqual(len(clean_list), 10)
        for element in clean_list:
            self.assertEqual(len(element), 5)

    def test_cleanup_list_more(self):
        """Test cleanup list more."""
        # Test that it adds approved words.
        approved_words = cleanup_dictionary.APPROVED_WORDS
        test_list = ['test', 'pls']
        dictionary = test_list + approved_words
        dictionary.sort()
        clean_list = cleanup_dictionary.cleanup_list_more(test_list)
        self.assertListEqual(dictionary, clean_list)
        # Test that it skips double letter words.
        dictionary = ['test', 'pls']
        dictionary += approved_words
        dictionary.sort()
        test_list = ['test', 'es', 'pls']
        clean_list = cleanup_dictionary.cleanup_list_more(test_list)
        self.assertListEqual(dictionary, clean_list)
        # Test that it skips words with letters not in string.ascii_lowercase.
        dictionary = ['test']
        dictionary += approved_words
        dictionary.sort()
        test_list = ['test', 'mís']
        clean_list = cleanup_dictionary.cleanup_list_more(test_list)
        self.assertListEqual(dictionary, clean_list)
        # Test that it skips words with apostrophes.
        dictionary = ['test']
        dictionary += approved_words
        dictionary.sort()
        test_list = ['test', "me's"]
        clean_list = cleanup_dictionary.cleanup_list_more(test_list)
        self.assertListEqual(dictionary, clean_list)
        # Test that it removes duplicates.
        dictionary = ['test']
        dictionary += approved_words
        dictionary.sort()
        test_list = ['test', 'test']
        clean_list = cleanup_dictionary.cleanup_list_more(test_list)
        self.assertListEqual(dictionary, clean_list)

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

    def test_recursive_ispalindrome(self):
        """Test that it can identify a pseudo-random palindrome."""
        random_string_ = random_string(10, string.ascii_lowercase)
        random_palindrome = random_string_ + random_string_[::-1]
        self.assertTrue(
            recursive_palindrome.recursive_ispalindrome(random_palindrome))
        # Test a word that isn't a palindrome.
        not_palindrome = 'cat'
        self.assertFalse(
            recursive_palindrome.recursive_ispalindrome(not_palindrome))

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout):
        """Test demo main function."""
        # Test hard-coded word.
        recursive_palindrome.main()
        # Test inputted word.
        recursive_palindrome.main('cat')
        # Test printed output.
        with open(os.path.normpath('tests/data/ch02/main/recursive_palindrome.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        self.assertEqual(mock_stdout.getvalue(), file_data)


if __name__ == '__main__':
    unittest.main()
