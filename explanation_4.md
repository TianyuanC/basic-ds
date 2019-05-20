# Dutch National Flag Problem

In order to sort array with single pass, we need to partition the array with three indexes, `curr_index` which keeps trace of 1, `zero_index` and `two_index`

The goal is to try to keep all 0s to the left by leveraging the `zero_index`, and the same applies to 2s by using the `two_index`.

The whole operation needs to iterate the array elements exactly once, so it is `O(n)`
