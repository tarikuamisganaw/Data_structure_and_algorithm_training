import pytest
from heap_sort import heap_sort

def test_sorted_array():
    arr = [1, 2, 3, 4, 5]
    heap_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_reverse_sorted_array():
    arr = [5, 4, 3, 2, 1]
    heap_sort(arr)
    assert arr == [1, 2, 3, 4, 5]

def test_unsorted_array():
    arr = [3, 5, 1, 10, 2, 7]
    heap_sort(arr)
    assert arr == [1, 2, 3, 5, 7, 10]

def test_empty_array():
    arr = []
    heap_sort(arr)
    assert arr == []

def test_single_element_array():
    arr = [42]
    heap_sort(arr)
    assert arr == [42]

def test_identical_elements():
    arr = [7, 7, 7, 7]
    heap_sort(arr)
    assert arr == [7, 7, 7, 7]

if __name__ == "__main__":
    pytest.main()
