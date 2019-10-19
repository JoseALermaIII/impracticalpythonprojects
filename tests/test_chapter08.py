"""Test Chapter 8."""
import unittest.mock

import src.ch08.p1_count_syllables as count_syllables


class TestCountSyllables(unittest.TestCase):
    """Test Count Syllables."""

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


if __name__ == '__main__':
    unittest.main()
