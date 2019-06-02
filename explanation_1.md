# Square Root of an Integer

It is implemented with an variation of binary search, and it will stop until the lower or upper bound meets the middle point.

Due to the nature of the binary search, the complexity is `O(log(n))`

In terms of the space complexity, since we are keeping track of `high`, `low` and `mid` indexes and not relevant to the size of the input, it's `O(1)`
