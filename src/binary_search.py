import random


def binary_search(arr, item):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


my_list = [my_list for my_list in range(random.randint(16, 100))]
print(my_list)
print(binary_search(my_list, int(input("Загадайте число: "))))
