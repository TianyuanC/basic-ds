import math


def merge(left, right):
    left_index = 0
    right_index = 0
    result = []
    while left_index < len(left) or right_index < len(right):
        if left_index == len(left):
            result.extend(right[right_index:len(right)])
            break
        if right_index == len(right):
            result.extend(left[left_index:len(left)])
            break

        if left[left_index] >= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1
    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = math.floor(len(arr)/2)
    left = arr[0:mid]
    right = arr[mid: len(arr)]
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
    return merge(left_sorted, right_sorted)


def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # Sort
    sorted_list = merge_sort(input_list)
    # Fill the digits
    first = "0"
    second = "0"
    for index, digit in enumerate(sorted_list):
        if index % 2 == 0:
            first += str(digit)
        else:
            second += str(digit)

    return int(first), int(second)


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")


# edge cases
test_function([[], [0, 0]])
test_function([[1], [1, 0]])
test_function([[1, 2], [2, 1]])

# with duplicates
test_function([[2, 2, 2, 2], [22, 22]])
test_function([[2, 2, 2, 2, 2], [222, 22]])

# normal cases
test_function([[1, 2, 4, 5], [52, 41]])
test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
