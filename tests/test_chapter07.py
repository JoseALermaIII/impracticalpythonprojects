"""Test Chapter 7."""
import unittest.mock
from random import Random

import src.ch07.c1_breed_rats as breed_rats


class TestBreedRats(unittest.TestCase):
    """Test Breed Rats."""

    @classmethod
    def setUpClass(cls):
        """Configure attributes for use in this class only."""
        cls.random = Random(512)

    @unittest.mock.patch('src.ch07.c1_breed_rats.random')
    def test_populate(self, mock_random):
        """Test populate."""
        # Patch random.triangular to use non-random seed.
        mock_random.triangular._mock_side_effect = self.random.triangular
        test_pop = breed_rats.populate(10, 100, 300, 200)
        expected_pop = [119, 193, 181, 190, 261, 190, 158, 169, 109, 229]
        self.assertListEqual(test_pop, expected_pop)

    def test_measure(self):
        """Test measure."""
        population = {
            'males': [219, 293, 281, 290, 361, 290, 258, 269, 309, 329],
            'females': [119, 193, 181, 190, 261, 190, 158, 169, 109, 229]
        }
        completion = breed_rats.measure(population, 500)
        self.assertEqual(completion, 0.4698)

    def test_select(self):
        """Test select."""
        population = [219, 293, 281, 290, 361, 290, 258, 269, 309, 329]

        # Test even numbered populations.
        test_population = breed_rats.select(population, 2)
        expected_population = [361, 329]
        self.assertListEqual(test_population, expected_population)
        test_population = breed_rats.select(population, 4)
        expected_population = [361, 329, 309, 293]
        self.assertListEqual(test_population, expected_population)

        # Test odd numbered populations.
        test_population = breed_rats.select(population, 3)
        expected_population = [361, 329, 309]
        self.assertListEqual(test_population, expected_population)
        test_population = breed_rats.select(population, 5)
        expected_population = [361, 329, 309, 293, 290]
        self.assertListEqual(test_population, expected_population)


if __name__ == '__main__':
    unittest.main()
