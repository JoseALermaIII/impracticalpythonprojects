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
        # Test that it does skip blanks.
        paragraphs = invisible_ink.get_text(testfile)
        blanklines = 0
        for paragraph in paragraphs:
            if len(paragraph.text) == 0:
                blanklines += 1
        self.assertEqual(blanklines, 0)
        # Test that it doesn't skip blanks.
        paragraphs = invisible_ink.get_text(testfile, skip_blank=False)
        blanklines = 0
        for paragraph in paragraphs:
            if len(paragraph.text) == 0:
                blanklines += 1
        self.assertEqual(blanklines, 4)


if __name__ == '__main__':
    unittest.main()
