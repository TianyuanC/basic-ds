# Rearrange Array Elements

Given that array elements are from 0 to 9, we don't need to worry about double digits.

Simply sort the array, not matter there are duplicates or not, it shouldn't matter, and fill the two array from most significant digit to the least, one by one, until the array runs out.

The sorting itself will take `O(nLogN)` and the filling process will take `O(n)`, and thus the overall complexity will be `O(nLogN)`

In terms of the space complexity, since we sort the array and the sorting algorithm is not in-place, it will be `O(n)`
