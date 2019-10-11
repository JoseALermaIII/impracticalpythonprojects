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
    mean = statistics.mean(combine_values(population))
    return mean / target_wt


def select(population: dict, to_keep: tuple) -> dict:
    """Select largest members of population.

    Sort members in descending order, and then keep largest members up to
    **to_keep**.

    Args:
        population (dict): Dictionary of lists with ``males`` and ``females``
            as keys and specimen weight in grams as values.
        to_keep (tuple): Tuple of integers representing number of males
            and females in population to keep.

    Returns:
        Dictionary of lists of length **to_keep** of largest members of
        **population**.

    Examples:
        >>> from src.ch07.c1_breed_rats import select
        >>> NUM_MALES, NUM_FEMALES = 4, 5
        >>> population = {
        ...     'males': [111, 222, 333, 444, 555],
        ...     'females': [666, 777, 888, 999, 1, 2]}
        >>> print(select(population, (NUM_MALES, NUM_FEMALES)))
        {'males': [555, 444, 333, 222], 'females': [999, 888, 777, 666]}

    """
    new_population = {'males': [], 'females': []}
    for gender in population:
        num_males, num_females = to_keep
        if gender == 'males':
            new_population[gender].extend(sorted(population[gender],
                                                 reverse=True)[:num_males])
        else:
            new_population[gender].extend(sorted(population[gender],
                                                 reverse=True)[:num_females])
    return new_population


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


def breed_rats(population: dict, limits: tuple, pop_stats: tuple,
               mut_stats: tuple) -> tuple:
    """Simulate genetic algorithm by breeding rats.

    Using **population**, repeat cycle of measure, select, crossover,
    and mutate until either of **limits** are met.

    Args:
        population (dict): Dictionary of lists with ``males`` and ``females``
            as keys and specimen weight in grams as values.
        limits (tuple): Tuple of integers representing target weight
            (in grams) and generational cutoff to stop breeding program.
        pop_stats (tuple): Tuple of integers representing number of male
            rats in population, number of female rats in population, and
            number of pups per pair of breeding rats.
        mut_stats (tuple): Tuple of floats representing probability of a
            mutation occurring in a pup, scalar on pup weight of least
            beneficial mutation, and scalar on pup weight of most
            beneficial mutation.

    Returns:
        Tuple containing list of average weights of generations and number
        of generations before meeting **target_wt**.

    Examples:
        >>> from src.ch07.c1_breed_rats import populate, breed_rats
        >>> INIT_MIN_WT, INIT_MAX_WT = 200, 600
        >>> INIT_MALE_MODE_WT, INIT_FEMALE_MODE_WT = 300, 250
        >>> TARGET_WT, GEN_LIMIT = 50000, 500
        >>> NUM_MALES, NUM_FEMALES, LITTER_SZ = 4, 16, 8
        >>> MUT_ODDS, MUT_MIN, MUT_MAX = 0.01, 0.5, 1.2
        >>>     population = {
        ...         'males': populate(NUM_MALES, INIT_MIN_WT, INIT_MAX_WT,
        ...                           INIT_MALE_MODE_WT),
        ...         'females': populate(NUM_FEMALES, INIT_MIN_WT, INIT_MAX_WT,
        ...                             INIT_FEMALE_MODE_WT)
        ...     }
        >>> ave_wt, generations = breed_rats(population,
        ...                                  (TARGET_WT, GEN_LIMIT),
        ...                                  (NUM_MALES, NUM_FEMALES,
        ...                                   LITTER_SZ),
        ...                                  (MUT_ODDS, MUT_MIN, MUT_MAX))
        >>> print(generations)
        248

    """
    litter_sz = pop_stats[2]
    target_wt, gen_limit = limits
    mut_odds, mut_min, mut_max = mut_stats

    generations = 0
    ave_wt = []
    match = measure(population, target_wt)

    while match < 1 and generations < gen_limit:
        population = select(population, pop_stats[:2])
        litter = crossover(population, litter_sz)
        litter = mutate(litter, mut_odds, mut_min, mut_max)
        for gender in litter:
            population[gender].extend(litter[gender])
        match = measure(population, limits[0])
        print(f'Generation {generations} match: {match * 100:.4f}%')

        ave_wt.append(int(statistics.mean(combine_values(population))))
        generations += 1
    return ave_wt, generations


def main():
    """Demonstrate breed_rats function.

    Wrap :func:`populate` and :func:`breed_rats` with module
    constants and then display time to run.

    """
    start_time = time.time()

    population = {
        'males': populate(NUM_MALES, INIT_MIN_WT, INIT_MAX_WT,
                          INIT_MALE_MODE_WT),
        'females': populate(NUM_FEMALES, INIT_MIN_WT, INIT_MAX_WT,
                            INIT_FEMALE_MODE_WT)
    }
    match = measure(population, TARGET_WT)
    print(f'Initial population match: {match * 100}%')
    print(f'Number of males, females to keep: {NUM_MALES}, {NUM_FEMALES}')
    ave_wt, generations = breed_rats(population,
                                     (TARGET_WT, GEN_LIMIT),
                                     (NUM_MALES, NUM_FEMALES, LITTER_SZ),
                                     (MUT_ODDS, MUT_MIN, MUT_MAX))

    print(f'Average weight per generation: {ave_wt}')
    print(f'\nNumber of generations: {generations}')
    print(f'Number of years: {int(generations/LITTERS_PER_YR)}')

    end_time = time.time()
    duration = end_time - start_time
    print(f'Runtime for this program was {duration} seconds.')


if __name__ == '__main__':
    main()
