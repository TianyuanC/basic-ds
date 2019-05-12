import math


def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    lower = 0
    upper = len(input_list) - 1

    # locate the rotation pivot point
    found_pivot = False
    mid_pos = math.ceil(upper/2)
    pivot_pos = -1
    while lower < upper and not found_pivot:
        # quick validates
        if input_list[mid_pos] == number:
            return mid_pos

        # boundary check
        if mid_pos+1 < len(input_list) and input_list[mid_pos+1] < input_list[mid_pos]:
            pivot_pos = mid_pos
            found_pivot = True
            continue

        # search range updates
        if input_list[mid_pos] >= input_list[-1]:
            lower = mid_pos
            mid_pos = math.floor((mid_pos+upper)/2)
        else:
            upper = mid_pos
            mid_pos = math.floor((mid_pos+lower)/2)

    # adjust search range based on pivot point
    if pivot_pos == -1:
        lower = 0
        upper = len(input_list) - 1
    elif number > input_list[-1]:
        lower = 0
        upper = pivot_pos
    else:
        lower = pivot_pos + 1
        upper = len(input_list) - 1

    # binary search finally
    pos = -1
    mid_pos = math.ceil((lower + upper)/2)
    while lower <= upper:
        if input_list[mid_pos] == number:
            return mid_pos
        if lower == upper:
            return pos

        if input_list[mid_pos] > number:
            upper = mid_pos
            mid_pos = math.floor((lower + mid_pos)/2)
        else:
            lower = mid_pos
            mid_pos = math.ceil((upper + mid_pos)/2)
    return pos


def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1


def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")


# empty array
test_function([[], 10])
# single item array
test_function([[10], 10])

# non-exist upper bound
test_function([[6, 7, 8, 1, 2, 3, 4], 10])
# non-exist lower bound
test_function([[1, 2, 3, 4, 6, 7, 8, 9, 10], 0])
# non-rotation
test_function([[1, 2, 3, 4, 6, 7, 8, 9, 10], 6])

# rotated right away
test_function([[10, 1, 2], 10])
# rotated first partition
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
# rotated second partition
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
# rotated pivot point
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
