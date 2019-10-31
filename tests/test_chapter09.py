"""Test Chapter 9."""
import unittest.mock
import os
from random import Random

import src.ch09.p1_markov_haiku as markov_haiku


class TestMarkovHaiku(unittest.TestCase):
    """Test Markov Haiku."""

    @classmethod
    def setUpClass(cls):
        """Configure attributes for use in this class only."""
        cls.random = Random()

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
        # Test third order.
        test_dict = markov_haiku.get_markov_model(word_list, 3)
        expected = {'a cat a': ['dog'], 'cat a dog': ['cat'],
                    'a dog cat': ['ballou']}
        self.assertDictEqual(test_dict, expected)

    @unittest.mock.patch('src.ch09.p1_markov_haiku.random')
    def test_random_word(self, mock_random):
        """Test random_word."""
        self.random.seed(1234)
        mock_random.choice.side_effect = self.random.choice

        word_list = ['coding', 'time', 'an', 'illusion',
                     'dimension', 'unseen']
        # Test default max_syls.
        result = markov_haiku.random_word(word_list)
        self.assertTupleEqual(result, ('illusion', 3))
        # Test smaller max_syls.
        result = markov_haiku.random_word(word_list, 2)
        self.assertTupleEqual(result, ('coding', 2))
        # Test smallest max_syls.
        result = markov_haiku.random_word(word_list, 1)
        self.assertTupleEqual(result, ('an', 1))

    def test_next_words(self):
        """Test next_words."""
        # Test first order Markov model.
        markov_model = {'a': ['cat', 'dog', 'dimension'],
                        'cat': ['a', 'elusive'], 'dog': ['cat', 'sitter']}
        prefix = 'a'
        # Test target syllable count of 2.
        test_list = markov_haiku.next_words(prefix, markov_model, 2)
        expected = ['cat', 'dog']
        self.assertListEqual(test_list, expected)
        # Test target syllable count of 4.
        test_list = markov_haiku.next_words(prefix, markov_model, 4)
        expected = ['cat', 'dog', 'dimension']
        self.assertListEqual(test_list, expected)

        # Test second order Markov model.
        markov_model = {'a cat': ['sitter', 'groomer', 'fanatic'],
                        'a dog': ['cat'], 'dog cat': ['pound']}
        prefix = 'a cat'
        # Test target syllable count of 4.
        test_list = markov_haiku.next_words(prefix, markov_model, 4)
        expected = ['sitter', 'groomer']
        self.assertListEqual(test_list, expected)
        # Test target syllable count of 5.
        test_list = markov_haiku.next_words(prefix, markov_model, 5)
        expected = ['sitter', 'groomer', 'fanatic']
        self.assertListEqual(test_list, expected)

        # Test third order Markov model.
        markov_model = {'a cat a': ['dog', 'ferret', 'pet'],
                        'a dog cat': ['shelter']}
        prefix = 'a cat a'
        # Test target syllable count of 4.
        test_list = markov_haiku.next_words(prefix, markov_model, 4)
        expected = ['dog', 'pet']
        self.assertListEqual(test_list, expected)
        # Test target syllable count of 5.
        test_list = markov_haiku.next_words(prefix, markov_model, 5)
        expected = ['dog', 'ferret', 'pet']
        self.assertListEqual(test_list, expected)

        # Test low target syllable count.
        test_list = markov_haiku.next_words(prefix, markov_model, 3)
        expected = []
        self.assertListEqual(test_list, expected)
        # Test unlisted prefix.
        prefix = 'a cat dog'
        test_list = markov_haiku.next_words(prefix, markov_model, 4)
        expected = []
        self.assertListEqual(test_list, expected)

    @unittest.mock.patch('src.ch09.p1_markov_haiku.random')
    def test_haiku_line(self, mock_random):
        """Test haiku_line."""
        self.random.seed(5676)
        mock_random.choice.side_effect = self.random.choice

        word_list = ['a', 'cat', 'a', 'dog', 'cat', 'ballou']
        # Test line 1.
        line = markov_haiku.haiku_line('a', word_list, 5, is_first_line=True)
        expected = 'a dog cat ballou'
        self.assertEqual(line, expected)
        # Test line 2.
        end_prev = ' '.join(line.split()[-2:])
        line2 = markov_haiku.haiku_line(end_prev, word_list, 7)
        expected = 'dog ballou cat a dog cat'
        self.assertEqual(line2, expected)
        # Test line 3.
        end_prev = ' '.join(line2.split()[-2:])
        line3 = markov_haiku.haiku_line(end_prev, word_list, 5)
        expected = 'ballou ballou cat'
        self.assertEqual(line3, expected)


if __name__ == '__main__':
    unittest.main()
