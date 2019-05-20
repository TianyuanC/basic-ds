def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    zero_index = 0
    curr_index = 0
    two_index = len(input_list)-1
    while curr_index <= two_index:
        curr_val = input_list[curr_index]
        # 0
        if curr_val < 1:
            # swap zero to the left
            if zero_index < curr_index:
                input_list[curr_index], input_list[zero_index] = input_list[zero_index], input_list[curr_index]

            zero_index += 1
            curr_index += 1
            continue
        # 2
        if curr_val > 1:
            if input_list[two_index] > 1:
                two_index -= 1
                continue
            else:
                # swap two to the right
                input_list[curr_index], input_list[two_index] = input_list[two_index], input_list[curr_index]
                two_index -= 1
                continue
        # 1
        else:
            # just move
            curr_index += 1
    return input_list


def test_function(test_case):
    sorted_array = sort_012(test_case)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")


# empty and edge case
test_function([])
test_function([0, 0])
test_function([1, 1])
test_function([2, 2])
test_function([2, 1])

# random cases
test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2,
               2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])

# sorted and reverse cases
test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
test_function([2, 2, 2, 1, 1, 1, 0, 0, 0])
