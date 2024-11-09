import pytest
from max_heapify_verbatim_recursive import max_heapify 

def test_max_heapify_sorted_array():
    arr = [1, 2, 3, 4, 5]
    max_heapify(arr, len(arr), 0)
    assert arr == [3, 2, 1, 4, 5]  # Expected output after max_heapify

def test_max_heapify_reverse_sorted_array():
    arr = [5, 4, 3, 2, 1]
    max_heapify(arr, len(arr), 0)
    assert arr == [5, 4, 3, 2, 1]  # Expected output after max_heapify

def test_max_heapify_unsorted_array():
    arr = [3, 5, 1, 10, 2, 7]
    max_heapify(arr, len(arr), 0)
    assert arr == [5, 10, 1, 3, 2, 7]  # Expected output after max_heapify

def test_max_heapify_empty_array():
    arr = []
    max_heapify(arr, len(arr), 0)
    assert arr == []  # Empty array should remain empty

def test_max_heapify_single_element_array():
    arr = [42]
    max_heapify(arr, len(arr), 0)
    assert arr == [42]  # Single element should remain unchanged

def test_max_heapify_identical_elements():
    arr = [7, 7, 7, 7]
    max_heapify(arr, len(arr), 0)
    assert arr == [7, 7, 7, 7]  # Identical elements remain unchanged

if __name__ == "__main__":
    pytest.main()
