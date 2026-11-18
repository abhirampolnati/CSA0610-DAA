from itertools import combinations
from bisect import bisect_left


def generate_subset_sums(arr):

    result = []

    n = len(arr)

    for r in range(n + 1):

        for indices in combinations(range(n), r):

            subset = [arr[i] for i in indices]

            result.append((sum(subset), subset))

    return result


def meet_in_middle(arr, target):

    n = len(arr)

    mid = n // 2

    left = arr[:mid]
    right = arr[mid:]

    # Generate subset sums
    left_sums = generate_subset_sums(left)
    right_sums = generate_subset_sums(right)

    # Sort right subset sums
    right_sums.sort(key=lambda x: x[0])

    right_values = [x[0] for x in right_sums]

    # Search for complementary sums
    for left_sum, left_subset in left_sums:

        required = target - left_sum

        index = bisect_left(right_values, required)

        if index < len(right_values):

            if right_values[index] == required:

                right_subset = right_sums[index][1]

                return left_subset + right_subset

    return None


arr = [3, 34, 4, 12, 5, 2]

target = 9

result = meet_in_middle(arr, target)

print("Array:", arr)
print("Target Sum:", target)

if result is not None:

    print("Subset Found:", result)
    print("Subset Sum:", sum(result))

else:

    print("No subset found")
