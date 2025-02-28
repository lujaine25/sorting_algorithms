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


# Generate random array
array_sizes = [1000, 2000,10000,25000]
bubble_times = []
selection_times = []
insertion_times = []
for size in array_sizes:
    random_array = generate_arr(size)

    bubble_times.append(measure_sorting_time(bubble_sort, random_array))
    selection_times.append(measure_sorting_time(selection_sort, random_array))
    insertion_times.append(measure_sorting_time(insertion_sort, random_array))

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(array_sizes, bubble_times, marker='o', linestyle='-', color='r', label="Bubble Sort")
plt.plot(array_sizes, selection_times, marker='s', linestyle='-', color='g', label="Selection Sort")
plt.plot(array_sizes, insertion_times, marker='d', linestyle='-', color='b', label="Insertion Sort")

# Graph Labels & Title
plt.xlabel("Array Size")
plt.ylabel("Time (Milliseconds)")
plt.title("Sorting Algorithm Performance")
plt.legend()
plt.grid(True)

# Show the graph
plt.show()
