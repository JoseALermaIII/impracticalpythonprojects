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

    @unittest.mock.patch('src.ch06.p1_invisible_ink.Path.resolve')
    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout, mock_abspath):
        """Test demo main function."""
        # FIXME: Why doesn't current_dir = os.path.abspath('./p1files') and
        #   fakefile = os.path.join(current_dir, 'fake.docx') used in
        #   src/ch06.p1_invisible_ink.main work with
        #   @unittest.mock.patch('src.ch06.p1_invisible_ink.os.path.abspath')
        #   and mock_abspath.return_value = os.path.normpath('src/ch06/p1files')
        #   used here?
        #   Using Python 3.6.8 and python-docx 0.8.10, fails with:
        #   ValueError: PackURI must begin with slash, got 'src/ch06/p1files'
        #   Had to use pathlib's Path and PurePath in p1_invisible_ink.main

        # Mock output of abspath to avoid FileNotFoundError.
        mock_abspath.return_value = os.path.normpath('src/ch06/p1files')
        current_dir = os.getcwd()
        # Test using test files.
        fakefile = os.path.join(current_dir, 'tests/data/ch06/fake.docx')
        cipherfile = os.path.join(current_dir, 'tests/data/ch06/cipher.docx')
        output_file = os.path.join(current_dir, 'tests/data/ch06/output.docx')
        faketext = invisible_ink.get_text(fakefile, False)
        ciphertext = invisible_ink.get_text(cipherfile)
        invisible_ink.main(fakefile, cipherfile, output_file)
        self.assertTrue(os.path.exists(output_file))
        output_text = invisible_ink.get_text(output_file)
        all_text = ([element for element in faketext if element != ''] +
                    ciphertext)
        self.assertEqual(len(all_text), len(output_text))
        for line in output_text:
            self.assertIn(line, all_text)
        os.remove(output_file)
        # Test printed output.
        with open(os.path.normpath('tests/data/ch06/main/invisible_ink.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        self.assertEqual(mock_stdout.getvalue(), file_data)
        # Test using default files.
        invisible_ink.main()
        fakefile = os.path.join(current_dir, 'src/ch06/p1files/fake.docx')
        cipherfile = os.path.join(current_dir, 'src/ch06/p1files/real.docx')
        output_file = os.path.normpath('src/ch06/p1files/LetterToUSDA.docx')
        faketext = invisible_ink.get_text(fakefile, False)
        ciphertext = invisible_ink.get_text(cipherfile)
        self.assertTrue(os.path.exists(output_file))
        output_text = invisible_ink.get_text(output_file)
        all_text = ([element for element in faketext if element != ''] +
                    ciphertext)
        self.assertEqual(len(all_text), len(output_text))
        for line in output_text:
            self.assertIn(line, all_text)
        os.remove(output_file)


if __name__ == '__main__':
    unittest.main()
