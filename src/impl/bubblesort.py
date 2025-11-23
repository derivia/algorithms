from src.generator import random_number_array


def bubblesort(array: list[int]):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]


def run():
    array = random_number_array()
    print("Unsorted:", array)
    bubblesort(array)
    print("Sorted", array)
