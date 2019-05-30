"""Test Chapter 3."""
import unittest
import src.ch03.p1_digram_counter as digram_counter
from src.ch03 import GET_DIGRAMS_ERROR, COUNT_DIGRAMS_ERROR


class TestDigramCounter(unittest.TestCase):
    """Test Digram Counter."""

    def test_bad_type(self):
        """Test that it raises its errors."""
        with self.assertRaises(TypeError) as err:
            digram_counter.get_digrams(5)
            self.assertEqual(GET_DIGRAMS_ERROR, err.exception)
            digram_counter.count_digrams(6, [])
            self.assertEqual(COUNT_DIGRAMS_ERROR, err.exception)
            digram_counter.count_digrams(set(), 7)
            self.assertEqual(COUNT_DIGRAMS_ERROR, err.exception)

    def test_get_digrams(self):
        """Test that it can make a set of digrams."""
        digrams = {'ol', 'vo', 'ov', 'oo', 'vl', 'lo', 'vv', 'lv'}
        test_word = 'volvo'
        test_digrams = digram_counter.get_digrams(test_word)
        self.assertSetEqual(digrams, test_digrams)


if __name__ == '__main__':
    unittest.main()
