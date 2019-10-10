"""Efficiently breed rats to an average weight of 50000 grams.

Use genetic algorithm on a mixed population of male and female rats.

Running as a program will output simulation in :func:`main` and the time (in
seconds) it took to run the simulation.

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


def measure(population, target_wt):
    pass


def select(population, to_keep):
    pass


def crossover(males, females, litter_sz):
    pass


def mutate(children, mut_odds, mut_min, mut_max):
    pass


def main():
    """Simulate genetic algorithm.

    After initializing population, repeat cycle of measure, select, crossover,
    and mutate to meet goal of 50000 grams.

    """
    pass


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print("\nRuntime for this program was {} seconds.".format(duration))
