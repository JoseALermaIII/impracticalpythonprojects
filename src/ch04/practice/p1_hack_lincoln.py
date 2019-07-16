"""Hack route cipher sent by Abraham Lincoln."""


def get_factors(integer):
    """Get factors of integer.

    Calculate factors of a given integer.

    Args:
        integer (int): Number to get factors of.

    Returns:
        List of integer factors of **integer**.

    """
    result = []
    # A factor will always be less than or equal to sqrt(integer).
    for i in range(1, int(integer ** 0.5) + 1):
        if integer % i == 0:
            result.append(i)
            # If you have one factor, the other is integer / factor
            result.append(integer // i)
    return list(set(result))  # Eliminate perfect squares


def main():
    """Demonstrate hack of Lincoln's route cipher."""
    ciphertext = """THIS OFF DETAINED ASCERTAIN WAYLAND CORRESPONDENTS OF AT
    WHY AND IF FILLS IT YOU GET THEY NEPTUNE THE TRIBUNE PLEASE ARE THEM CAN 
    UP"""
