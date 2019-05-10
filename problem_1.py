import math


def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    low = 0
    high = number
    mid = math.ceil(number/2)
    while low != mid and high != mid:
        if mid * mid == number:
            break
        elif mid * mid > number:
            high = mid
            mid = math.floor((low + mid) / 2)
        else:
            low = mid
            mid = math.floor((mid + high) / 2)
    return mid


print("Pass" if (0 == sqrt(0)) else "Fail")
print("Pass" if (1 == sqrt(1)) else "Fail")
print("Pass" if (1 == sqrt(2)) else "Fail")
print("Pass" if (2 == sqrt(4)) else "Fail")
print("Pass" if (3 == sqrt(9)) else "Fail")
print("Pass" if (4 == sqrt(16)) else "Fail")
print("Pass" if (5 == sqrt(27)) else "Fail")
print("Pass" if (10 == sqrt(101)) else "Fail")
print("Pass" if (56941 == sqrt(3242343667)) else "Fail")
