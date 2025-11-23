from src.generator import random_number_array


def insertionsort(array: list[int]):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key


def run():
    array = random_number_array()
    print("Unsorted:", array)
    insertionsort(array)
    print("Sorted:", array)
