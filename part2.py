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
    hybrid_merge_insertion(M,THRESHOLD)

    i = j = k = 0

    while i < len(L) and j < len(M):
        if L[i] < M[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = M[j]
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



arr = [9, 5, 2, 7, 1, 8, 3]
THRESHOLD = 3
hybrid_merge_insertion(arr, THRESHOLD)
print(arr)