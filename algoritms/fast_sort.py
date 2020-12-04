import random


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i < pivot]
        greater = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


arr = [random.randint(1, 54643) for i in range(10, 35)]
print(arr)
print(quicksort(arr))
