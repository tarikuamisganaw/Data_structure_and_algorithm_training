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
# Build a max heap from the given array
def heapify(arr):
    """
    Build a max heap from the given array.
    which changes a list to a heap order
    Parameters:
    arr (list): The array to be transformed into a max heap.
    """
    n = len(arr) 
    # Start from the last non-leaf node and go up to the root
    for i in range(n // 2, -1, -1):
        max_heapify(arr, n, i)  # Call max_heapify on the current node
# Test the heapify function
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
heapify(arr)
print(arr)        
