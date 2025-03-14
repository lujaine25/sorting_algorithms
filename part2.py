# Insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

def hybrid_merge_insertion (arr,THRESHOLD ):
    if len(arr) <= THRESHOLD:
        insertion_sort(arr)
        return

    r = len(arr) // 2
    L = arr[:r]
    M = arr[r:]

    hybrid_merge_insertion(L,THRESHOLD)
    hybrid_merge_insertion(M,THRESHOLD)                       # Best/Worst/Average case : O(n log n)

    i = j = k = 0                                             # Insertion sort is O(n^2) for worst case

    while i < len(L) and j < len(M):                          # This improves sorting time
        if L[i] < M[j]:                                       # as were using insertion sort which is faster for small arrays
            arr[k] = L[i]                                     # than merge sort since it needs extra time 
            i += 1                                            # money due to the recursive calls, memory allocations and computations
        else:                                                 # and that could be costly.
            arr[k] = M[j]                                     # This method reduces number of recursive calls.
            j += 1
        k += 1

    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    while j < len(M):
        arr[k] = M[j]
        j += 1
        k += 1

# Quick Sort partition
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def KthSmallest(arr, low, high, k):
    if k > 0 and k <= high - low + 1:
        index = partition(arr, low, high)

        if index - low == k - 1:
            return arr[index]

        elif index - low > k - 1:
            return KthSmallest(arr, low, index - 1, k)
        
        else:
            return KthSmallest(arr, index + 1, high, k - index + low - 1)


arr = [9, 5, 23, 7, 15, 8, 3, 6, 14]
THRESHOLD = 3
K = 8
print(str(K) + "th smallest element: " + str(KthSmallest(arr, 0, len(arr) - 1, K)))
hybrid_merge_insertion(arr, THRESHOLD)
print(arr)