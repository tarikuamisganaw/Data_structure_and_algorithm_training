def max_heapify(arr, n, i):
    """
    Maintain the max-heap property for the subtree rooted at index i.

    Parameters:
    arr (list): The array representing the heap.
    n (int): The size of the heap.
    i (int): The index of the root of the subtree.
    """
    largest = i
    while True:
        l = 2 * largest + 1  # Left child index
        r = 2 * largest + 2  # Right child index

        # If the left child exists and is greater, update largest
        if l < n and arr[l] > arr[largest]:
            largest = l
        
        # If the right child exists and is greater, update largest
        if r < n and arr[r] > arr[largest]:
            largest = r

        # If largest is still the current index, break
        if largest == i:
            break
        
        # Swap and continue heapifying
        arr[i], arr[largest] = arr[largest], arr[i]
        i = largest
