"""Test Chapter 7."""
import unittest.mock
from random import Random

import src.ch07.c1_breed_rats as breed_rats


class TestBreedRats(unittest.TestCase):
    """Test Breed Rats."""

    @classmethod
    def setUpClass(cls):
        """Configure attributes for use in this class only."""
        cls.random = Random()

    @unittest.mock.patch('src.ch07.c1_breed_rats.random')
    def test_populate(self, mock_random):
        """Test populate."""
        # Patch random.triangular to use non-random seed.
        self.random.seed(512)
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

    @unittest.mock.patch('src.ch07.c1_breed_rats.random')
    def test_crossover(self, mock_random):
        """Test crossover."""
        # Patch random to use non-random seed.
        self.random.seed(411)
        mock_random.choice._mock_side_effect = self.random.choice
        mock_random.randint._mock_side_effect = self.random.randint

        # Test equal males and females.
        population = {
            'males': [219, 293, 281],
            'females': [119, 193, 181]
        }
        litter_sz = 8
        litter = breed_rats.crossover(population, litter_sz)
        expected_litter = {
            'males': [128, 148, 196, 197, 201, 206, 213, 214, 256, 269],
            'females': [120, 160, 170, 182, 187, 193, 196, 197, 203,
                        212, 215, 250, 251, 256]
        }
        self.assertDictEqual(litter, expected_litter)
        litter_total = sum([len(value) for value in litter.values()])
        self.assertEqual(litter_total,
                         litter_sz * len(population['females']))

        # Test fewer males than females.
        population = {
            'males': [219, 293],
            'females': [119, 193, 181]
        }
        litter_sz = 8
        litter = breed_rats.crossover(population, litter_sz)
        expected_litter = {
            'males': [165, 190, 208, 210, 245, 257, 280, 287],
            'females': [128, 140, 179, 181, 182, 182, 184, 187,
                        187, 194, 201, 206, 216, 241, 281, 290]
        }
        self.assertDictEqual(litter, expected_litter)
        litter_total = sum([len(value) for value in litter.values()])
        self.assertEqual(litter_total,
                         litter_sz * len(population['females']))

        # Test fewer females than males.
        population = {
            'males': [219, 293],
            'females': [119]
        }
        litter_sz = 8
        litter = breed_rats.crossover(population, litter_sz)
        expected_litter = {
            'males': [162, 201, 265],
            'females': [205, 228, 254, 261, 282]
        }
        self.assertDictEqual(litter, expected_litter)
        litter_total = sum([len(value) for value in litter.values()])
        self.assertEqual(litter_total,
                         litter_sz * len(population['females']))

        # Test different litter size.
        population = {
            'males': [219, 293],
            'females': [119]
        }
        litter_sz = 3
        litter = breed_rats.crossover(population, litter_sz)
        expected_litter = {
            'males': [167, 181],
            'females': [291]
        }
        self.assertDictEqual(litter, expected_litter)
        litter_total = sum([len(value) for value in litter.values()])
        self.assertEqual(litter_total,
                         litter_sz * len(population['females']))

        # Test larger female than males.
        population = {
            'males': [119, 193],
            'females': [219]
        }
        litter_sz = 3
        litter = breed_rats.crossover(population, litter_sz)
        expected_litter = {
            'males': [139, 150],
            'females': [119]
        }
        self.assertDictEqual(litter, expected_litter)
        litter_total = sum([len(value) for value in litter.values()])
        self.assertEqual(litter_total,
                         litter_sz * len(population['females']))

    @unittest.mock.patch('src.ch07.c1_breed_rats.random')
    def test_mutate(self, mock_random):
        """Test mutate."""
        # Patch random to use non-random seed.
        self.random.seed(311)
        mock_random.random._mock_side_effect = self.random.random
        mock_random.uniform._mock_side_effect = self.random.uniform

        # Test large litter with low mutation chance.
        litter = {
            'males': [165, 190, 208, 210, 245, 257, 280, 287],
            'females': [128, 140, 179, 181, 182, 182, 184, 187,
                        187, 194, 201, 206, 216, 241, 281, 290]
        }
        mutated_litter = breed_rats.mutate(litter, 0.01, 0.5, 1.2)
        expected = {
            'males': [165, 190, 208, 210, 245, 257, 280, 287],
            'females': [128, 140, 179, 181, 182, 182, 184, 187,
                        187, 194, 201, 206, 216, 241, 281, 290]
        }
        self.assertDictEqual(mutated_litter, expected)

        # Test small litter with large mutation chance.
        litter = {
            'males': [162, 201, 265],
            'females': [205, 228, 254, 261, 282]
        }
        mutated_litter = breed_rats.mutate(litter, 0.90, 0.5, 1.2)
        expected = {
            'males': [95, 201, 265],
            'females': [179, 130, 267, 211, 261]
        }
        self.assertDictEqual(mutated_litter, expected)

        # Test small litter with large mutation chance and scale factor.
        litter = {
            'males': [162, 201, 265],
            'females': [205, 228, 254, 261, 282]
        }
        mutated_litter = breed_rats.mutate(litter, 0.90, 2.0, 3.0)
        expected = {
            'males': [338, 442, 655],
            'females': [469, 666, 254, 612, 789]
        }
        self.assertDictEqual(mutated_litter, expected)


if __name__ == '__main__':
    unittest.main()
