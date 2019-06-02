import random


def get_min_max_by_sorting(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    init_val = None
    if len(ints) > 0:
        init_val = ints[0]
    min_value = init_val
    max_value = init_val
    for i in ints:
        if i < min_value:
            min_value = i

        if i > max_value:
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

# negative inputs
print("Pass" if ((-2, 3) == get_min_max_by_sorting(
    [3, 3, 1, -1, 1, -2])) else "Fail")
