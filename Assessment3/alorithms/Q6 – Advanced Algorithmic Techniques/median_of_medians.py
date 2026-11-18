def median_of_medians(arr, k):

    if k < 1 or k > len(arr):
        raise ValueError("Invalid value of k")

    if len(arr) <= 5:
        return sorted(arr)[k - 1]

    # Divide array into groups of five
    groups = [
        arr[i:i + 5]
        for i in range(0, len(arr), 5)
    ]

    # Find median of each group
    medians = []

    for group in groups:
        sorted_group = sorted(group)
        medians.append(sorted_group[len(sorted_group) // 2])

    # Find median of medians
    pivot = median_of_medians(
        medians,
        (len(medians) + 1) // 2
    )

    # Partition the array
    smaller = [x for x in arr if x < pivot]
    equal = [x for x in arr if x == pivot]
    greater = [x for x in arr if x > pivot]

    if k <= len(smaller):

        return median_of_medians(smaller, k)

    elif k <= len(smaller) + len(equal):

        return pivot

    else:

        return median_of_medians(
            greater,
            k - len(smaller) - len(equal)
        )


arr = [12, 3, 5, 7, 4, 19, 26, 1, 15, 8]

k = 4

result = median_of_medians(arr, k)

print("Original Array:", arr)
print("K value:", k)
print("Kth Smallest Element:", result)
