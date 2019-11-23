def binary_search(array, item):
    low = 0
    high = len(array) - 1

    while low <= high:
        mid = int((high + low) / 2)
        guess = array[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None


test_list = [1, 2, 3, 5]
print(binary_search(test_list, 3))
