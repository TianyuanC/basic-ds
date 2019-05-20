# HTTPRouter using a Trie

Implementation details are very similar to [autocomplete](./explanation_5.md), which leverages the Trie data structure

In terms of time complexity, both `add_handle` and `lookup` should be `O(n)` considering the worst case scenario where all nodes are structured with no branches
