import heap_sort

def main():
    import random
    array = [random.randint(1, 100) for _ in range(10)]

    print(f"unsorted array: {array}")
    heap_sort.heap_sort(array)
    print(f"sorted array: {array}")

if __name__ == "__main__":
    main()