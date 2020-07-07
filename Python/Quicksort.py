"""Implement quick sort in Python.
Input a list.
Output a sorted list."""
def quicksort(array):
    if len(array)<=1:
        return array
    else:
        pivot = array[-1]
        lesser, equal, greater = [], [], []
        for element in array:
            if element < pivot:
                lesser.append(element)
            elif element == pivot:
                equal.append(element)
            else:
                greater.append(element)
        return quicksort(lesser) + equal + quicksort(greater)

test = [21, 4, 1, 3, 9, 20, 25, 6, 21, 14]
print quicksort(test)

"""
Time Complexity: O(n^2) worst case / O(n*logn) average case
Memory Complexity: O(n)
"""
