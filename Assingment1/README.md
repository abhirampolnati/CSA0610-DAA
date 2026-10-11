# CSA0610-DAA
# DESIGN AND ANALYSIS OF ALGORITHMS

## ASSIGNMENT 1

### STUDENT RECORD RETRIEVAL: DESIGN, ANALYSIS, AND VALIDATION

**Submitted by:** POLNATI ABHIRAMA KRISHNA
**Registration Number:** 192472037
**Department:** Computer Science and Engineering — Artificial Intelligence
**Subject:** Design and Analysis of Algorithms
**Assignment:** Assignment 1

---

# ABSTRACT

Student record retrieval is an important operation in educational institutions. A college database may contain thousands or even millions of student records, and administrative applications must retrieve a particular student's information efficiently using a unique registration number.

This project analyses three searching techniques: iterative linear search, recursive binary search, and hash-table lookup. Their algorithms, basic operations, time complexities, preprocessing requirements, and practical limitations are examined.

Python implementations of the three techniques can be evaluated using datasets of different sizes, ranging from 1,000 to 1,000,000 records. The performance evaluation should measure preprocessing and searching separately to provide a fair comparison.

The theoretical analysis indicates that linear search has linear-time complexity, binary search has logarithmic search complexity when the records are sorted, and hash-table lookup has expected constant-time complexity under suitable hashing conditions.

Considering the workload of 50,000 searches per hour and one daily batch of new records, this report recommends a hash-table index for exact-match student registration-number lookups, subject to memory availability, collision handling, and consistency requirements.

# 1. INTRODUCTION

Searching is a fundamental operation in computer science. It involves locating a required element within a collection of data.

In an educational institution, student records may contain registration numbers, student names, departments, course details, and academic information. When an administrator enters a registration number, the system must retrieve the corresponding record.

For a small dataset, a simple searching algorithm may be sufficient. However, as the number of records increases, the choice of algorithm can significantly affect performance.

This project compares three searching algorithms and analyses their suitability for student record retrieval.

## 1.1 Problem Statement

Design and analyse an efficient student record retrieval system capable of searching for a unique registration number in datasets containing between 1,000 and 1,000,000 or more records.

The revised system requirements specify 50,000 searches per hour, with new student records added in one daily batch.

The solution must compare different searching algorithms, analyse their theoretical complexities, implement them in Python, and evaluate their practical performance.

## 1.2 Objectives

1. Understand the operation of linear search, binary search, and hash-table lookup.
2. Identify the basic operation performed by each algorithm.
3. Derive the time-complexity functions mathematically.
4. Analyse the best, average, and worst cases.
5. Formulate and solve the recurrence relation for recursive binary search.
6. Implement and test the algorithms using Python.
7. Measure the performance of each algorithm on datasets of different sizes.
8. Compare theoretical predictions with measured results.
9. Recommend an appropriate searching strategy for the specified workload.

## 1.3 System Requirements

The system must satisfy the following requirements:

* Search using a unique student registration number.
* Support datasets containing up to one million records or more.
* Handle approximately 50,000 searches per hour.
* Support daily batch additions of new records.
* Provide correct results for existing and missing registration numbers.
* Allow performance comparison between different algorithms.

# 2. TASK 1 — DESIGN THE ALGORITHMS

Three algorithms are considered for student record retrieval.

## 2.1 Algorithm A: Iterative Linear Search

### Description

Linear search examines each record sequentially until the target registration number is found or the end of the dataset is reached.

It does not require the records to be sorted.

### Pseudocode

```
LINEAR-SEARCH(records, target)
    for i = 0 to length(records) - 1
        if records[i] = target
            return i
    return NOT_FOUND
```

### Advantages

* Simple to understand and implement.
* Works with sorted and unsorted data.
* Requires no preprocessing.
* Uses constant auxiliary space in its iterative implementation.

### Limitations

* May examine every record when the target is absent.
* Becomes inefficient for very large datasets.
* Repeated searches can result in substantial total work.

### Selection Justification

Linear search provides a useful baseline for comparing the performance of more advanced algorithms. It is appropriate for small datasets or situations where searches are infrequent.

## 2.2 Algorithm B: Recursive Binary Search

### Description

Binary search uses the divide-and-conquer approach. It compares the target with the middle element of a sorted dataset and recursively searches only the half that may contain the target.

The dataset must be sorted by registration number before binary search is performed.

### Pseudocode

```
RECURSIVE-BINARY-SEARCH(A, target, left, right)
    if left > right
        return NOT_FOUND

    mid = floor((left + right) / 2)

    if A[mid] = target
        return mid

    else if target < A[mid]
        return RECURSIVE-BINARY-SEARCH(
            A, target, left, mid - 1
        )

    else
        return RECURSIVE-BINARY-SEARCH(
            A, target, mid + 1, right
        )
```

### Advantages

* Efficient for sorted datasets.
* Reduces the search interval by approximately half at each step.
* Requires only logarithmically many comparisons.
* Suitable for repeated searches when sorted data is maintained.

### Limitations

* Requires sorted input.
* Initial sorting can be expensive.
* Maintaining a sorted array can make insertions costly.
* Recursive calls require additional stack space.

### Selection Justification

Binary search is suitable when student records are maintained in sorted order. Since the system receives new records only once daily, rebuilding or updating the sorted representation may be practical.

## 2.3 Algorithm C: Hash-Table Lookup

### Description

A hash table stores student records using registration numbers as keys. A hash function determines where a key is stored in the underlying table.

For a search request, the system uses the registration number to locate the corresponding entry.

### Pseudocode

```
BUILD-HASH-INDEX(records)
    index = empty hash table

    for each record in records
        index[record.registration_number] = record

    return index

HASH-SEARCH(index, target)
    if target is a key in index
        return index[target]

    return NOT_FOUND
```

### Advantages

* Expected constant-time lookup under suitable conditions.
* Well suited to frequent exact-match searches.
* Index construction can be performed once per daily batch.
* Can map registration numbers directly to student records.

### Limitations

* Requires additional memory.
* Performance depends on hashing and collision handling.
* Poor collision behaviour can lead to linear-time lookup.
* The index must be refreshed consistently after new records are added.

### Selection Justification

Hash-table lookup is a strong candidate because the system performs many searches between daily updates. The cost of building the index can be distributed across a large number of searches.

# 3. TASK 2 — IDENTIFY THE BASIC OPERATION

The basic operation is the fundamental operation whose repeated execution determines the algorithm's running time.

## 3.1 Linear Search

The basic operation is the equality comparison between the current registration number and the target.

For a missing target, the algorithm performs exactly n equality comparisons.

If the target occurs at zero-based position k, the algorithm performs k + 1 comparisons.

## 3.2 Recursive Binary Search

The basic operations are the comparisons between the target and the middle registration number.

Each unsuccessful recursive call reduces the candidate interval to approximately half its previous size.

Consequently, the number of comparisons grows logarithmically with the dataset size.

## 3.3 Hash-Table Lookup

The basic operation is the lookup of a key in the hash table.

This includes hashing the key and examining the relevant table location or collision-resolution structure.

Under suitable hashing conditions and a controlled load factor, expected lookup time is constant.

# 4. TASK 3 — MATHEMATICAL DERIVATION OF TIME COMPLEXITY

## 4.1 Linear Search

Let C(n) represent the number of equality comparisons.

### Best Case

The target is the first record.

C(n) = 1

Therefore, the best-case time complexity is Θ(1).

### Worst Case

The target is absent or occurs at the last position.

C(n) = n

Therefore, the worst-case time complexity is Θ(n).

### Average Case

Assume the target is equally likely to occur at any of the n positions.

The average number of comparisons is:

Cavg(n) = (1 + 2 + 3 + ... + n) / n

Using the arithmetic-series formula:

Cavg(n) = [n(n + 1) / 2] / n

Cavg(n) = (n + 1) / 2

Therefore, the average-case time complexity is Θ(n).

For q unsuccessful searches, the total number of comparisons can reach qn.

## 4.2 Recursive Binary Search

Let T(n) represent the worst-case searching time for n sorted records.

Each recursive call performs constant work and continues on at most half of the current interval.

The recurrence is:

T(n) = T(floor(n / 2)) + c

where c is a constant representing the work performed outside the recursive call.

After k halvings, the remaining interval has size approximately:

n / 2^k

The recursion stops when:

n / 2^k ≤ 1

Therefore:

2^k ≥ n

Taking logarithms:

k ≥ log₂(n)

Thus, the number of recursive levels is Θ(log n), and the worst-case search complexity is Θ(log n).

If sorting is required first, the overall preprocessing and one-search cost is:

Θ(n log n) + Θ(log n)

Therefore, the overall cost is Θ(n log n).

For q searches after a single sort, the total cost is:

Θ(n log n + q log n)

## 4.3 Hash-Table Lookup

Building a hash index involves processing every record.

Expected build time:

B(n) = Θ(n)

Under suitable hashing conditions, the expected lookup time is:

H(n) = Θ(1)

Therefore, the expected build-and-search cost for one query is:

Θ(n) + Θ(1) = Θ(n)

For q searches after one index build, the expected total cost is:

Θ(n + q)

In the worst case, severe collisions can cause a lookup to require Θ(n) work.

# 5. TASK 4 — BEST, AVERAGE, AND WORST CASES

| Algorithm               | Best Case     | Average Case  | Worst Case |
| ----------------------- | ------------- | ------------- | ---------- |
| Linear Search           | Θ(1)          | Θ(n)          | Θ(n)       |
| Recursive Binary Search | Θ(1)          | Θ(log n)      | Θ(log n)   |
| Hash-Table Lookup       | Expected Θ(1) | Expected Θ(1) | Θ(n)       |

The exact behaviour depends on the algorithm and its input conditions.

Linear search is fastest when the first record matches the target. Binary search is fastest when the middle record matches immediately. Hash-table performance depends on the distribution of keys and the collision-resolution strategy.

# 6. TASK 5 — ASYMPTOTIC ANALYSIS

Asymptotic analysis describes how an algorithm's resource requirements grow as the input size increases.

## 6.1 Big-O Notation

Big-O represents an asymptotic upper bound on growth.

## 6.2 Big-Omega Notation

Big-Omega represents an asymptotic lower bound.

## 6.3 Big-Theta Notation

Big-Theta represents a tight asymptotic bound when matching upper and lower bounds hold.

### Complexity Comparison

| Algorithm     | Search Complexity | Preprocessing          | Build and One Search |
| ------------- | ----------------- | ---------------------- | -------------------- |
| Linear Search | Θ(n) worst case   | Θ(1)                   | Θ(n)                 |
| Binary Search | Θ(log n)          | Θ(n log n) for sorting | Θ(n log n)           |
| Hash Table    | Expected Θ(1)     | Expected Θ(n)          | Expected Θ(n)        |

Increasing the dataset from 1,000 to 1,000,000 records multiplies its size by 1,000.

Linear search can require 1,000 times as many comparisons for an absent target.

Binary search requires approximately 10 comparison levels for 1,000 records and 20 for 1,000,000 records.

Expected hash-table lookup time remains approximately constant under suitable operating conditions, although the index requires additional memory.

# 7. TASK 6 — FORMULATE THE RECURRENCE

Recursive binary search reduces the problem size by approximately half at every recursive call.

The non-recursive work includes calculating the middle index, comparing values, and choosing the next interval.

This work is represented by a constant c.

The recurrence is:

T(n) = T(floor(n / 2)) + c, for n > 1

Base cases:

T(1) = c₀

T(0) = c₀

Here, c and c₀ represent constant amounts of work.

# 8. TASK 7 — SOLVE THE RECURRENCE

Assume n is a power of two for simplicity.

T(n) = T(n / 2) + c

Expanding the recurrence:

T(n) = T(n / 4) + 2c

T(n) = T(n / 8) + 3c

After k expansions:

T(n) = T(n / 2ᵏ) + kc

The recursion reaches a single element when:

n / 2ᵏ = 1

Therefore:

2ᵏ = n

k = log₂(n)

Substituting this result:

T(n) = T(1) + c log₂(n)

Hence:

T(n) = Θ(log n)

This demonstrates that recursive binary search has logarithmic worst-case time complexity.

The sorting cost must be analysed separately because binary search assumes that the records are already sorted.

# 9. TASK 8 — IMPLEMENTATION AND TESTING

The algorithms should be implemented in Python and tested using datasets of different sizes.

The implementation should include:

1. Iterative linear search.
2. Recursive binary search.
3. Hash-table construction and lookup.
4. Correctness tests for present and missing registration numbers.
5. Performance benchmarking.
6. CSV output containing measured timings.

### Correctness Tests

The implementation should test the following situations:

* Searching for the first registration number.
* Searching for a middle registration number.
* Searching for the last registration number.
* Searching for a registration number that does not exist.
* Searching an empty dataset, where supported by the implementation.

The expected result should be checked against the actual result for each test.

### Execution

After creating the Python files, run the benchmark using:

```
python benchmark.py
```

The benchmark should record the time required for preprocessing and searching separately.

**The implementation and output screenshots must be added after the Python programs have been created and tested.**

# 10. TASK 9 — EXPERIMENTAL PERFORMANCE

The experiment should compare the three algorithms using datasets containing:

* 1,000 records.
* 10,000 records.
* 100,000 records.
* 1,000,000 records.

The benchmark should use consistent datasets and test conditions.

An absent registration number can be used to measure the worst-case scan for linear search.

The following measurements should be recorded:

* Dataset size.
* Sorting time.
* Hash-index construction time.
* Median linear-search time.
* Median binary-search time.
* Median hash-lookup time.

The measurements should be stored in a CSV file for analysis.

### Experimental Results

**Insert the actual results generated by running the benchmark on the submission computer.**

Do not insert invented timings or present example values as measured results.

# 11. TASK 10 — COMPARE THEORY WITH EXPERIMENT

The theoretical analysis predicts that linear-search time increases approximately in proportion to the number of records for unsuccessful searches.

Binary search grows logarithmically when the data is sorted.

Hash-table lookup is expected to remain approximately constant under suitable hashing conditions.

Experimental measurements may differ from ideal theoretical growth because of processor speed, memory behaviour, interpreter overhead, operating-system scheduling, garbage collection, and timer resolution.

For small datasets, fixed overhead can be significant.

Preprocessing must also be included when comparing the overall cost of the approaches.

### Discussion of Results

After running the benchmark, compare the measured results with the theoretical predictions.

Explain whether the measured trends agree with the expected complexity of each algorithm and discuss any noticeable deviations.

# 12. TASK 11 — RECOMMEND AND DEFEND THE DESIGN

For the specified workload, a hash-table index is a strong candidate for the primary registration-number lookup structure.

The system receives new records once per day and performs 50,000 searches per hour. This means the cost of building an index can be amortized across many searches.

The expected total work for building the index and performing q searches is:

Θ(n + q)

This assumes expected constant-time lookup and successful index construction.

Binary search is a practical alternative when the records are maintained in sorted order. It provides deterministic logarithmic search complexity and is useful when ordered listing or range queries are required.

Linear search is not recommended for frequent searches over one million records because its worst-case time grows linearly.

The final recommendation should be supported by actual benchmark results and should consider memory requirements, collision handling, data consistency, and the system's operational requirements.

# 13. TASK 12 — DAY-4 DESIGN CHALLENGE

## 13.1 Impact Analysis

The system contains 1,000,000 student records and receives 50,000 searches per hour.

Average search rate:

50,000 / 3,600 ≈ 13.9 searches per second

If this rate continues throughout the day:

50,000 × 24 = 1,200,000 searches per day

Since new records are added only once daily, repeated lookup efficiency is a major consideration.

## 13.2 Evaluate the Original Design

For one million records:

log₂(1,000,000) ≈ 19.93

Binary search therefore requires approximately 20 comparison levels in the worst case.

Across 50,000 searches, this represents roughly one million comparison levels, assuming each search reaches approximately that depth.

For linear search, 50,000 unsuccessful searches could require:

50,000 × 1,000,000

= 50,000,000,000 comparisons

This worst-case estimate demonstrates why linear search is unsuitable for the stated workload.

Hash-table lookup is expected to perform constant-time key lookups, provided that collisions and load factor are controlled.

## 13.3 Adaptation and Redesign

The proposed design uses a hash-table index as the primary exact-match lookup structure.

At the end of each daily update batch, the system builds or refreshes the index.

Search requests then use the index to locate student records.

If the application also requires ordered listings or range queries, a sorted representation or database index can be maintained as a secondary structure.

For q searches per day, the expected total work is:

Θ(n + q)

This assumes expected linear-time index construction and expected constant-time lookup.

## 13.4 Evidence-Based Defence

The hash-table approach is appropriate because the system performs many searches between daily updates.

Building an index once and reusing it can be more efficient than repeatedly scanning the entire dataset.

Binary search remains a strong alternative when sorted data is already available.

The final choice should be supported by measured preprocessing and search times, memory usage, and the system's consistency requirements.

# 14. CONCLUSION

This project compares iterative linear search, recursive binary search, and hash-table lookup for student record retrieval.

Linear search is simple and requires no preprocessing, but its running time grows linearly with the dataset size.

Binary search offers logarithmic search time when the records are sorted, although the sorting cost must be considered if the sorted representation is not already maintained.

Hash-table lookup provides expected constant-time exact-match searches under suitable hashing conditions. Its index can be built once after the daily update batch and reused across a large number of searches.

For the stated workload of one million records and 50,000 searches per hour, a hash-table index is the recommended primary lookup strategy, subject to memory availability, collision handling, consistency requirements, and validation against measured performance.

The experiment should be completed on the submission computer so that the final report contains genuine benchmark results.

# REFERENCES

1. Cormen, T. H., Leiserson, C. E., Rivest, R. L., and Stein, C. *Introduction to Algorithms*. MIT Press.
2. Python Software Foundation. *Python 3 Documentation*.
3. Course materials for Design and Analysis of Algorithms.
4. The actual Python implementation, test results, and benchmark measurements produced for this assignment.
