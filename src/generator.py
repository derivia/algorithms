from math import floor
import random
import time

random.seed(time.time())


def random_number(min: int, max: int) -> int:
    return floor(random.random() * (max - min) + min)


def random_string(length: int) -> str:
    letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    result = ""
    for _ in range(length):
        result += letters[random_number(0, len(letters))]
    return result


def random_number_array(
    min_num: int = -126, max_num: int = 125, length: int = 16
) -> list[int]:
    result = []
    for _ in range(length):
        result.append(random_number(min_num, max_num))
    return result


def random_string_array(length: int = 16) -> list[str]:
    result = []
    for _ in range(length):
        result.append(random_string(1))
    return result
