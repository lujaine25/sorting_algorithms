import random
import time
import matplotlib.pyplot as plt 

# Generates a random array based on size
def generate_arr(size: int):
    return [random.randint(0, size) for _ in range(size)]

# Measures the time taken to sort the array
def measure_sorting_time(sort_function, arr):
    arr_copy = arr.copy()
    start_time = time.perf_counter()
    sort_function(arr_copy)
    end_time = time.perf_counter()
    return (end_time - start_time) * 1000

# Bubble Sort
def bubble_sort(arr):
    sorted_flag = False
    while not sorted_flag:
        sorted_flag = True                                       # Best case : O(n) 
        for i in range(len(arr) - 1):                            # Worst/Average case : O(n^2)
            if arr[i] > arr[i + 1]:                              
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_flag = False

# Selection Sort
def selection_sort(arr):
    size = len(arr)
    for step in range(size):
        min_idx = step                                           # Best/Worst/Average case : O(n^2)
        for i in range(step + 1, size):
            if arr[i] < arr[min_idx]:
                min_idx = i
        arr[step], arr[min_idx] = arr[min_idx], arr[step]

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        temp = arr[i]
        j = i - 1                                                 # Best case : O(n)
        while j >= 0 and arr[j] > temp:                           # Worst/Average case : O(n^2)
            arr[j + 1] = arr[j] 
            j -= 1
        arr[j + 1] = temp

# Merge Sort
def merge_sort(arr):
    if len(arr) <= 1:
        return

    r = len(arr) // 2
    L = arr[:r]
    M = arr[r:]

    merge_sort(L)
    merge_sort(M)

    i = j = k = 0                                                  # Best/Worst/Average case : O(n log n)

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

# Quick Sort
def quick_sort(arr):
    if len(arr) <= 1: 
        return arr

    pivot_index = random.randint(0, len(arr) - 1)                   # Best/Average case : O(n log n)
    pivot = arr[pivot_index]                                        # Worst case : O(n^2) 

    left = [x for i, x in enumerate(arr) if x < pivot and i != pivot_index]  
    right = [x for i, x in enumerate(arr) if x >= pivot and i != pivot_index]  

    return quick_sort(left) + [pivot] + quick_sort(right)

        
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
        arr[i],arr[largest]=arr[largest],arr[i]                      # Best/Worst/Average case : O(n log n)
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

# Array sizes to test
array_sizes = [1000, 2000,10000,25000] 

# Arrays to store the time taken for each sorting algorithm
bubble_times = []
selection_times = []
insertion_times = []
merge_times = []
quick_times = []
heap_times = []

# For each array size, generate a random array and measure the time taken for each sorting algorithm and store it in the respective array
for size in array_sizes:
    random_array = generate_arr(size)

    bubble_times.append(measure_sorting_time(bubble_sort, random_array))
    selection_times.append(measure_sorting_time(selection_sort, random_array))
    insertion_times.append(measure_sorting_time(insertion_sort, random_array))
    merge_times.append(measure_sorting_time(merge_sort, random_array))
    quick_times.append(measure_sorting_time(quick_sort, random_array))
    heap_times.append(measure_sorting_time(heap_sort, random_array))

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(array_sizes, bubble_times, marker='o', linestyle='-', color='r', label="Bubble Sort")
plt.plot(array_sizes, selection_times, marker='s', linestyle='-', color='g', label="Selection Sort")
plt.plot(array_sizes, insertion_times, marker='d', linestyle='-', color='b', label="Insertion Sort")
plt.plot(array_sizes, merge_times, marker='x', linestyle='-', color='y', label="Merge Sort")
plt.plot(array_sizes, quick_times, marker='p', linestyle='-', color='m', label="Quick Sort")
plt.plot(array_sizes, heap_times, marker='^', linestyle='-', color='g', label="Heap Sort")

# Graph Labels & Title
plt.xlabel("Array Size")
plt.ylabel("Time (Milliseconds)")
plt.title("Sorting Algorithm Performance")
plt.legend()
plt.grid(True)

# Show the graph
plt.show()



