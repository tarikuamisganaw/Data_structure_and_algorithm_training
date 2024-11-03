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
    else:
        largest = i
    # Update largest if right child is greater    
    if r < n and arr[r] > arr[largest]:
        largest = r
    """
    If largest is not the current index, swap and recursively 
    apply max-heapify on the largest index.
    """ 
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)
# Test the max-heapify function
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
max_heapify(arr, n, 0)
print(arr)