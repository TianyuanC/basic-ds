# Autocomplete with Tries

Using Trie data structure to arrange words and make word lookup and autocomplete efficient.

Each node will capture its children as well as a property to indicate if the current node is a complete word.

For autocomplete feature, we also need an internal array to keep track all suffixes needed to form a complete word.

## Time Complexity

-   TrieNode Insert. Imagine worst case, all nodes will be sitting on one branch, adding new node will be linear `O(n)`.

-   Trie Insert. Each char of of word need to be inserted to the Trie, it will be `O(n)`.

-   Find. Similar to above, worst case scenario, no branches, all linear time, `O(n)`.

-   Suffixes. All the sub nodes will be examined, and thus `O(n)`

## Space Complexity

Let's assume the number of words are `m` and the average length of the words are `n`, according to the Tries data structure, since we are saving on the char level, the space complexity will be `O(m*n)`
