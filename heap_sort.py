def heapify(arr, n, i): #helper method
    """heapifies the subtree rooted at index i, n is the size of arr"""
    largest = i #Assume current node is the largest
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])
        heapify(arr, n, largest)

def heap_sort(arr):
    """turns the array into a heap/tree, then calls the heapify function each time, swaps the root with the last element,
    then repeats the process until the whole heap is sorted in descending order"""
    n = len(arr)

    #last parent of the heap: at index n // 2 - 1
    for i in range(n // 2 - 1, -1, -1): #range(start(included), stop(excluded), step)
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])
        heapify(arr, i, 0) #third argument being 0 means heapify the entirety of heap