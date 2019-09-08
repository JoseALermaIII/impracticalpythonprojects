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

    def test_check_blanks(self):
        """Test check_blanks."""
        fakefile = os.path.normpath('tests/data/ch06/fake.docx')
        cipherfile = os.path.normpath('tests/data/ch06/cipher.docx')
        # Test that it doesn't need extra blanks.
        faketext = invisible_ink.get_text(fakefile, False)
        ciphertext = invisible_ink.get_text(cipherfile)
        blanks_needed = invisible_ink.check_blanks(faketext, ciphertext)
        self.assertEqual(blanks_needed, 0)
        # Test that it does need extra blanks.
        faketext = invisible_ink.get_text(fakefile)
        blanks_needed = invisible_ink.check_blanks(faketext, ciphertext)
        self.assertEqual(blanks_needed, 3)
        faketext.append('')
        blanks_needed = invisible_ink.check_blanks(faketext, ciphertext)
        self.assertEqual(blanks_needed, 2)
        faketext.append('')
        blanks_needed = invisible_ink.check_blanks(faketext, ciphertext)
        self.assertEqual(blanks_needed, 1)
        faketext.append('')
        blanks_needed = invisible_ink.check_blanks(faketext, ciphertext)
        self.assertEqual(blanks_needed, 0)

    def test_write_invisible(self):
        """Test write_invisible."""
        fakefile = os.path.normpath('tests/data/ch06/fake.docx')
        cipherfile = os.path.normpath('tests/data/ch06/cipher.docx')
        faketext = invisible_ink.get_text(fakefile, False)
        ciphertext = invisible_ink.get_text(cipherfile)
        current_dir = os.path.curdir
        # Test default template and filename.
        invisible_ink.write_invisible(faketext, ciphertext)
        output_file = os.path.join(current_dir, 'output.docx')
        self.assertTrue(os.path.exists(output_file))
        output_text = invisible_ink.get_text(output_file)
        all_text = [element for element in faketext if element != ''] + \
            ciphertext
        self.assertEqual(len(all_text), len(output_text))
        for line in output_text:
            self.assertIn(line, all_text)
        os.remove(output_file)
        # Test custom template and filename.
        template_file = os.path.normpath('tests/data/ch06/template.docx')
        output_file = os.path.join(current_dir, 'letter.docx')
        invisible_ink.write_invisible(faketext, ciphertext, template_file, 'letter.docx')
        self.assertTrue(os.path.exists(output_file))
        output_text = invisible_ink.get_text(output_file)
        all_text = [element for element in faketext if element != ''] + \
            ciphertext
        self.assertEqual(len(all_text), len(output_text))
        for line in output_text:
            self.assertIn(line, all_text)
        os.remove(output_file)
        # Test error.
        faketext = invisible_ink.get_text(fakefile)
        error = ('3 more blanks are needed in the '
                 'plaintext (fake) message.')
        with self.assertRaises(ValueError) as err:
            invisible_ink.write_invisible(faketext, ciphertext)
        self.assertEqual(error, str(err.exception))


if __name__ == '__main__':
    unittest.main()
