import random


def get_min_max_by_sorting(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    min_value = None
    max_value = None
    for i in ints:
        if min_value is None or i < min_value:
            min_value = i

        if max_value is None or i > max_value:
            max_value = i

    return (min_value, max_value)


# empty inputs
print("Pass" if ((None, None) == get_min_max_by_sorting([])) else "Fail")

# random inputs
l = [i for i in range(0, 10)]
random.shuffle(l)
print("Pass" if ((0, 9) == get_min_max_by_sorting(l)) else "Fail")

# duplicated inputs
print("Pass" if ((1, 3) == get_min_max_by_sorting(
    [3, 3, 1, 1, 1, 1])) else "Fail")
