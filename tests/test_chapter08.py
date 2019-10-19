"""Test Chapter 8."""
import unittest.mock
import os
from random import Random
from io import StringIO

import src.ch08.p1_count_syllables as count_syllables


class TestCountSyllables(unittest.TestCase):
    """Test Count Syllables."""

    @classmethod
    def setUpClass(cls):
        """Configure attributes for use in this class only."""
        cls.random = Random()

    def test_format_words(self):
        """Test format_words."""
        # Test convert to lowercase.
        for word in ['YOU', 'You', 'yOu', 'yoU', 'yOU', 'YOu', 'YoU', 'you']:
            self.assertEqual(count_syllables.format_words(word), ['you'])
        # Test remove hyphens.
        self.assertEqual(count_syllables.format_words('nit-pick'), ['nit', 'pick'])
        # Test remove punctuation.
        self.assertEqual(count_syllables.format_words('nit-pick!'), ['nit', 'pick'])
        # Test remove possessives.
        for word in ['test’s', 'test\'s']:
            self.assertEqual(count_syllables.format_words(word), ['test'])
        # Test phrase.
        self.assertEqual(count_syllables.format_words('TEST nit-pick'), ['test', 'nit', 'pick'])

    def test_count_syllables(self):
        """Test count_syllables."""
        # Test word not in CMUdict.
        self.assertEqual(count_syllables.count_syllables(['tuxes']), 2)
        # Test word in CMUdict.
        self.assertEqual(count_syllables.count_syllables(['test']), 1)

    @unittest.mock.patch('src.ch08.p1_count_syllables.DICTIONARY_FILE_PATH', 'tests/data/ch08/dictionary.txt')
    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    @unittest.mock.patch('src.ch08.p1_count_syllables.choice')
    def test_main(self, mock_choice, mock_stdout):
        """Test demo main function."""
        self.random.seed(222)
        mock_choice._mock_side_effect = self.random.choice

        count_syllables.main()

        # Test sys.stdout output.
        with open(os.path.normpath('tests/data/ch08/main/count_syllables.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        self.assertEqual(mock_stdout.getvalue(), file_data)


if __name__ == '__main__':
    unittest.main()
