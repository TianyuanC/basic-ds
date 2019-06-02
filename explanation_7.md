# HTTPRouter using a Trie

Implementation details are very similar to [autocomplete](./explanation_5.md), which leverages the Trie data structure

## Time Complexity

`split_path` depends on the length of the route, and scanning for `/` so it is `O(n)`, where n is the length of the route.

Both `add_handle` and `lookup` should be `O(m*n)` considering the worst case scenario where all nodes are structured with no branches, where m is the length of the route and n is the number of nodes in the Trie

## Space Complexity

Let's assume the number of handlers are `m` and the length of each route is `n`, in the worst case scenario, each handler is distinct from each other and half of chars in the route are `/`, thus the space complexity will be `O(m*n)`
