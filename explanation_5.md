# Autocomplete with Tries

Using Trie data structure to arrange words and make word lookup and autocomplete efficient.

Each node will capture its children as well as a property to indicate if the current node is a complete word.

For autocomplete feature, we also need an internal array to keep track all suffixes needed to form a complete word.

## Time complexity

-   Insert. Imagine worst case, all nodes will be sitting on one branch, adding new node will be linear `O(n)`.

-   Find. Similar to above, worst case scenario, no branches, all linear time, `O(n)`.

-   Suffixes. All the sub nodes will be examined, and thus `O(n)`
