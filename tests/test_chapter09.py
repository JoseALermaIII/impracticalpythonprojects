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

    def test_get_markov_model(self):
        """Test get_markov_model."""
        word_list = ['a', 'cat', 'a', 'dog', 'cat', 'ballou']
        # Test first order.
        test_dict = markov_haiku.get_markov_model(word_list, 1)
        expected = {'a': ['cat', 'dog'], 'cat': ['a', 'ballou'],
                    'dog': ['cat']}
        self.assertDictEqual(test_dict, expected)
        # Test second order.
        test_dict = markov_haiku.get_markov_model(word_list, 2)
        expected = {'a cat': ['a'], 'cat a': ['dog'], 'a dog': ['cat'],
                    'dog cat': ['ballou']}
        self.assertDictEqual(test_dict, expected)


if __name__ == '__main__':
    unittest.main()
