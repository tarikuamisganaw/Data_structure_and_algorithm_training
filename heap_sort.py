def max_heapify(arr, n, i):
    """
    Maintain the max-heap property for a subtree rooted at index i.
    
    Parameters:
    arr (list): The array representing the heap.
    n (int): The size of the heap.
    i (int): The index of the root of the subtree.
    """
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # Update largest if left child is greater
    if l < n and arr[l] > arr[largest]:
        largest = l
    # Update largest if right child is greater    
    if r < n and arr[r] > arr[largest]:
        largest = r

    # If largest is not the current index, swap and recursively apply max-heapify
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def heapify(arr):
    """
    Build a max heap from the given array.
    
    Parameters:
    arr (list): The array to be transformed into a max heap.
    """
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        max_heapify(arr, n, i)
       
def heap_sort(arr):
    """
    Sort an array in ascending order using the heap sort algorithm.
    
    Parameters:
    arr (list): The array to be sorted.
    """
    n = len(arr)
    heapify(arr)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)

# Test the heap sort
if __name__ == "__main__":
    arr = [3, 5, 1, 10, 2, 7]
    heap_sort(arr)
    print("Sorted array:", arr)
