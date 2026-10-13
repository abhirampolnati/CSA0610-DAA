# M3: Product Search
# ShopSphere Scalability Audit


# S1: Linear Search
def linear_search(products, target):
    comparisons = 0

    for i in range(len(products)):
        comparisons += 1

        if products[i] == target:
            return i, comparisons

    return -1, comparisons


# S2: Binary Search
# The input list must be sorted.
def binary_search(products, target):
    low = 0
    high = len(products) - 1
    comparisons = 0

    while low <= high:
        mid = (low + high) // 2
        comparisons += 1

        if products[mid] == target:
            return mid, comparisons
        elif target < products[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1, comparisons


# Sample sorted product catalogue
products = [101, 205, 310, 415, 520, 625, 730, 835]

target = 520

linear_index, linear_comparisons = linear_search(products, target)
binary_index, binary_comparisons = binary_search(products, target)

print("ShopSphere - Product Search")
print("---------------------------")

print("Target product ID:", target)

print("\nS1 - Linear Search")
print("Product index:", linear_index)
print("Comparisons:", linear_comparisons)

print("\nS2 - Binary Search")
print("Product index:", binary_index)
print("Comparisons:", binary_comparisons)
