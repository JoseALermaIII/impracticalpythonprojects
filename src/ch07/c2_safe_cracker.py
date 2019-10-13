"""Use hill-climbing algorithm to solve a lock combination.

Solve a lock combination by randomly changing a tumbler's values one
by one and noting whether the safe had a response. If so, lock the
tumbler at that value and continue randomly changing tumbler values.

Previously, a locked tumbler can still be changed, but the safe wouldn't
respond, so the change would be discarded. This improves upon the algorithm by
removing the locked tumbler from the pool of tumblers to randomly change.

"""
import time
import random


def compare(combo: list, attempt: list) -> int:
    """Compare items in two lists and count number of matches.

    Compare each element in **combo** with **attempt** and return
    the number of matches.

    Args:
        combo (list): Integers of safe combination.
        attempt (list): Integers of guessed safe combination.

    Returns:
        Number of combination matches between **combo** and **attempt**.

    """
    return sum(1 for i, j in zip(combo, attempt) if i == j)


def crack_safe(combo: str) -> tuple:
    """Crack a safe combination with a hill-climbing algorithm.

    Solve a lock combination by randomly changing a tumbler's values one
    by one and noting whether the safe had a response. If so, lock the
    tumbler at that value, remove it from the pool of tumblers, and
    continue randomly changing tumbler values.

    Args:
        combo (str): String of numbers representing combination of safe.

    Returns:
        Tuple with string of solved combination and number of attempts.

    """
    # Convert combo to list.
    combo = [int(i) for i in combo]

    # Make initial guess and compare.
    best_guess = [0] * len(combo)
    best_guess_match = compare(combo, best_guess)

    count = 0
    tumblers = list(range(len(combo)))

    # Evolve guess.
    while best_guess != combo:
        # Crossover.
        guess = best_guess.copy()

        # Mutate.
        lock_tumbler = random.choice(tumblers)
        guess[lock_tumbler] = random.randint(0, len(combo) - 1)

        # Compare and select.
        guess_match = compare(combo, guess)
        if guess_match > best_guess_match:
            best_guess = guess.copy()
            best_guess_match = guess_match
            tumblers.remove(lock_tumbler)
        print(guess, best_guess)
        count += 1
    return ''.join([str(i) for i in best_guess]), count


def main():
    """Demonstrate safe cracker.

    Use default combination to demonstrate :func:`crack_safe` and display time
    (in seconds) it took to run.

    """
    start_time = time.time()

    combination = '6822858902'
    print(f'Combination: {combination}')
    guess, count = crack_safe(combination)
    print(f'\nCracked! {guess} ')
    print(f'in {count} tries!')

    end_time = time.time()
    duration = end_time - start_time
    print(f'\nRuntime for this program was {duration:.5f} seconds.')


if __name__ == '__main__':
    main()
