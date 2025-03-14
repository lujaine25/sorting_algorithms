import random
import time
import matplotlib.pyplot as plt


def generate_arr(size: int):
    return [random.randint(0, size) for _ in range(size)]

def measure_sorting_time(sort_function, arr):
    arr_copy = arr.copy()
    start_time = time.perf_counter()
    sort_function(arr_copy)
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000

def bubble_sort(arr: list[int]):
    sorted_flag = False
    while not sorted_flag:
        sorted_flag = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_flag = False


def selection_sort(array):
    size = len(array)
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if array[i] < array[min_idx]:
                min_idx = i
        array[step], array[min_idx] = array[min_idx], array[step]


def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > temp:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = temp

def merge_sort(arr):
    if len(arr) <= 1:
        return

    r = len(arr) // 2
    L = arr[:r]
    M = arr[r:]

    merge_sort(L)
    merge_sort(M)

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
        
# Heap Sort
def max_heapify(arr, i, size) :
    left=2*i+1
    right=2*i+2
    largest=i
    if left<size and arr[left] > arr[largest]:
        largest=left
    if right<size and arr[right]> arr[largest]:
        largest=right
    if i!=largest:
        arr[i],arr[largest]=arr[largest],arr[i]
        max_heapify(arr,largest,size)   

def buildMaxHeap(arr,size):
    for i in range(size //2 - 1, -1, -1):
        max_heapify(arr, i, size)

def heap_sort(arr):
    size=len(arr)
    buildMaxHeap(arr,size)
    for i in range(size -1, 0, -1):
        arr[0],arr[i]=arr[i],arr[0]
        max_heapify(arr,0,i)      

# Generate random array
array_sizes = [1000, 2000,10000,25000]
bubble_times = []
selection_times = []
insertion_times = []
merge_times = []
heap_times = []
for size in array_sizes:
    random_array = generate_arr(size)

    bubble_times.append(measure_sorting_time(bubble_sort, random_array))
    selection_times.append(measure_sorting_time(selection_sort, random_array))
    insertion_times.append(measure_sorting_time(insertion_sort, random_array))
    merge_times.append(measure_sorting_time(merge_sort, random_array))
    heap_times.append(measure_sorting_time(heap_sort, random_array))

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(array_sizes, bubble_times, marker='o', linestyle='-', color='r', label="Bubble Sort")
plt.plot(array_sizes, selection_times, marker='s', linestyle='-', color='g', label="Selection Sort")
plt.plot(array_sizes, insertion_times, marker='d', linestyle='-', color='b', label="Insertion Sort")
plt.plot(array_sizes, merge_times, marker='x', linestyle='-', color='y', label="Merge Sort")
plt.plot(array_sizes, heap_times, marker='^', linestyle='-', color='m', label="Heap Sort")

# Graph Labels & Title
plt.xlabel("Array Size")
plt.ylabel("Time (Milliseconds)")
plt.title("Sorting Algorithm Performance")
plt.legend()
plt.grid(True)

# Show the graph
plt.show()



