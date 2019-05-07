"""Test impractical python projects."""
import unittest
import src.ch01.practice.p1_pig_latin as pig_latin

class TestPigLatin(unittest.TestCase):
    """Test Pig Latin encoder."""

    def test_consonant(self):
        """Test that it can encode a word starting with a consonant."""
        self.assertEqual(pig_latin.encode('test'), 'esttay')

    def test_vowel(self):
        """Test that it can encode a word starting with a vowel."""
        self.assertEqual(pig_latin.encode('opportunity'), 'opportunityway')

if __name__ == '__main__':
    unittest.main()
