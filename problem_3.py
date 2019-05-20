def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    # Sort
    input_list.sort(reverse=True)
    # Fill the digits
    first = "0"
    second = "0"
    for index, digit in enumerate(input_list):
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
