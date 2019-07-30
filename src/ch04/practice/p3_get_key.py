"""Get route cipher key from user and store as dictionary."""


def key_to_dict(keys: list) -> dict:
    """Convert route cipher key to dictionary.

    Take a route cipher key in list format where integers are column numbers
    and positive/negative is the route direction and convert to a dictionary
    where the column numbers are keys and the route direction as
    ``up``/``down`` are the values.

    Args:
        keys (list): List of integers with direction as positive/negative.

    Returns:
        Integers keys and ``up``/``down`` as values.

    """


def get_key() -> list:
    """Get route cipher key from user.

    User only has to enter positive/negative integers. Each gets added to a
    list and returned when the user has no other keys to add.

    Returns:
        List of integers as column numbers and positive/negative values as
        route direction.

    """


def main():
    """Demonstrate getting route cipher keys from the user."""


if __name__ == '__main__':
    main()
