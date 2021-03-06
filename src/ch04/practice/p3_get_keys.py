"""Get route cipher key from user and store as dictionary.

Note:
    Assumes vertical cipher routes.

"""


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
    dictionary = dict()
    for key in keys:
        if key < 0:
            # Negative key is 'down'
            dictionary[abs(key)] = 'down'
        else:
            # Positive key is 'up'
            dictionary[key] = 'up'
    return dictionary


def get_keys() -> list:
    """Get route cipher keys from user.

    User only has to enter positive/negative integers. Each gets added to a
    list and returned when the user has no other keys to add.

    Returns:
        List of integers as column numbers and positive/negative values as
        route direction.

    """
    cols = int(input('How many columns? '))
    keys = []
    while len(keys) < cols:
        key = int(input('Enter a signed integer key: '))
        keys.append(key)
    print(f'\nThis is the route cipher key: {keys}\n')
    return keys


def main():
    """Demonstrate getting route cipher keys from the user."""
    print('I can get a route cipher key from you and even turn it into a '
          'dictionary.\nHey, I have my niche!')
    print('\nFirst, the route cipher key:')
    keys = get_keys()
    print('Next, this is the same key as a dictionary:')
    print(key_to_dict(keys))


if __name__ == '__main__':
    main()
