#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)Linear because execution increases with outputs


b)O(n^2) Because our loops or nested like a bird


c) its being called recursively and used in the same way as a for loop so its Linear

## Exercise II
Floors are in order so we can just use a binary search 

`def egg_search(arr,floor):
    low = 0
    high = len(arr) - 1
    while low <= high:
        middle = (low+high)/2
        if floor < arr[middle]:
            high = middle - 1
        elif floor> arr[middle]:
            low = middle + 1
        else:
            return middle
    return "Not found"`

    The Runtime is O(log(N)) aka log</br>
    And the Space Complexity is O(1) aka constant</br>

