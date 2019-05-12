# Rotated Sorted Array Search

-   First use a variation of binary search to detect the rotation pivot point, by edge checking. Due to the binary search nature, it's `O(logN)`

-   After determining the pivot point, we can decide the search range again and giving it's sorted, we can apply binary search again, and that will be `O(logN)`

-   Thus, overall the complexity is `O(logN)`
