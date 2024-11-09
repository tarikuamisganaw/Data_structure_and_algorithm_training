def max_heapify(arr, n, i):
    """
    Maintain the max-heap property for the subtree rooted at index i iteratively.

    Parameters:
    arr (list): The array representing the heap.
    n (int): The size of the heap.
    i (int): The index of the root of the subtree.
    """
    largest = i
    while True:
        left = 2 * largest + 1  # Left child index
        right = 2 * largest + 2  # Right child index
        swap = False

        # If the left child exists and is greater than the current largest
        if left < n and arr[left] > arr[largest]:
            largest = left
            swap = True

        # If the right child exists and is greater than the current largest
        if right < n and arr[right] > arr[largest]:
            largest = right
            swap = True

        # If the largest is still the current index, break the loop
        if not swap:
            break

        # Swap and continue heapifying
        arr[largest], arr[i] = arr[i], arr[largest]
        i = largest
