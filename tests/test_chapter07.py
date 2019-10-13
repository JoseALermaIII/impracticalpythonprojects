"""Test Chapter 7."""
import unittest.mock
import os
from random import Random
from io import StringIO

import src.ch07.c1_breed_rats as breed_rats
import src.ch07.c2_safe_cracker as safe_cracker


class TestBreedRats(unittest.TestCase):
    """Test Breed Rats."""

    @classmethod
    def setUpClass(cls):
        """Configure attributes for use in this class only."""
        cls.random = Random()

    def test_properties(self):
        """Test properties."""
        experiment = breed_rats.BreedRats()

        # Test default property values.
        self.assertEqual(experiment.num_males, 4)
        self.assertEqual(experiment.num_females, 16)
        self.assertEqual(experiment.target_wt, 50000)
        self.assertEqual(experiment.gen_limit, 500)
        self.assertEqual(experiment.min_wt, 200)
        self.assertEqual(experiment.max_wt, 600)
        self.assertEqual(experiment.male_mode_wt, 300)
        self.assertEqual(experiment.female_mode_wt, 250)
        self.assertEqual(experiment.mut_odds, 0.01)
        self.assertEqual(experiment.mut_min, 0.5)
        self.assertEqual(experiment.mut_max, 1.2)
        self.assertEqual(experiment.litters_per_yr, 10)
        self.assertEqual(experiment.litter_sz, 8)

        # Test setters.
        experiment.num_males = 10
        self.assertEqual(experiment.num_males, 10)
        experiment.num_females = 20
        self.assertEqual(experiment.num_females, 20)
        experiment.target_wt = 20000
        self.assertEqual(experiment.target_wt, 20000)
        experiment.gen_limit = 200
        self.assertEqual(experiment.gen_limit, 200)
        experiment.min_wt = 250
        self.assertEqual(experiment.min_wt, 250)
        experiment.max_wt = 700
        self.assertEqual(experiment.max_wt, 700)
        experiment.male_mode_wt = 400
        self.assertEqual(experiment.male_mode_wt, 400)
        experiment.female_mode_wt = 300
        self.assertEqual(experiment.female_mode_wt, 300)
        experiment.mut_odds = 0.93
        self.assertEqual(experiment.mut_odds, 0.93)
        experiment.mut_min = 2.5
        self.assertEqual(experiment.mut_min, 2.5)
        experiment.mut_max = 3.0
        self.assertEqual(experiment.mut_max, 3.0)
        experiment.litters_per_yr = 8
        self.assertEqual(experiment.litters_per_yr, 8)
        experiment.litter_sz = 3
        self.assertEqual(experiment.litter_sz, 3)

    @unittest.mock.patch('src.ch07.c1_breed_rats.random')
    def test_populate(self, mock_random):
        """Test populate."""
        # Patch random.triangular to use non-random seed.
        self.random.seed(512)
        mock_random.triangular._mock_side_effect = self.random.triangular
        experiment = breed_rats.BreedRats()
        experiment.min_wt = 100
        experiment.max_wt = 300
        test_pop = experiment.populate(10, 200)
        expected_pop = [119, 193, 181, 190, 261, 190, 158, 169, 109, 229]
        self.assertListEqual(test_pop, expected_pop)

    def test_combine_values(self):
        """Test combine_values."""
        dictionary = {
            'first': [1, 2, 3, 4, 5],
            'second': [6, 7, 8, 9, 0]
        }
        experiment = breed_rats.BreedRats()
        combined = experiment.combine_values(dictionary)
        expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
        self.assertListEqual(combined, expected)

    def test_measure(self):
        """Test measure."""
        population = {
            'males': [219, 293, 281, 290, 361, 290, 258, 269, 309, 329],
            'females': [119, 193, 181, 190, 261, 190, 158, 169, 109, 229]
        }
        experiment = breed_rats.BreedRats(target_wt=500)
        completion = experiment.measure(population)
        self.assertEqual(completion, 0.4698)

    def test_select(self):
        """Test select."""
        population = {
            'males': [219, 293, 281, 290, 361, 290, 258, 269, 309, 329],
            'females': [119, 193, 181, 190, 261, 190, 158, 169, 209, 229]
        }
        experiment = breed_rats.BreedRats()

        # Test even numbered populations.
        experiment.num_males = 2
        experiment.num_females = 2
        test_population = experiment.select(population)
        expected_population = {
            'males': [361, 329], 'females': [261, 229]
        }
        self.assertDictEqual(test_population, expected_population)
        experiment.num_males = 4
        experiment.num_females = 4
        test_population = experiment.select(population)
        expected_population = {
            'males': [361, 329, 309, 293], 'females': [261, 229, 209, 193]
        }
        self.assertDictEqual(test_population, expected_population)

        # Test odd numbered populations.
        experiment.num_males = 3
        experiment.num_females = 3
        test_population = experiment.select(population)
        expected_population = {
            'males': [361, 329, 309], 'females': [261, 229, 209]
        }
        self.assertDictEqual(test_population, expected_population)
        experiment.num_males = 5
        experiment.num_females = 5
        test_population = experiment.select(population)
        expected_population = {
            'males': [361, 329, 309, 293, 290],
            'females': [261, 229, 209, 193, 190]
        }
        self.assertDictEqual(test_population, expected_population)

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
        experiment = breed_rats.BreedRats()
        experiment.litter_sz = 8
        litter = experiment.crossover(population)
        expected_litter = {
            'males': [128, 148, 196, 197, 201, 206, 213, 214, 256, 269],
            'females': [120, 160, 170, 182, 187, 193, 196, 197, 203,
                        212, 215, 250, 251, 256]
        }
        self.assertDictEqual(litter, expected_litter)
        litter_total = sum([len(value) for value in litter.values()])
        self.assertEqual(litter_total,
                         experiment.litter_sz * len(population['females']))

        # Test fewer males than females.
        population = {
            'males': [219, 293],
            'females': [119, 193, 181]
        }
        litter = experiment.crossover(population)
        expected_litter = {
            'males': [165, 190, 208, 210, 245, 257, 280, 287],
            'females': [128, 140, 179, 181, 182, 182, 184, 187,
                        187, 194, 201, 206, 216, 241, 281, 290]
        }
        self.assertDictEqual(litter, expected_litter)
        litter_total = sum([len(value) for value in litter.values()])
        self.assertEqual(litter_total,
                         experiment.litter_sz * len(population['females']))

        # Test fewer females than males.
        population = {
            'males': [219, 293],
            'females': [119]
        }
        litter = experiment.crossover(population)
        expected_litter = {
            'males': [162, 201, 265],
            'females': [205, 228, 254, 261, 282]
        }
        self.assertDictEqual(litter, expected_litter)
        litter_total = sum([len(value) for value in litter.values()])
        self.assertEqual(litter_total,
                         experiment.litter_sz * len(population['females']))

        # Test different litter size.
        population = {
            'males': [219, 293],
            'females': [119]
        }
        experiment.litter_sz = 3
        litter = experiment.crossover(population)
        expected_litter = {
            'males': [167, 181],
            'females': [291]
        }
        self.assertDictEqual(litter, expected_litter)
        litter_total = sum([len(value) for value in litter.values()])
        self.assertEqual(litter_total,
                         experiment.litter_sz * len(population['females']))

        # Test larger female than males.
        population = {
            'males': [119, 193],
            'females': [219]
        }
        litter = experiment.crossover(population)
        expected_litter = {
            'males': [139, 150],
            'females': [119]
        }
        self.assertDictEqual(litter, expected_litter)
        litter_total = sum([len(value) for value in litter.values()])
        self.assertEqual(litter_total,
                         experiment.litter_sz * len(population['females']))

    @unittest.mock.patch('src.ch07.c1_breed_rats.random')
    def test_mutate(self, mock_random):
        """Test mutate."""
        # Patch random to use non-random seed.
        self.random.seed(311)
        mock_random.random._mock_side_effect = self.random.random
        mock_random.uniform._mock_side_effect = self.random.uniform

        experiment = breed_rats.BreedRats()

        # Test large litter with low mutation chance.
        litter = {
            'males': [165, 190, 208, 210, 245, 257, 280, 287],
            'females': [128, 140, 179, 181, 182, 182, 184, 187,
                        187, 194, 201, 206, 216, 241, 281, 290]
        }
        mutated_litter = experiment.mutate(litter)
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
        experiment.mut_odds = 0.90
        mutated_litter = experiment.mutate(litter)
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
        experiment.mut_min = 2.0
        experiment.mut_max = 3.0
        mutated_litter = experiment.mutate(litter)
        expected = {
            'males': [338, 442, 655],
            'females': [469, 666, 254, 612, 789]
        }
        self.assertDictEqual(mutated_litter, expected)

    @unittest.mock.patch('src.ch07.c1_breed_rats.random', new_callable=Random)
    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_simulate(self, mock_stdout, mock_random):
        """Test simulate."""
        # Patch random to use non-random seed.
        mock_random.seed(311)

        population = {
            'males': [450, 320, 510],
            'females': [250, 300, 220, 160]
        }
        experiment = breed_rats.BreedRats(num_males=3, num_females=10,
                                          target_wt=20000, gen_limit=500)
        experiment.mut_odds = 0.75
        experiment.mut_min = 0.75
        experiment.mut_max = 1.5
        ave, generations = experiment.simulate(population)
        self.assertEqual(generations, 12)
        self.assertEqual(ave, [347, 564, 861, 1181, 1636, 2344, 3319, 4950,
                               7234, 10464, 15115, 21703])

        # Test sys.stdout output.
        with open(os.path.normpath('tests/data/ch07/breed_rats.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        self.assertEqual(mock_stdout.getvalue(), file_data)

    @unittest.mock.patch('src.ch07.c1_breed_rats.time')
    @unittest.mock.patch('src.ch07.c1_breed_rats.random', new_callable=Random)
    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout, mock_random, mock_time):
        """Test main."""
        # Patch out variances.
        mock_random.seed(311)
        mock_time.time.side_effect = [12345, 67890]

        breed_rats.main()

        # Test sys.stdout output.
        with open(os.path.normpath('tests/data/ch07/main/breed_rats.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        self.assertEqual(mock_stdout.getvalue(), file_data)


class TestSafeCracker(unittest.TestCase):
    """Test Safe Cracker."""

    @classmethod
    def setUpClass(cls):
        """Configure attributes for use in this class only."""
        cls.random = Random()

    def test_compare(self):
        """Test compare."""
        list1 = [8]
        list2 = [8]
        test = safe_cracker.compare(list1, list2)
        self.assertEqual(test, 1)
        list1 = [8, 9]
        list2 = [8]
        test = safe_cracker.compare(list1, list2)
        self.assertEqual(test, 1)
        list1 = [8, 9]
        list2 = [8, 8]
        test = safe_cracker.compare(list1, list2)
        self.assertEqual(test, 1)
        list1 = [8, 9]
        list2 = [8, 9]
        test = safe_cracker.compare(list1, list2)
        self.assertEqual(test, 2)
        list1 = [8, 9, 7, 4, 5, 9, 0]
        list2 = [8, 8, 6, 3, 5, 8, 1]
        test = safe_cracker.compare(list1, list2)
        self.assertEqual(test, 2)
        list1 = [8, 9, 7, 4, 5, 9, 0]
        list2 = [8, 9, 7, 4, 5, 9, 0]
        test = safe_cracker.compare(list1, list2)
        self.assertEqual(test, 7)

    @unittest.mock.patch('src.ch07.c2_safe_cracker.random')
    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_crack_safe(self, mock_stdout, mock_random):
        """Test crack_safe."""
        # Patch random to use non-random seed.
        self.random.seed(211)
        mock_random.choice._mock_side_effect = self.random.choice
        mock_random.randint._mock_side_effect = self.random.randint

        combo = '8974590213'
        test, count = safe_cracker.crack_safe(combo)
        self.assertEqual(count, 110)
        self.assertEqual(combo, test)

        # Test sys.stdout output.
        with open(os.path.normpath('tests/data/ch07/safe_cracker.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        self.assertEqual(mock_stdout.getvalue(), file_data)

    @unittest.mock.patch('src.ch07.c2_safe_cracker.time')
    @unittest.mock.patch('src.ch07.c2_safe_cracker.random')
    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_main(self, mock_stdout, mock_random, mock_time):
        """Test main."""
        # Patch out variances.
        self.random.seed(111)
        mock_random.choice._mock_side_effect = self.random.choice
        mock_random.randint._mock_side_effect = self.random.randint
        mock_time.time.side_effect = [12345, 67890]

        safe_cracker.main()

        # Test sys.stdout output.
        with open(os.path.normpath('tests/data/ch07/main/safe_cracker.txt'),
                  'r') as file:
            file_data = ''.join(file.readlines())
        self.assertEqual(mock_stdout.getvalue(), file_data)


if __name__ == '__main__':
    unittest.main()
