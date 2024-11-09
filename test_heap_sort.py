from heap_sort import max_heapify, heap_sort

def test_max_heapify():
    # Test max_heapify function with a subtree rooted at index 0
    arr = [3, 5, 1, 10, 2, 7]
    max_heapify(arr, len(arr), 0)
    # Check if the largest of the root and its immediate children is at the root
    assert arr[0] == max(arr[0], arr[1], arr[2]), "max_heapify did not set the largest element at the root."

def test_heap_sort():
    # Test heap_sort function with an unsorted array
    arr = [3, 5, 1, 10, 2, 7]
    heap_sort(arr)
    # Verify if the array is sorted in ascending order
    assert arr == sorted(arr), "heap_sort did not sort the array correctly"
