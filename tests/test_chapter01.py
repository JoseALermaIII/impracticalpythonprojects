"""Test Chapter 1."""
import unittest
import src.ch01.practice.p1_pig_latin as pig_latin
import src.ch01.practice.p2_poor_bar_chart as bar_chart
from src.ch01.practice import ENCODE_ERROR, FREQ_ANALYSIS_ERROR, PRINT_BAR_CHART_ERROR


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
        """Test that it raises an error if sentence is not a string nor
        if freq_dict is not a dictionary."""
        with self.assertRaises(TypeError) as err:
            bar_chart.freq_analysis(3)
            self.assertEqual(FREQ_ANALYSIS_ERROR, err.exception)
        with self.assertRaises(TypeError) as err:
            bar_chart.print_bar_chart(4)
            self.assertEqual(PRINT_BAR_CHART_ERROR, err.exception)


if __name__ == '__main__':
    unittest.main()
