def binary_search(arr, target):
    """
    Perform binary search on a sorted list to find the index of a target value.

    Args:
        arr (list): A list of sortable elements (must be sorted).
        target (Any): The value to search for.

    Returns:
        int: The index of the target if found, otherwise -1.
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def bubble_sort(arr):
    """
    Sort a list in ascending order using the bubble sort algorithm.

    Args:
        arr (list): A list of sortable elements.

    Returns:
        list: The sorted list.
    """
    n = len(arr)
    # Optimize by checking if any swap happened in the inner loop
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break
    
    return arr
