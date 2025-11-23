def linearsearch(hay: list[int], needle: int) -> int:
    i = 0
    for _ in hay:
        if hay[i] == needle:
            return i
        i += 1
    return -1


def run(hay: list[int], needle: int):
    print(f"Found at index: {linearsearch(hay, needle)}")
