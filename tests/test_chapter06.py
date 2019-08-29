"""Test Chapter 6."""
import os
import unittest.mock
from io import StringIO
import src.ch06.p1_invisible_ink as invisible_ink


class TestInvisibleInk(unittest.TestCase):
    """Test Invisible Ink."""

    def test_get_text(self):
        """Test get_text."""
        testfile = os.path.normpath('tests/data/ch06/fake.docx')
        # Test that it doesn't skip blanks.
        paragraphs = invisible_ink.get_text(testfile, skip_blank=False)
        self.assertEqual(paragraphs.count(''), 4)
        # Test that it does skip blanks.
        paragraphs = invisible_ink.get_text(testfile)
        self.assertEqual(paragraphs.count(''), 0)
        # Test that it read contents.
        answerlist = \
            ['This is a test document.',
             'This is a paragraph with two runs. However, it’s not because it has two '
             'lines.',
             'There is intentionally a lot of blank spaces to check if the code can count '
             'them correctly.',
             'So, don’t send me e-mails saying that the formatting in my test files is '
             'incorrect.',
             'Word.']
        self.assertEqual(answerlist, paragraphs)


if __name__ == '__main__':
    unittest.main()
