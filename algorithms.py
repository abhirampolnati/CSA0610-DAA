# DAA Assignment 1
# Student Record Retrieval System
# Algorithms: Linear Search, Recursive Binary Search, Hash Table Lookup


# --------------------------------------------------
# 1. LINEAR SEARCH
# --------------------------------------------------

def linear_search(student_records, target):
    """
    Searches for a student registration number one by one.
    Time Complexity: Best O(1), Average O(n), Worst O(n)
    """

    for i in range(len(student_records)):
        if student_records[i] == target:
            return i

    return -1


# --------------------------------------------------
# 2. RECURSIVE BINARY SEARCH
# --------------------------------------------------

def binary_search(student_records, target, left, right):
    """
    Searches a sorted list using recursion.
    Time Complexity: Best O(1), Average O(log n), Worst O(log n)
    The input list must be sorted.
    """

    if left > right:
        return -1

    middle = (left + right) // 2

    if student_records[middle] == target:
        return middle

    elif target < student_records[middle]:
        return binary_search(
            student_records, target, left, middle - 1
        )

    else:
        return binary_search(
            student_records, target, middle + 1, right
        )


# --------------------------------------------------
# 3. HASH TABLE LOOKUP
# --------------------------------------------------

def create_hash_table(student_records):
    """
    Creates a hash table using a Python dictionary.
    Expected construction time: O(n)
    """

    hash_table = {}

    for index, registration_number in enumerate(student_records):
        hash_table[registration_number] = index

    return hash_table


def hash_search(hash_table, target):
    """
    Retrieves a student using a hash table.
    Expected lookup time: O(1)
    Worst-case lookup time: O(n)
    """

    return hash_table.get(target, -1)


# --------------------------------------------------
# 4. TESTING THE THREE ALGORITHMS
# --------------------------------------------------

if __name__ == "__main__":

    # Sample student registration numbers
    student_records = [
        192472037,
        192472015,
        192472028,
        192472042,
        192472006,
        192472033,
        192472019
    ]

    target = 192472028

    # Linear Search
    linear_result = linear_search(student_records, target)

    # Binary Search requires sorted records
    sorted_records = sorted(student_records)

    binary_result = binary_search(
        sorted_records,
        target,
        0,
        len(sorted_records) - 1
    )

    # Hash Table Lookup
    hash_table = create_hash_table(student_records)
    hash_result = hash_search(hash_table, target)

    # Display results
    print("STUDENT RECORD RETRIEVAL SYSTEM")
    print("--------------------------------")

    print("Target Registration Number:", target)

    if linear_result != -1:
        print("Linear Search: Student Found")
    else:
        print("Linear Search: Student Not Found")

    if binary_result != -1:
        print("Binary Search: Student Found")
    else:
        print("Binary Search: Student Not Found")

    if hash_result != -1:
        print("Hash Table Lookup: Student Found")
    else:
        print("Hash Table Lookup: Student Not Found")
