"""Test Chapter 1."""
import io
import os
import string
import unittest
import unittest.mock
from tests import random_string
import src.ch01.practice.p1_pig_latin as pig_latin
import src.ch01.practice.p2_poor_bar_chart as bar_chart
import src.ch01.challenge.c1_foreign_bar_chart as foreign_chart
from src.ch01.practice import ENCODE_ERROR, FREQ_ANALYSIS_ERROR, PRINT_BAR_CHART_ERROR
from src.ch01.challenge import ADD_KEYS_ERROR
from tests.data.ch01 import EMPTY_LETTER_DICT


class TestPigLatin(unittest.TestCase):
    """Test Pig Latin encoder."""

    def test_consonant(self):
        """Test that it can encode a word starting with a consonant."""
        self.assertEqual(pig_latin.encode('test'), 'esttay')

    def test_vowel(self):
        """Test that it can encode a word starting with a vowel."""
        self.assertEqual(pig_latin.encode('opportunity'), 'opportunityway')

    def test_bad_type(self):
        """Test that it raises an error if word is not a string."""
        with self.assertRaises(TypeError) as err:
            pig_latin.encode(2)
            self.assertEqual(ENCODE_ERROR, err.exception)

    def test_upper_to_lower(self):
        """Test that it converts uppercase to lowercase."""
        self.assertEqual(pig_latin.encode('Jose'), 'osejay')


class TestBarChart(unittest.TestCase):
    """Test Poor Bar Chart."""

    def test_bad_type(self):
        """Test that it raises an error if sentence is not a string and
        if freq_dict is not a dictionary."""
        with self.assertRaises(TypeError) as err:
            bar_chart.freq_analysis(3)
            self.assertEqual(FREQ_ANALYSIS_ERROR, err.exception)
        with self.assertRaises(TypeError) as err:
            bar_chart.print_bar_chart(4)
            self.assertEqual(PRINT_BAR_CHART_ERROR, err.exception)

    def test_freq_analysis(self):
        """Test that it performs a proper frequency analysis."""
        test_string = random_string(20, string.ascii_lowercase)
        string_set = set(test_string)
        analysis = bar_chart.freq_analysis(test_string)

        for element in string_set:
            # Test that each element in the set is a key.
            self.assertIn(element, analysis)
            # Test that each element in the dictionary value matches the key.
            for i in analysis[element]:
                self.assertEqual(element, i)
            # Test that each dictionary value has the correct number of elements.
            self.assertEqual(test_string.count(element), len(analysis[element]))

        # Test that it skips non-letters.
        test_string = random_string(20, string.punctuation + string.whitespace)
        analysis = bar_chart.freq_analysis(test_string)
        self.assertDictEqual(analysis, {})

        # Test that it converts uppercase to lowercase.
        test_string = random_string(20, string.ascii_uppercase)
        analysis = bar_chart.freq_analysis(test_string)
        for key in analysis.keys():
            self.assertTrue(key.islower())

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def test_print_bar_chart(self, mock_stdout):
        """Test that it properly prints a dictionary."""
        with open(os.path.normpath('tests/data/poor_bar_chart.txt'), 'r') as file:
            file_data = ''.join(file.readlines())

        test_string = "Peter Piper picked a peck of pickled peppers."
        test_dict = bar_chart.freq_analysis(test_string)
        bar_chart.print_bar_chart(test_dict)
        self.assertEqual(mock_stdout.getvalue(), file_data)


class TestForeignChart(unittest.TestCase):
    """Test Foreign Bar Chart."""

    def test_bad_type(self):
        """Test that it raises an error if sentence is not a string and
        if dictionary is not a dictionary."""
        with self.assertRaises(TypeError) as err:
            foreign_chart.foreign_freq_analysis(3)
            self.assertEqual(FREQ_ANALYSIS_ERROR, err.exception)
        with self.assertRaises(TypeError) as err:
            foreign_chart.add_keys_to_dict(4)
            self.assertEqual(ADD_KEYS_ERROR, err.exception)

    def test_add_keys_to_dict(self):
        """Test add_keys_to_dict function."""
        # Test that it adds all ASCII lowercase letters to a dictionary.
        test_dict = foreign_chart.add_keys_to_dict({})
        for letter in string.ascii_lowercase:
            self.assertIn(letter, test_dict)

        # Test that it doesn't duplicate keys.
        random_letter = random_string(1, string.ascii_lowercase)
        random_dict = {random_letter: []}
        test_dict = foreign_chart.add_keys_to_dict(random_dict)
        self.assertDictEqual(test_dict, EMPTY_LETTER_DICT)


if __name__ == '__main__':
    unittest.main()
