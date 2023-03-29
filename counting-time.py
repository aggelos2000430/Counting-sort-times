# Import the necessary packages
import random
import time
import matplotlib.pyplot as plt

# Import sorting algorithms from Εργασία01_1
from Εργασία01_1 import bubble_sort, quick_sort, merge_sort, selection_sort, insertion_sort, shell_sort, heap_sort

# Define function that generates an array of random integers between 0, 1.000.000
def generate_array(size):
    return [random.randint(0, 1000000) for _ in range(size)]

# Define function to measure execution time, using the time library, of every sorting algorithm one at a time
def measure_sorting_time(algorithm, array):
    start_time = time.time()
    algorithm(array)
    end_time = time.time()
    return end_time - start_time

# Define 10 scenarios for 100, 200, ... , 1000 integers that needs to be sorted using every algorithm imported from
# Εργασία01_1
scenarios = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Define a dictionary of the sorting algorithms
sorting_algorithms = {
    "bubble_sort": bubble_sort,
    "quick_sort": quick_sort,
    "merge_sort": merge_sort,
    "selection_sort": selection_sort,
    "insertion_sort": insertion_sort,
    "shell_sort": shell_sort,
    "heap_sort": heap_sort
}

# Measure sorting time for each scenario and algorithm exporting the results at the .txt file; given the parameters
# algorithm and array
with open("sorting_runtimes.txt", "w") as f:
    # Loop through the scenarios list in order to define the size of every scenario inside the .txt file
    for size in scenarios:
        array = generate_array(size)
        f.write(f"\nScenario with {size} integers:\n")
        # Loop through the sorting algorithms dictionary
        for name, algorithm in sorting_algorithms.items():
            time_taken = measure_sorting_time(algorithm, array)
            f.write(f"{name} - {time_taken:.6f} seconds:\n")

# Define the list sizes to test
list_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]

# Define a dictionary to store the runtimes for each algorithm
runtimes = {
    "bubble_sort": [],
    "quick_sort": [],
    "merge_sort": [],
    "selection_sort": [],
    "insertion_sort": [],
    "shell_sort": [],
    "heap_sort": []
}

# Measure the runtime of each algorithm on each list size
for size in list_sizes:
    # Generate a list of random integers
    arr = [random.randint(0, 1000000) for i in range(size)]

    # Measure the runtime of each algorithm
    start_time = time.time()
    bubble_sort(arr)
    end_time = time.time()
    # and append the result on the dicrionary
    runtimes["bubble_sort"].append(end_time - start_time)

    start_time = time.time()
    quick_sort(arr)
    end_time = time.time()
    runtimes["quick_sort"].append(end_time - start_time)

    start_time = time.time()
    merge_sort(arr)
    end_time = time.time()
    runtimes["merge_sort"].append(end_time - start_time)

    start_time = time.time()
    selection_sort(arr)
    end_time = time.time()
    runtimes["selection_sort"].append(end_time - start_time)

    start_time = time.time()
    insertion_sort(arr)
    end_time = time.time()
    runtimes["insertion_sort"].append(end_time - start_time)

    start_time = time.time()
    shell_sort(arr)
    end_time = time.time()
    runtimes["shell_sort"].append(end_time - start_time)

    start_time = time.time()
    heap_sort(arr)
    end_time = time.time()
    runtimes["heap_sort"].append(end_time - start_time)

# Create a chart, using matplotlib, of the runtimes for each algorithm on each list size
for algorithm in runtimes:
    plt.plot(list_sizes, runtimes[algorithm], label=algorithm)
plt.legend()
plt.xlabel("List Size")
plt.ylabel("Runtime (seconds)")
plt.show()