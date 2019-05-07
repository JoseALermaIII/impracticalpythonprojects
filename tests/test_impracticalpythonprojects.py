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

    def test_bad_type(self):
        """Test that it raises an error if word is not a string."""
        with self.assertRaises(TypeError):
            pig_latin.encode(2)

    def test_upper_to_lower(self):
        """Test that it converts uppercase to lowercase."""
        self.assertEqual(pig_latin.encode('Jose'), 'osejay')

if __name__ == '__main__':
    unittest.main()
