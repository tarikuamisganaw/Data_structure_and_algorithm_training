def max_heapify(arr, n, i):
    """
    Maintain the max-heap property for the subtree rooted at index i.

    Parameters:
    arr (list): The array representing the heap.
    n (int): The size of the heap.
    i (int): The index of the root of the subtree.
    """
    # Assume largest is the current index
    largest = i
    # Loop until no more swaps are needed
    for _ in range(n):
        # Find the indices of the left and right children of the current node
        l = 2 * largest + 1
        r = 2 * largest + 2
        # If the left child exists and is greater, update largest
        if l < n and arr[l] > arr[largest]:
            largest = l
        else:
            largest = i
        # If the right child exists and is greater, update largest
        if r < n and arr[r] > arr[largest]:
            largest = r
        """
        If the largest index is not equal to the current index, swap
        the current index with the largest index.
        """  
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            i = largest
        else: 
            break

# Test the max-heapify function
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
n = len(arr)
max_heapify(arr, n, 0)
print(arr)