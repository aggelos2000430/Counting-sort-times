import random
import time
import string
from Εργασία01_1 import bubble_sort, quick_sort, merge_sort, selection_sort, insertion_sort, shell_sort, heap_sort

# Define the data record structure
class Record:
    # the constructor method takes four arguments
    def __init__(self, number, string1, string2, string3):
        # and creates four attributes (self in python is used as "this" in Java)
        self.number = number
        self.string1 = string1
        self.string2 = string2
        self.string3 = string3
        # The try-except is used to handle the error that may occur when converting the string to an integer
        try:
            self.int_field = int(string1)
        # When an error occurs the int_field is set to 0
        except ValueError:
            self.int_field = 0

    # lt = "less than" operator
    # Takes two instances of the records class and compares them
    def __lt__(self, other):
        # Returns true if "self" is smaller than the "other", otherwise false
        return self.number < other.number

# Create 1000 records with random data
# creating the records list where we will store the generated data
records = []
for i in range(1000):
    # Creating random the random values
    number = random.randint(1, 1000000)
    name = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
    surname = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=10))
    city = ''.join(random.choices(['New York', 'London', 'Paris', 'Tokyo'], weights=[2, 2, 1, 1], k=1))
    # Create a new record object with the generated data
    record = Record(number, name, surname, city)
    # and add them to the list of records
    records.append(record)

def load_data(n):
    data = []
    for i in range(n):
        record = Record(random.randint(1, 100), generate_random_string(), generate_random_string(), generate_random_string())
        data.append(record)
    return data

def generate_random_string():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(10))

def measure_runtime(records, file_path):
    with open(file_path, 'a') as f:

            f.write(f'For data size:{size}, runtimes \n')
            start_time = time.time()
            bubble_sort(records)
            bubble_sort_time = time.time() - start_time
            f.write(f'Bubble Sort: {bubble_sort_time}\n')

            start_time = time.time()
            quick_sort(records)
            quick_sort_time = time.time() - start_time
            f.write(f'Quick Sort: {quick_sort_time}\n')

            start_time = time.time()
            merge_sort(records)
            merge_sort_time = time.time() - start_time
            f.write(f'Merge Sort: {merge_sort_time}\n')

            start_time = time.time()
            selection_sort(records)
            selection_sort_time = time.time() - start_time
            f.write(f'Selection Sort: {selection_sort_time}\n')

            start_time = time.time()
            insertion_sort(records)
            insertion_sort_time = time.time() - start_time
            f.write(f'Insertion Sort: {insertion_sort_time}\n')

            start_time = time.time()
            shell_sort(records)
            shell_sort_time = time.time() - start_time
            f.write(f'Shell Sort: {shell_sort_time}\n')

            start_time = time.time()
            heap_sort(records)
            heap_sort_time = time.time() - start_time
            f.write(f'Heap Sort: {heap_sort_time}\n')


    return [bubble_sort_time, quick_sort_time, merge_sort_time, selection_sort_time, insertion_sort_time, shell_sort_time, heap_sort_time]

def write_records_to_file(records, file_path):
    with open(file_path, 'w') as f:
        f.write('Number\tString1\tString2\tString3\tIntField\n')
        for record in records:
            f.write(f'{record.number}\t{record.string1}\t{record.string2}\t{record.string3}\t{record.int_field}\n')

data_sizes = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
runtimes = []

for size in data_sizes:
    data = load_data(1000)
    measure_runtime(data, 'runtimes.txt')

write_records_to_file(records, 'records.txt')

print(runtimes)
