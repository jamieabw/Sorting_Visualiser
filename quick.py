import random

def quick_sort(arr, low, high):
    if low < high:
        # Partition the array
        pi = partition(arr, low, high)
        # Recursively sort left and right
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # We pick last element as pivot
    i = low - 1        # Pointer for smaller element
    return partitionStep(arr, low, high, pivot, i)
    


def partitionStep(arr, low, high, pivot, i, j=-1):
    if j == -1:
        j = low
    if j == high:
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    return partitionStep(arr, low, high, pivot, i, j+1)

# Example usage
lst = [random.randint(0, 100) for _ in range(15)]
print("Original:", lst)
quick_sort(lst, 0, len(lst) - 1)
print("Sorted:  ", lst)
