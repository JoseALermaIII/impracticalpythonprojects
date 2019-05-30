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


if __name__ == '__main__':
    unittest.main()
