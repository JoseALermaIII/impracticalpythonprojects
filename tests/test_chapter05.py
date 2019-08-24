"""Test Chapter 5."""
import os
import unittest.mock
from io import StringIO
import src.ch05.p1_encode_null as encode_null
import src.ch05.p2_decode_null as decode_null


class TestEncodeNull(unittest.TestCase):
    """Test Encode Null."""

    def test_encode_null(self):
        """Test encode_null."""
        message = 'Test msg'
        # Test that it raises an ValueError for the second letter.
        word_list = ['Fill', 'Fuller', 'Filling', 'Filler']
        with self.assertRaises(ValueError) as err:
            encode_null.encode_null(message, word_list)
        self.assertEqual('Missing word with second letter of: t', str(err.exception))
        # Test that it raises an ValueError for the third letter.
        word_list = ['Fill', 'Fuller', 'Stout', 'Filler']
        with self.assertRaises(ValueError) as err:
            encode_null.encode_null(message, word_list)
        self.assertEqual('Missing word with third letter of: e', str(err.exception))
        # Test that it encodes a cipherlist.
        word_list = ['Loki', 'Sampson', 'Lemon', 'Stout', 'Ruth',
                     'Egg', 'Vest', 'Lisa', 'Lee', 'Tsar', 'Smoke']
        testlist = encode_null.encode_null(message, word_list)
        answerlist = ['Stout', 'Lee', 'Tsar', 'Ruth', 'Smoke', 'Vest', 'Egg']
        self.assertListEqual(testlist, answerlist)

    @unittest.mock.patch('src.ch05.p1_encode_null.split_names')
    @unittest.mock.patch('src.ch05.p1_encode_null.os.path.abspath')
    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout, mock_abspath, mock_split_names):
        """Test demo main function."""
        # Mock output of abspath to avoid FileNotFoundError.
        mock_abspath.return_value = os.path.normpath('src/ch01/challenge/c2files')
        # Mock output of split_names for test consistency.
        mock_split_names.return_value = \
            {'last': ['Abumrad', 'Abando', 'Dyke', 'Anthony', 'Chapman',
                      'Breeck', 'Brooks', 'Armstrong', 'Anderson', 'Baker',
                      'Bennington', 'Edwards', 'Dewees', 'Belushi', 'April',
                      'Cicierega', 'Brookshier']}
        encode_null.main()
        # Test printed output.
        with open(os.path.normpath('tests/data/ch05/main/encode_null.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        self.assertEqual(mock_stdout.getvalue(), file_data)


class TestDecodeNull(unittest.TestCase):
    """Test Decode Null."""

    def test_decode_null(self):
        """Test decode_null."""
        # Test place == 1
        plaintext = 'word'
        ciphertext = 'why obviously reclusive day'
        test_string = decode_null.decode_null(1, ciphertext)
        self.assertEqual(plaintext, test_string)
        # Test place == 2
        plaintext = 'hello'
        ciphertext = 'The plain eel cannot plot the place of wool'
        test_string = decode_null.decode_null(2, ciphertext)
        self.assertEqual(plaintext, test_string)
        # Test place == 3
        plaintext = 'john'
        ciphertext = ('Baja California runs amok with the aching of the '
                      'bandersnatches')
        test_string = decode_null.decode_null(3, ciphertext)
        self.assertEqual(plaintext, test_string)

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout):
        """Test demo main function."""
        decode_null.main()
        # Test printed output.
        with open(os.path.normpath('tests/data/ch05/main/decode_null.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        self.assertEqual(mock_stdout.getvalue(), file_data)


if __name__ == '__main__':
    unittest.main()
