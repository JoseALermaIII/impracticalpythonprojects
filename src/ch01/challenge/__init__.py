"""Chapter 1 Challenge Projects.

Attributes:
    ADD_KEYS_ERROR (str): String with :py:exc:`TypeError` for
        :func:`~c1_foreign_bar_chart.add_keys_to_dict`.
    SPLIT_NAME_LIST_ERROR (str): String with :py:exc:`TypeError` for
        :func:`~c2_name_generator.split_names`.
    SPLIT_NAME_EMPTY_ERROR (str): Sting with :py:exc:`ValueError` for
        :func:`~c2_name_generator.split_names`.
    ADD_NAME_TO_KEY_ERROR (str): String with :py:exc:`TypeError` for
        :func:`~c2_name_generator.add_name_to_key`.
    GENERATE_NAME_ERROR (str): String with :py:exc:`KeyError` for
        :func:`~c2_name_generator.generate_name`.
    BUILD_LIST_ERROR (str): String with :py:exc:`IndexError` for
        :func:`~c2_name_generator.build_name_list`.

"""

# Constants
ADD_KEYS_ERROR = 'Input must be a dictionary.'
SPLIT_NAME_LIST_ERROR = 'List of names must be a list or tuple.'
SPLIT_NAME_EMPTY_ERROR = 'List must not be empty.'
ADD_NAME_TO_KEY_ERROR = 'Name and key must be a string and dictionary must ' \
                        'be a dictionary.'
GENERATE_NAME_ERROR = 'Dictionary needs three keys.'
BUILD_LIST_ERROR = 'Folder must not be empty.'
