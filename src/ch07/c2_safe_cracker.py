"""Use hill-climbing algorithm to solve a lock combination.

Solve a lock combination by randomly changing a tumbler's values one
by one and noting whether the safe had a response. If so, lock the
tumbler at that value and continue randomly changing tumbler values.

Previously, a locked tumbler can still be changed, but the safe wouldn't
respond so, the change would be discarded. This improves upon the algorithm by
removing the locked tumbler from the pool of tumblers to randomly change.

"""
