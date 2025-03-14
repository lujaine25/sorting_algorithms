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

def bubble_sort(arr):
    sorted_flag = False
    while not sorted_flag:
        sorted_flag = True
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                sorted_flag = False


def selection_sort(arr):
    size = len(arr)
    for step in range(size):
        min_idx = step
        for i in range(step + 1, size):
            if arr[i] < arr[min_idx]:
                min_idx = i
        arr[step], arr[min_idx] = arr[min_idx], arr[step]


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

def quick_sort(arr):
    if len(arr) <= 1: 
        return arr

    pivot_index = random.randint(0, len(arr) - 1)  
    pivot = arr[pivot_index]  

    left = [x for i, x in enumerate(arr) if x < pivot and i != pivot_index]  
    right = [x for i, x in enumerate(arr) if x >= pivot and i != pivot_index]  

    return quick_sort(left) + [pivot] + quick_sort(right)

# Generate random array
array_sizes = [1000, 2000,10000,25000] # Array sizes to test
bubble_times = []
selection_times = []
insertion_times = []
merge_times = []
quick_times = []
for size in array_sizes:
    random_array = generate_arr(size)

    bubble_times.append(measure_sorting_time(bubble_sort, random_array))
    selection_times.append(measure_sorting_time(selection_sort, random_array))
    insertion_times.append(measure_sorting_time(insertion_sort, random_array))
    merge_times.append(measure_sorting_time(merge_sort, random_array))
    quick_times.append(measure_sorting_time(quick_sort, random_array))


# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(array_sizes, bubble_times, marker='o', linestyle='-', color='r', label="Bubble Sort")
plt.plot(array_sizes, selection_times, marker='s', linestyle='-', color='g', label="Selection Sort")
plt.plot(array_sizes, insertion_times, marker='d', linestyle='-', color='b', label="Insertion Sort")
plt.plot(array_sizes, merge_times, marker='x', linestyle='-', color='y', label="Merge Sort")
plt.plot(array_sizes, quick_times, marker='p', linestyle='-', color='m', label="Quick Sort")

# Graph Labels & Title
plt.xlabel("Array Size")
plt.ylabel("Time (Milliseconds)")
plt.title("Sorting Algorithm Performance")
plt.legend()
plt.grid(True)

# Show the graph
plt.show()
