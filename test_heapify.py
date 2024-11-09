import pytest
from heapify import heapify

def test_heapify_sorted_array():
    arr = [1, 2, 3, 4, 5]
    heapify(arr)
    assert arr == [5, 4, 3, 1, 2]

def test_heapify_reverse_sorted_array():
    arr = [5, 4, 3, 2, 1]
    heapify(arr)
    assert arr == [5, 4, 3, 2, 1]

def test_heapify_unsorted_array():
    arr = [3, 5, 1, 10, 2, 7]
    heapify(arr)
    assert arr == [10, 5, 7, 3, 2, 1]

def test_heapify_empty_array():
    arr = []
    heapify(arr)
    assert arr == []

def test_heapify_single_element_array():
    arr = [42]
    heapify(arr)
    assert arr == [42]

def test_heapify_identical_elements():
    arr = [7, 7, 7, 7]
    heapify(arr)
    assert arr == [7, 7, 7, 7]

if __name__ == "__main__":
    pytest.main()
