"""Efficiently breed rats to an average weight of 50000 grams.

Use genetic algorithm on a mixed population of male and female rats.

"""
import time
import random
import statistics


class BreedRats(object):
    """Efficiently breed rats to an average weight of **target_wt**.

    Use genetic algorithm on a mixed population of male and female rats.

    Weights and number of each gender vary and can be set by modifying the
    following:

    Args:
        num_males (int): Number of male rats in population.
            Default is ``4``.
        num_females (int): Number of female rats in population.
            Default is ``16``.
        target_wt (int): Target weight in grams. Default is ``50000``.
        gen_limit (int): Generational cutoff to stop breeding program.
            Default is ``500``.

    Attributes:
        _min_wt (int): Minimum weight of adult rat in initial population.
            Default is ``200``.
        _max_wt (int): Maximum weight of adult rat in initial population.
            Default is ``600``.
        _male_mode_wt (int): Most common adult male rat weight in initial
            population. Default is ``300``.
        _female_mode_wt (int): Most common adult female rat weight in initial
            population. Default is ``250``.
        _mut_odds (float): Probability of a mutation occurring in a pup.
            Default is ``0.01``.
        _mut_min (float): Scalar on rat weight of least beneficial mutation.
            Default is ``0.5``.
        _mut_max (float): Scalar on rat weight of most beneficial mutation.
            Default is ``1.2``.
        _litter_sz (int): Number of pups per pair of breeding rats.
            Default is ``8``.
        _litters_per_yr (int): Number of litters per year per pair of breeding rats.
            Default is ``10``.

    """
    def __init__(self, num_males: int = 4, num_females: int = 16,
                 target_wt: int = 50000, gen_limit: int = 500):
        self._min_wt = 200
        self._max_wt = 600
        self._male_mode_wt = 300
        self._female_mode_wt = 250
        self._mut_odds = 0.01
        self._mut_min = 0.5
        self._mut_max = 1.2
        self._litter_sz = 8
        self._litters_per_yr = 10

        self.num_males = num_males
        self.num_females = num_females
        self.target_wt = target_wt
        self.gen_limit = gen_limit

    @property
    def min_wt(self):
        """int: Minimum weight of adult rat in initial population."""
        return self._min_wt

    @min_wt.setter
    def min_wt(self, value: int):
        self._min_wt = value

    @property
    def max_wt(self):
        """int: Maximum weight of adult rat in initial population."""
        return self._max_wt

    @max_wt.setter
    def max_wt(self, value: int):
        self._max_wt = value

    @property
    def male_mode_wt(self):
        """int: Most common adult male rat weight in initial population."""
        return self._male_mode_wt

    @male_mode_wt.setter
    def male_mode_wt(self, value: int):
        self._male_mode_wt = value

    @property
    def female_mode_wt(self):
        """int: Most common adult female rat weight in initial population."""
        return self._female_mode_wt

    @female_mode_wt.setter
    def female_mode_wt(self, value: int):
        self._female_mode_wt = value

    @property
    def mut_odds(self):
        """float: Probability of a mutation occurring in a pup."""
        return self._mut_odds

    @mut_odds.setter
    def mut_odds(self, value: float):
        self._mut_odds = value

    @property
    def mut_min(self):
        """float: Scalar on rat weight of least beneficial mutation."""
        return self._mut_min

    @mut_min.setter
    def mut_min(self, value: float):
        self._mut_min = value

    @property
    def mut_max(self):
        """float: Scalar on rat weight of most beneficial mutation."""
        return self._mut_max

    @mut_max.setter
    def mut_max(self, value: float):
        self._mut_max = value

    @property
    def litter_sz(self):
        """int: Number of pups per pair of breeding rats."""
        return self._litter_sz

    @litter_sz.setter
    def litter_sz(self, value: int):
        self._litter_sz = value

    @property
    def litters_per_yr(self):
        """int: Number of litters per year per pair of breeding rats."""
        return self._litters_per_yr

    @litters_per_yr.setter
    def litters_per_yr(self, value: int):
        self._litters_per_yr = value

    def populate(self, pop_total: int, mode_wt: int) -> list:
        """Generate population with a triangular distribution of weights.

        Use :py:mod:`~random.triangular` to generate a population with a triangular
        distribution of weights based on **mode_wt**.

        Args:
            pop_total (int): Total number of rats in population.
            mode_wt (int): Most common adult rat weight in initial population.

        Returns:
            List of triangularly distributed weights of a given rat population.

        """
        return [int(random.triangular(self._min_wt, self._max_wt, mode_wt))
                for _ in range(pop_total)]

    def get_population(self, num_males: int = None,
                       num_females: int = None) -> dict:
        """Generate random population of rats.

        Wraps :func:`populate` using **num_males** and **num_females**.

        Args:
            num_males (int): Number of males in population.
                If :obj:`None`, defaults to instance value.
            num_females (int): Number of females in population.
                If :obj:`None`, defaults to instance value.

        Returns:
            Dictionary of lists with ``males`` and ``females`` as keys and
            specimen weight in grams as values.

        """
        if num_males is None:
            num_males = self.num_males
        if num_females is None:
            num_females = self.num_females
        population = {
            'males': self.populate(num_males, self._male_mode_wt),
            'females': self.populate(num_females, self._female_mode_wt)
        }
        return population

    @staticmethod
    def combine_values(dictionary: dict) -> list:
        """Combine dictionary values.

        Combine values in a dictionary of lists into one list.

        Args:
            dictionary (dict): Dictionary of lists.

        Returns:
            List containing all values that were in **dictionary**.

        """
        values = []
        for value in dictionary.values():
            values.extend(value)
        return values

    def measure(self, population: dict) -> float:
        """Measure average weight of population against target.

        Calculate mean weight of **population** and divide by **target_wt** to
        determine if goal has been met.

        Args:
            population (dict): Dictionary of lists with ``males`` and ``females``
                as keys and specimen weight in grams as values.

        Returns:
            :py:obj:`float` representing decimal percentage of completion where a
            value of ``1`` is ``100%``, or complete.

        """
        mean = statistics.mean(self.combine_values(population))
        return mean / self.target_wt

    def select(self, population: dict) -> dict:
        """Select largest members of population.

        Sort members in descending order, and then keep largest members up to
        instance values for **num_males** and **num_females**.

        Args:
            population (dict): Dictionary of lists with ``males`` and ``females``
                as keys and specimen weight in grams as values.

        Returns:
            Dictionary of lists of specified length of largest members of
            **population**.

        Examples:
            >>> from src.ch07.c1_breed_rats import BreedRats
            >>> sample_one = BreedRats(num_males = 4, num_females = 4)
            >>> s1_population = sample_one.get_population(num_males = 5,
            ...                                           num_females = 10)
            >>> selected_population = sample_one.select(s1_population)
            >>> print(selected_population)
            {'males': [555, 444, 333, 222], 'females': [999, 888, 777, 666]}

        """
        new_population = {'males': [], 'females': []}
        for gender in population:
            if gender == 'males':
                new_population[gender].extend(sorted(population[gender],
                                                     reverse=True)[:self.num_males])
            else:
                new_population[gender].extend(sorted(population[gender],
                                                     reverse=True)[:self.num_females])
        return new_population

    def crossover(self, population: dict) -> dict:
        """Crossover genes among members (weights) of a population.

        Breed **population** where each breeding pair produces a litter
        of instance value for **_litter_sz** pups. Pup's gender is assigned
        randomly.

        To accommodate mismatched pairs, breeding pairs are selected randomly,
        and once paired, females are removed from the breeding pool while
        males remain.

        Args:
            population (dict): Dictionary of lists with ``males`` and ``females``
                as keys and specimen weight in grams as values.

        Returns:
            Dictionary of lists with ``males`` and ``females`` as keys and
            pup weight in grams as values.

        """
        males = population['males']
        females = population['females'].copy()
        litter = {'males': [], 'females': []}
        while females:
            male = random.choice(males)
            female = random.choice(females)
            for pup in range(self._litter_sz):
                larger, smaller = male, female
                if female > male:
                    larger, smaller = female, male
                pup = random.randint(smaller, larger)
                if random.choice([0, 1]):
                    litter['males'].append(pup)
                else:
                    litter['females'].append(pup)
            females.remove(female)
        # Sort output for test consistency.
        for value in litter.values():
            value.sort()
        return litter

    def mutate(self, litter):
        """Randomly alter pup weights applying input odds as a scalar.

        For each pup in **litter**, randomly decide if a floating point number
        between instance values for **_mut_min** and **_mut_max** from
        :py:mod:`~random.uniform` will be used as a scalar to modified their
        weight.

        Args:
            litter (dict): Dictionary of lists with ``males`` and ``females``
                as keys and specimen weight in grams as values.

        Returns:
            Same dictionary of lists with weights potentially modified.

        """
        for gender in litter:
            pups = litter[gender]
            for index, pup in enumerate(pups):
                if self._mut_odds >= random.random():
                    pups[index] = round(pup * random.uniform(self._mut_min, self._mut_max))
        return litter

    def breed_rats(self, population: dict) -> tuple:
        """Simulate genetic algorithm by breeding rats.

        Using **population**, repeat cycle of measure, select, crossover,
        and mutate until either of **limits** are met.

        Args:
            population (dict): Dictionary of lists with ``males`` and ``females``
                as keys and specimen weight in grams as values.

        Returns:
            Tuple containing list of average weights of generations and number
            of generations before meeting target weight or generation limit in
            **limits**.

        Examples:
            >>> from src.ch07.c1_breed_rats import BreedRats
            >>> sample_one = BreedRats()
            >>> s1_population = sample_one.get_population()
            >>> ave_wt, generations = sample_one.breed_rats(s1_population)
            >>> print(generations)
            248

        """
        generations = 0
        ave_wt = []
        match = self.measure(population)

        while match < 1 and generations < self.gen_limit:
            population = self.select(population)
            litter = self.crossover(population)
            litter = self.mutate(litter)
            for gender in litter:
                population[gender].extend(litter[gender])
            match = self.measure(population)
            print(f'Generation {generations} match: {match * 100:.4f}%')

            ave_wt.append(int(statistics.mean(self.combine_values(population))))
            generations += 1
        return ave_wt, generations


def main():
    """Demonstrate BreedRats class.

    Use default values to run a demonstration simulation and display time
    (in seconds) it took to run.

    """
    start_time = time.time()
    experiment = BreedRats()

    population = experiment.get_population()
    match = experiment.measure(population)
    print(f'Initial population: {population}')
    print(f'Initial population match: {match * 100}%')
    print(f'Number of males, females to keep: {experiment.num_males}, '
          f'{experiment.num_females}')
    ave_wt, generations = experiment.breed_rats(population)

    print(f'Average weight per generation: {ave_wt}')
    print(f'\nNumber of generations: {generations}')
    print(f'Number of years: {int(generations/experiment.litters_per_yr)}')

    end_time = time.time()
    duration = end_time - start_time
    print(f'Runtime for this program was {duration} seconds.')


if __name__ == '__main__':
    main()
