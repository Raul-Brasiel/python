def partition(array, left, right):
    pivot = array[right]
    i = left - 1
    for j in range(left, right):
        if array[j] >= pivot:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[right] = array[right], array[i + 1]
    return i + 1

def quicksort(array, left, right):
    if left < right:
        pivot_index = partition(array, left, right)
        quicksort(array, left, pivot_index - 1)
        quicksort(array, pivot_index + 1, right)

array = [10, 7, 8, 9, 1, 5]
print("Array original:", array)

quicksort(array, 0, len(array) - 1)
print("Array ordenado:", array)
