"""Test Chapter 9."""
import unittest.mock
import os

import src.ch09.p1_markov_haiku as markov_haiku


class TestMarkovHaiku(unittest.TestCase):
    """Test Markov Haiku."""

    def test_prep_training(self):
        """Test prep_training."""
        file = os.path.normpath('tests/data/ch09/training.txt')
        test_list = markov_haiku.prep_training(file)
        expected = ['coding', 'can', 'be', 'fun',
                    'bugs', 'give', 'me', 'more', 'things', 'to', 'do',
                    'not', 'the', 'ones', 'that', 'crawl',
                    'time', 'an', 'illusion',
                    'in', 'a', 'dimension', 'unseen',
                    'what', 'does', 'it', 'look', 'like']
        self.assertListEqual(test_list, expected)


if __name__ == '__main__':
    unittest.main()
