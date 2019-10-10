"""Efficiently breed rats to an average weight of 50000 grams.

Use genetic algorithm on a mixed population of male and female rats.

Running :func:`main` will output demonstration simulation and the time (in
seconds) it took to run.

Weights and number of each gender vary and can be set by modifying the
following:

Attributes:
    TARGET_WT (int): Target weight in grams.
    NUM_MALES (int): Number of male rats in population.
    NUM_FEMALES (int): Number of female rats in population.
    INIT_MIN_WT (int): Minimum weight of adult rat in initial population.
    INIT_MAX_WT (int): Maximum weight of adult rat in initial population.
    INIT_MALE_MODE_WT (int): Most common adult male rat weight in initial
        population.
    INIT_FEMALE_MODE_WT (int): Most common adult female rat weight in initial
        population.
    MUT_ODDS (float): Probability of a mutation occurring in a pup.
    MUT_MIN (float): Scalar on rat weight of least beneficial mutation.
    MUT_MAX (float): Scalar on rat weight of most beneficial mutation.
    LITTER_SZ (int): Number of pups per pair of breeding rats.
    LITTERS_PER_YR (int): Number of litters per year per pair of breeding rats.
    GEN_LIMIT (int): Generational cutoff to stop breeding program.

"""
import time
import random
import statistics

# CONSTANTS (weights in grams)
TARGET_WT = 50000  # Target weight in grams.
NUM_MALES = 4  # Number of male rats in population.
NUM_FEMALES = 16  # Number of female rats in population.
INIT_MIN_WT = 200  # Minimum weight of adult rat in initial population.
INIT_MAX_WT = 600  # Maximum weight of adult rat in initial population.
INIT_MALE_MODE_WT = 300  # Most common adult male rat weight.
INIT_FEMALE_MODE_WT = 250  # Most common adult female rat weight.
MUT_ODDS = 0.01  # Probability of a mutation occurring in a pup.
MUT_MIN = 0.5  # Scalar on rat weight of least beneficial mutation.
MUT_MAX = 1.2  # Scalar on rat weight of most beneficial mutation.
LITTER_SZ = 8  # Number of pups per pair of breeding rats.
LITTERS_PER_YR = 10  # Number of litters per year per pair of breeding rats.
GEN_LIMIT = 500  # Generational cutoff to stop breeding program.


def populate(pop_total: int, minimum_wt: int,
             maximum_wt: int, mode_wt: int) -> list:
    """Generate population with a triangular distribution of weights.

    Use :py:mod:`~random.triangular` to generate a population with a triangular
    distribution of weights based on *minimum_wt*, *maximum_wt*, and *mode_wt*.

    Args:
        pop_total (int): Total number of rats in population.
        minimum_wt (int): Minimum weight of adult rat in initial population.
        maximum_wt (int): Maximum weight of adult rat in initial population.
        mode_wt (int): Most common adult rat weight in initial population.

    Returns:
        List of triangularly distributed weights of a given rat population.

    """
    return [int(random.triangular(minimum_wt, maximum_wt, mode_wt))
            for _ in range(pop_total)]


def measure(population: dict, target_wt: int) -> float:
    """Measure average weight of population against target.

    Calculate mean weight of **population** and divide by **target_wt** to
    determine if goal has been met.

    Args:
        population (dict): Dictionary of lists with ``males`` and ``females``
            as keys and specimen weight in grams as values.
        target_wt (int): Target average weight of population in grams.

    Returns:
        :py:obj:`float` representing decimal percentage of completion where a
        value of ``1`` is ``100%``, or complete.

    """
    # Combine genders into same list for measurement.
    total = []
    for value in population.values():
        total.extend(value)
    mean = statistics.mean(total)
    return mean / target_wt


def select(population: list, to_keep: int) -> list:
    """Select largest members of population.

    Sort members in descending order, and then keep largest members up to
    **to_keep**.

    Args:
        population (list): List of members (weights in grams) in population.
        to_keep (int): Number of members in population to keep.

    Returns:
        List of length **to_keep** of largest members of **population**.

    """
    return sorted(population, reverse=True)[:to_keep]


def crossover(population: dict, litter_sz: int) -> dict:
    """Crossover genes among members (weights) of a population.

    Breed population where each breeding pair produces a litter
    of **litter_sz** pups. Pup's gender is assigned randomly.

    To accommodate mismatched pairs, breeding pairs are selected randomly,
    and once paired, females are removed from the breeding pool while
    males remain.

    Args:
        population (dict): Dictionary of lists with ``males`` and ``females``
            as keys and specimen weight in grams as values.
        litter_sz (int): Number of pups per breeding pair of rats.

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
        for pup in range(litter_sz):
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


def mutate(litter, mut_odds, mut_min, mut_max):
    """Randomly alter pup weights applying input odds as a scalar.

    For each pup in **litter**, randomly decide if a floating point number
    between **mut_min** and **mut_max** from :py:mod:`~random.uniform` will
    be used as a scalar to modified their weight.

    Args:
        litter (dict): Dictionary of lists with ``males`` and ``females``
            as keys and specimen weight in grams as values.
        mut_odds (float): Probability of a mutation occurring in a pup.
        mut_min (float): Scalar on rat weight of least beneficial mutation.
        mut_max (float): Scalar on rat weight of most beneficial mutation.

    Returns:
        Same dictionary of lists with weights potentially modified.

    """
    for gender in litter:
        pups = litter[gender]
        for index, pup in enumerate(pups):
            if mut_odds >= random.random():
                pups[index] = round(pup * random.uniform(mut_min, mut_max))
    return litter


def main():
    """Simulate genetic algorithm.

    After initializing population, repeat cycle of measure, select, crossover,
    and mutate to meet goal of 50000 grams.

    """
    start_time = time.time()
    pass
    end_time = time.time()
    duration = end_time - start_time
    print(f'Runtime for this program was {duration} seconds.')


if __name__ == '__main__':
    main()
