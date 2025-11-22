from src.generator import random_number_array


def bubblesort(array: list[int]):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def run():
    array = random_number_array(length=10, min_num=1, max_num=100)
    print("Unsorted:", array)
    bubblesort(array)
    print("Sorted", array)
