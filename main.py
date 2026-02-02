from algorithms import binary_search, bubble_sort

def example_binary_search():
    """
    Demonstrate binary search functionality.
    """
    print("--- Binary Search Example ---")
    sorted_list = [1, 3, 5, 7, 9, 11, 13, 15]
    target = 7
    print(f"List: {sorted_list}")
    print(f"Target: {target}")
    
    result = binary_search(sorted_list, target)
    
    if result != -1:
        print(f"Target found at index: {result}")
    else:
        print("Target not found")
    print()

def example_bubble_sort():
    """
    Demonstrate bubble sort functionality.
    """
    print("--- Bubble Sort Example ---")
    unsorted_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"Unsorted list: {unsorted_list}")
    
    sorted_list = bubble_sort(unsorted_list.copy())
    
    print(f"Sorted list:   {sorted_list}")
    print()

def main():
    """
    Main entry point to showcase functionality.
    """
    example_binary_search()
    example_bubble_sort()

if __name__ == "__main__":
    main()