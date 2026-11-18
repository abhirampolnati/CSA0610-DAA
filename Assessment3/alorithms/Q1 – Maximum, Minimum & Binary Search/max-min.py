def find_max_min(arr, low, high):

    # Base case: Only one element
    if low == high:
        return arr[low], arr[low]

    # Base case: Two elements
    if high == low + 1:
        if arr[low] > arr[high]:
            return arr[low], arr[high]
        else:
            return arr[high], arr[low]

    # Divide the array
    mid = (low + high) // 2

    # Conquer
    max1, min1 = find_max_min(arr, low, mid)
    max2, min2 = find_max_min(arr, mid + 1, high)

    # Combine
    maximum = max(max1, max2)
    minimum = min(min1, min2)

    return maximum, minimum


arr = [45, 12, 89, 23, 67, 5, 91, 34]

maximum, minimum = find_max_min(arr, 0, len(arr) - 1)

print("Array:", arr)
print("Maximum element:", maximum)
print("Minimum element:", minimum)
