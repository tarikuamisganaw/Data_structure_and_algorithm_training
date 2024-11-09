import pytest
from heap_sort import max_heapify, heapify, heap_sort

def test_max_heapify():
    # Test max_heapify function with a subtree rooted at index 0
    arr = [3, 5, 1, 10, 2, 7]
    max_heapify(arr, len(arr), 0)
    # Check that max_heapify results in the maximum element at the root
    assert arr[0] >= arr[1], "max_heapify did not set the largest element at the root."
    assert arr[0] >= arr[2], "max_heapify did not set the largest element at the root."

def test_heapify():
    # Test heapify function to ensure it builds a max-heap
    arr = [3, 5, 1, 10, 2, 7]
    heapify(arr)
    # Check if the max-heap property holds for the entire array
    for i in range(len(arr) // 2):
        l = 2 * i + 1
        r = 2 * i + 2
        if l < len(arr):
            assert arr[i] >= arr[l], "heapify failed to maintain max-heap property at left child."
        if r < len(arr):
            assert arr[i] >= arr[r], "heapify failed to maintain max-heap property at right child."

def test_heap_sort():
    # Test heap_sort on different arrays to check sorting functionality
    arr = [3, 5, 1, 10, 2, 7]
    heap_sort(arr)
    assert arr == [1, 2, 3, 5, 7, 10], "heap_sort failed on unsorted input."

    arr = [1, 2, 3, 4, 5, 6]
    heap_sort(arr)
    assert arr == [1, 2, 3, 4, 5, 6], "heap_sort failed on already sorted input."

    arr = [10, 9, 8, 7, 6, 5]
    heap_sort(arr)
    assert arr == [5, 6, 7, 8, 9, 10], "heap_sort failed on reverse sorted input."

    arr = []
    heap_sort(arr)
    assert arr == [], "heap_sort failed on empty input."

    arr = [42]
    heap_sort(arr)
    assert arr == [42], "heap_sort failed on single-element input."

def test_heap_sort_duplicates():
    # Test heap_sort with an array containing duplicates
    arr = [4, 1, 3, 2, 4, 2]
    heap_sort(arr)
    assert arr == [1, 2, 2, 3, 4, 4], "heap_sort failed on input with duplicates."
