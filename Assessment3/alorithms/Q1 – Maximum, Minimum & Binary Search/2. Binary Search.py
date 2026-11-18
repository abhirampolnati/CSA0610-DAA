def binary_search(arr, target):

    low = 0
    high = len(arr) - 1

    while low <= high:

        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            low = mid + 1

        else:
            high = mid - 1

    return -1


arr = [5, 12, 23, 34, 45, 67, 89, 91]

target = 67

result = binary_search(arr, target)

print("Array:", arr)

if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")
