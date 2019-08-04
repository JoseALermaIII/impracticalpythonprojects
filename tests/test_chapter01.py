"""Test Chapter 1."""
import os
import string
import unittest.mock
from io import StringIO
from random import Random
from tests import random_string
import src.ch01.practice.p1_pig_latin as pig_latin
import src.ch01.practice.p2_poor_bar_chart as bar_chart
import src.ch01.challenge.c1_foreign_bar_chart as foreign_chart
import src.ch01.challenge.c2_name_generator as name_generator
from src.ch01.practice import ENCODE_ERROR, FREQ_ANALYSIS_ERROR, PRINT_BAR_CHART_ERROR
from src.ch01.challenge import ADD_KEYS_ERROR, SPLIT_NAME_LIST_ERROR, \
    SPLIT_NAME_EMPTY_ERROR, ADD_NAME_TO_KEY_ERROR, GENERATE_NAME_ERROR, \
    BUILD_LIST_ERROR
from tests.data.ch01.ch01 import EMPTY_LETTER_DICT


class TestPigLatin(unittest.TestCase):
    """Test Pig Latin encoder."""

    def test_bad_type(self):
        """Test that it raises an error if word is not a string."""
        with self.assertRaises(TypeError) as err:
            pig_latin.encode(2)
            self.assertEqual(ENCODE_ERROR, err.exception)

    def test_pig_latin(self):
        """Test pig_latin."""
        # Test that it can encode a word starting with a consonant.
        self.assertEqual(pig_latin.encode('test'), 'esttay')
        # Test that it can encode a word starting with a vowel.
        self.assertEqual(pig_latin.encode('opportunity'), 'opportunityway')
        # Test that it converts uppercase to lowercase.
        self.assertEqual(pig_latin.encode('Jose'), 'osejay')

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout):
        """Test demo main function."""
        # Mock user input.
        with unittest.mock.patch('builtins.input',
                                 side_effect=['computer', 'no']):
            pig_latin.main()
        # Test printed output.
        with open(os.path.normpath('tests/data/ch01/main/pig_latin.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        self.assertEqual(mock_stdout.getvalue(), file_data)


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

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_print_bar_chart(self, mock_stdout):
        """Test that it properly prints a dictionary."""
        test_string = "Peter Piper picked a peck of pickled peppers."
        test_dict = bar_chart.freq_analysis(test_string)
        bar_chart.print_bar_chart(test_dict)
        # Test printed output.
        with open(os.path.normpath('tests/data/ch01/poor_bar_chart_func.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        self.assertEqual(mock_stdout.getvalue(), file_data)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout):
        """Test demo main function."""
        bar_chart.main()
        # Test printed output.
        with open(os.path.normpath('tests/data/ch01/main/poor_bar_chart.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
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


class TestNameGenerator(unittest.TestCase):
    """Test Name Generator."""

    @classmethod
    def setUpClass(cls):
        """Configure attributes for use in this class only."""
        cls.random = Random(512)

    def test_errors(self):
        """Test that each function raises its errors."""
        with self.assertRaises(IndexError) as err:
            os.makedirs('tests/data/ch01/empty', exist_ok=True)
            name_generator.build_name_list('tests/data/ch01/empty')
            self.assertEqual(BUILD_LIST_ERROR, err.exception)
        with self.assertRaises(TypeError) as err:
            test_dict = {'blank': []}
            name_generator.add_name_to_key(4, test_dict, 'blank')
            self.assertEqual(ADD_NAME_TO_KEY_ERROR, err.exception)
            name_generator.add_name_to_key('First', test_dict, 5)
            self.assertEqual(ADD_NAME_TO_KEY_ERROR, err.exception)
            name_generator.add_name_to_key('First', 6, 'blank')
            self.assertEqual(ADD_NAME_TO_KEY_ERROR, err.exception)
            name_generator.split_names(7)
            self.assertEqual(SPLIT_NAME_LIST_ERROR, err.exception)
            test_list = []
            name_generator.split_names(test_list)
            self.assertEqual(SPLIT_NAME_EMPTY_ERROR, err.exception)
        with self.assertRaises(KeyError) as err:
            name_generator.generate_name(test_dict)
            self.assertEqual(GENERATE_NAME_ERROR, err.exception)

    def test_read_from_file(self):
        """Test that read_from_file can read names from a file."""
        test_name_list = name_generator.read_from_file('tests/data/ch01/names/name.txt')
        name_list = ['Sam Smith Schmidt "The Squid" Sampson IV',
                     'Tadd Todd Thomas Sr.']
        self.assertListEqual(test_name_list, name_list)

    def test_build_name_list(self):
        """Test that build_name_list can read names from multiple files."""
        test_name_list = name_generator.build_name_list('tests/data/ch01/names')
        name_list = ['Sally Smith', 'Sam Smith Schmidt "The Squid" Sampson IV',
                     'Tadd Todd Thomas Sr.']
        self.assertListEqual(test_name_list, name_list)

    def test_add_name_to_key(self):
        """Test that add_name_to_key can add strings to a dictionary key."""
        test_dict = {'blank': []}
        name_generator.add_name_to_key('name', test_dict, 'blank')
        self.assertDictEqual(test_dict, {'blank': ['name']})
        # Test that it ignores duplicates.
        name_generator.add_name_to_key('name', test_dict, 'blank')
        self.assertDictEqual(test_dict, {'blank': ['name']})

    def test_split_names(self):
        """Test that split_names can split a list of names into a
        dictionary."""
        name_list = name_generator.build_name_list('tests/data/ch01/names')
        test_dict = name_generator.split_names(name_list)
        name_dict = {'first': ['Sally', 'Sam', 'Tadd'],
                     'middle': ['"The Squid"', 'Schmidt', 'Smith', 'Todd'],
                     'last': ['Sampson', 'Smith', 'Thomas']}
        self.assertDictEqual(test_dict, name_dict)

    @unittest.mock.patch('src.ch01.challenge.c2_name_generator.random')
    def test_generate_name(self, random):
        """Test that generate_name can make a name with(out) a middle name."""
        name_dict = {'first': ['Sally', 'Sam', 'Tadd'],
                     'middle': ['"The Squid"', 'Smith', 'Schmidt', 'Todd'],
                     'last': ['Smith', 'Sampson', 'Thomas']}
        random.choice._mock_side_effect = self.random.choice
        # Use seed that generates a middle name.
        self.assertEqual(name_generator.generate_name(name_dict), 'Sally Schmidt Sampson')
        # Use seed that doesn't generate a middle name.
        self.random = Random(511)
        self.assertEqual(name_generator.generate_name(name_dict), 'Sam Sampson')

    @unittest.mock.patch('src.ch01.challenge.c2_name_generator.random')
    def test_name_generator(self, random):
        """Test that name_generator can output a name."""
        # Use predictable seed
        self.random.seed(555)
        random.choice._mock_side_effect = self.random.choice
        self.assertEqual(name_generator.name_generator('tests/data/ch01/names'), 'Sally Schmidt Smith')


if __name__ == '__main__':
    unittest.main()
