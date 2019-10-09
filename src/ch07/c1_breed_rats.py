"""Efficiently breed rats to an average weight of 50000 grams.

Use genetic algorithm on a mixed population of male and female rats.

Running as a program will output simulation in :func:`main` and the time (in
seconds) it took to run the simulation.

Weights and number of each gender vary and can be set by modifying the
following:

Attributes:

"""
import time
import random
import statistics


def populate(pop_total, minimum_wt, maximum_wt, mode_wt):


def measure(population, target_wt):


def select(population, to_keep):


def crossover(males, females, litter_sz):


def mutate(children, mut_odds, mut_min, mut_max):


def main():
    """Simulate genetic algorithm.

    After initializing population, repeat cycle of measure, select, crossover,
    and mutate to meet goal of 50000 grams.

    """


if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    duration = end_time - start_time
    print("\nRuntime for this program was {} seconds.".format(duration))
