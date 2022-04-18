"""
Created by hu-jinwen on 
"""


def find_min_and_max(source):
    """

    :param source:
    :return:
    """
    min_value = None
    max_value = None

    for i in source:
        if min_value is None:
            min_value = i
        if max_value is None:
            max_value = i

        if i < min_value:
            min_value = i
        if i > max_value:
            max_value = i

    return min_value, max_value


source_list = [9, 4, 6, 2, 8]

result = find_min_and_max(source_list)
print()
