"""Test Chapter 5."""
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
        with self.assertRaises(IndexError) as err:
            encode_null.encode_null(message, name_list)
        self.assertEqual('Missing name with second letter of: t', str(err.exception))
        # Test that it raises an IndexError for the third letter.
        name_list = ['Fill', 'Fuller', 'Stout', 'Filler']
        with self.assertRaises(IndexError) as err:
            encode_null.encode_null(message, name_list)
        self.assertEqual('Missing name with third letter of: e', str(err.exception))
        # Test that it encodes a cipherlist.
        name_list = ['Loki', 'Sampson', 'Lemon', 'Stout', 'Ruth',
                     'Egg', 'Vest', 'Lisa', 'Lee', 'Tsar', 'Smoke']
        testlist = encode_null.encode_null(message, name_list)
        answerlist = ['Loki', 'Stout', 'Lee', 'Tsar', 'Scrooge',
                      'Ruth', 'Smoke', 'Nero', 'Vest', 'Egg']
        self.assertListEqual(testlist, answerlist)


if __name__ == '__main__':
    unittest.main()
