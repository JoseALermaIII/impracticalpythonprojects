"""Test Chapter 5."""
import os
import unittest.mock
from io import StringIO
import src.ch05.p1_encode_null as encode_null


class TestEncodeNull(unittest.TestCase):
    """Test Encode Null."""

    def test_encode_null(self):
        """Test encode_null."""
        message = 'Test msg'
        # Test that it raises an IndexError for the second letter.
        name_list = ['Fill', 'Fuller', 'Filling', 'Filler']
        with self.assertRaises(ValueError) as err:
            encode_null.encode_null(message, name_list)
        self.assertEqual('Missing name with second letter of: t', str(err.exception))
        # Test that it raises an IndexError for the third letter.
        name_list = ['Fill', 'Fuller', 'Stout', 'Filler']
        with self.assertRaises(ValueError) as err:
            encode_null.encode_null(message, name_list)
        self.assertEqual('Missing name with third letter of: e', str(err.exception))
        # Test that it encodes a cipherlist.
        name_list = ['Loki', 'Sampson', 'Lemon', 'Stout', 'Ruth',
                     'Egg', 'Vest', 'Lisa', 'Lee', 'Tsar', 'Smoke']
        testlist = encode_null.encode_null(message, name_list)
        answerlist = ['Loki', 'Stout', 'Lee', 'Tsar', 'Scrooge',
                      'Ruth', 'Smoke', 'Nero', 'Vest', 'Egg']
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


if __name__ == '__main__':
    unittest.main()
