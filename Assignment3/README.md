# DESIGN AND ANALYSIS OF ALGORITHMS

## Assignment 3 – CO3

**Course:** Design and Analysis of Algorithms (DAA)
**Course Outcome:** CO3
**Assessment:** Assignment 3
**Mode:** Pair Work – 2 Students per Group
**Duration:** 1 Week
**Total Marks:** 50

---

## 1. Project Overview

This project investigates advanced algorithm design techniques, with particular emphasis on Divide and Conquer, efficient searching and sorting, recursive problem decomposition, and optimization of computational complexity.

The assignment combines theoretical analysis, algorithm implementation, experimental benchmarking, and comparative evaluation to understand how different algorithmic strategies perform under different input conditions.

Both students participate in every question and share responsibility for understanding the complete assignment. Individual responsibilities alternate between algorithm design, mathematical analysis, implementation, experimental investigation, and verification.

## 2. Objectives

* Understand the principles of Divide and Conquer and problem decomposition.
* Implement efficient searching and sorting algorithms.
* Analyse algorithm performance using time and space complexity.
* Derive and interpret recurrence relations.
* Compare theoretical complexity with experimentally observed performance.
* Investigate the effects of input size, pivot selection, recursion depth, and computational overhead.
* Evaluate trade-offs between execution time, memory usage, and algorithmic efficiency.
* Develop the ability to explain, test, and defend algorithm design decisions.

## 3. Assignment Questions

### Q1 – Decomposition and Elimination in Ordered Data

**Part A: Finding Maximum and Minimum**

Implement a Divide-and-Conquer or tournament-based approach to find both the maximum and minimum elements in an array.

Tasks:

* Decompose the input into smaller subproblems.
* Define the base case and combine operation.
* Count element comparisons.
* Derive the expected number of comparisons.
* Compare the results with independently finding the maximum and minimum.
* Validate theoretical predictions using experimental datasets.

**Part B: Binary Search**

Implement Binary Search on sorted data.

Tasks:

* Investigate successful and unsuccessful searches.
* Record comparison counts for different input sizes.
* Explain the decision rule and elimination of the search space.
* Analyse the termination condition and computational efficiency.

**Expected complexity:**

* Divide-and-Conquer Maximum/Minimum: O(n) time.
* Binary Search: O(log n) time.

### Q2 – The Quality of Decomposition in Sorting

Implement and compare Merge Sort and Quick Sort.

Tasks:

* Select and document a Quick Sort pivot strategy.
* Investigate balanced and severely unbalanced partitions.
* Record partition sizes and maximum recursion depth.
* Analyse Merge Sort's predictable decomposition.
* Compare recursion-tree heights and sorting performance.
* Investigate conditions that can lead to quadratic Quick Sort behaviour.

**Expected complexity:**

| Algorithm  | Best Case  | Average Case | Worst Case |
| ---------- | ---------- | ------------ | ---------- |
| Merge Sort | O(n log n) | O(n log n)   | O(n log n) |
| Quick Sort | O(n log n) | O(n log n)   | O(n²)      |

The pair will also evaluate which sorting strategy is more appropriate when input characteristics are unknown.

### Q3 – Breaking the Quadratic Barrier: Karatsuba Multiplication

Implement conventional integer multiplication and Karatsuba multiplication.

Tasks:

* Decompose large integers into smaller parts.
* Implement the standard multiplication method.
* Reduce recursive multiplications using Karatsuba's technique.
* Formulate and solve the recurrence relation.
* Record multiplication counts and execution times.
* Determine the approximate practical crossover range.
* Investigate recursion overhead for small inputs.

**Expected complexity:**

* Conventional digit-by-digit multiplication: O(n²).
* Karatsuba multiplication: O(n^log₂3), approximately O(n^1.585).

The experiment will examine why Karatsuba's theoretical advantage may not translate into better performance for every input size.

### Q4 – The Reality of Strassen's Matrix Multiplication

Implement conventional matrix multiplication and Strassen's matrix multiplication.

Tasks:

* Explain conventional block-matrix decomposition.
* Identify the eight block multiplications in conventional recursive multiplication.
* Implement Strassen's seven-multiplication transformation.
* Verify the correctness of both implementations.
* Handle non-power-of-two matrix dimensions through padding or an appropriate alternative.
* Record multiplication counts and execution times.
* Analyse addition, subtraction, recursion, memory, and padding overhead.
* Determine the approximate practical crossover range.

**Expected complexity:**

| Algorithm                          | Time Complexity                      |
| ---------------------------------- | ------------------------------------ |
| Conventional matrix multiplication | O(n³)                                |
| Strassen's matrix multiplication   | O(n^log₂7), approximately O(n^2.807) |

The pair will identify conditions under which conventional matrix multiplication remains preferable despite Strassen's superior asymptotic complexity.

### Q5 – Upgrading Closest Pair Using Divide and Conquer

Compare the Brute-Force Closest-Pair algorithm with a Divide-and-Conquer solution.

Tasks:

* Organise the input points appropriately.
* Divide the point set into smaller subproblems.
* Find the closest pair in each subproblem.
* Combine the results using a dividing-boundary strip.
* Explain why the boundary region requires special treatment.
* Count distance calculations and measure execution times.
* Compare both algorithms on equivalent datasets.
* Investigate the input sizes at which Divide and Conquer becomes practically advantageous.

**Expected complexity:**

| Approach           | Time Complexity |
| ------------------ | --------------- |
| Brute Force        | O(n²)           |
| Divide and Conquer | O(n log n)      |

The implementation must handle duplicate points, small input sets, and other relevant edge cases correctly.

### Q6 – Advanced Divide-and-Conquer Mini-Investigations

#### Part A: Median of Medians and QuickSelect

Implement Median of Medians for finding the k-th smallest element and compare it with QuickSelect.

Tasks:

* Group elements and determine the pivot using the Median of Medians strategy.
* Explain how pivot quality influences partition balance.
* Compare deterministic selection with QuickSelect.
* Investigate a deterministic poor-pivot strategy.
* Examine the effects of randomised pivot selection.
* Explain the worst-case complexity guarantee.

**Expected complexity:**

| Algorithm              | Expected/Average Time | Worst-Case Time |
| ---------------------- | --------------------- | --------------- |
| Median of Medians      | O(n)                  | O(n)            |
| Randomised QuickSelect | O(n)                  | O(n²)           |

#### Part B: Meet-in-the-Middle Subset Sum

Implement Meet-in-the-Middle for the Subset Sum problem.

Tasks:

* Divide the input set into two halves.
* Generate subset sums for both halves.
* Combine or search the partial results to find a target sum.
* Analyse the number of generated subset sums.
* Evaluate additional memory requirements.
* Compare the approach with straightforward exhaustive enumeration.
* Explain the time-memory trade-off.

**Expected complexity:**

For n elements, a typical Meet-in-the-Middle implementation uses approximately O(2^(n/2)) subset sums per half and O(n × 2^(n/2)) time when sorting the sums and performing binary searches, with O(2^(n/2)) auxiliary space.

Straightforward exhaustive enumeration takes O(2^n) time in the general case.

Exact complexity depends on the implementation and the operations used to combine the partial results.

## 4. Algorithms and Techniques Used

The project covers the following algorithms and techniques:

1. Divide-and-Conquer Maximum and Minimum.
2. Binary Search.
3. Merge Sort.
4. Quick Sort.
5. Conventional Integer Multiplication.
6. Karatsuba Multiplication.
7. Conventional Matrix Multiplication.
8. Strassen's Matrix Multiplication.
9. Brute-Force Closest Pair.
10. Divide-and-Conquer Closest Pair.
11. Median of Medians.
12. QuickSelect.
13. Meet-in-the-Middle Subset Sum.

## 5. Project Structure

The repository will be organised as follows. File and folder names can be adjusted to match the final implementation.

```text
DAA-Assignment-3-CO3/
│
├── README.md
│
├── Q1_Max_Min_Binary_Search/
│   ├── max_min.py
│   ├── binary_search.py
│   └── benchmark.py
│
├── Q2_Merge_Quick_Sort/
│   ├── merge_sort.py
│   ├── quick_sort.py
│   └── benchmark.py
│
├── Q3_Karatsuba_Multiplication/
│   ├── standard_multiplication.py
│   ├── karatsuba.py
│   └── benchmark.py
│
├── Q4_Strassen_Matrix_Multiplication/
│   ├── conventional_matrix.py
│   ├── strassen.py
│   └── benchmark.py
│
├── Q5_Closest_Pair/
│   ├── brute_force.py
│   ├── divide_conquer.py
│   └── benchmark.py
│
├── Q6_Advanced_Algorithms/
│   ├── median_of_medians.py
│   ├── quickselect.py
│   ├── subset_sum_mitm.py
│   └── benchmark.py
│
├── tests/
│   ├── test_q1.py
│   ├── test_q2.py
│   ├── test_q3.py
│   ├── test_q4.py
│   ├── test_q5.py
│   └── test_q6.py
│
├── results/
│   ├── csv/
│   └── graphs/
│
└── report/
    └── DAA_Assignment_3_CO3_Report.docx
```

*Note: This is the planned structure. The final repository should contain only files that have actually been created and tested.*

## 6. Experimental Methodology

Experiments will be conducted using multiple input sizes and appropriate input distributions.

The methodology includes:

* Testing small, medium, and large datasets.
* Using equivalent inputs when comparing algorithms.
* Repeating timing measurements to reduce the influence of transient system activity.
* Recording comparison counts, multiplication counts, recursion depth, or distance calculations where applicable.
* Separating correctness testing from performance benchmarking.
* Recording experimental observations in CSV files.
* Generating graphs to compare the performance of different algorithms.
* Comparing observed results against theoretical complexity predictions.

### Important Performance Metrics

| Metric                | Purpose                                       |
| --------------------- | --------------------------------------------- |
| Execution Time        | Measures observed runtime                     |
| Comparison Count      | Evaluates comparison-based computational work |
| Multiplication Count  | Evaluates multiplication reduction            |
| Recursion Depth       | Investigates recursive decomposition          |
| Distance Calculations | Measures closest-pair computational work      |
| Memory Usage          | Evaluates storage requirements                |
| Input Size            | Helps analyse scalability                     |

Execution times may vary with processor performance, programming language, implementation details, system load, and memory behaviour. Experimental results will therefore be interpreted alongside theoretical analysis.

## 7. Testing and Correctness

Each algorithm will be tested using appropriate cases, including:

* Empty input where supported.
* Single-element input.
* Two-element input.
* Already sorted data.
* Reverse-sorted data.
* Randomly generated data.
* Duplicate elements.
* Negative values where applicable.
* Boundary values.
* Valid and invalid search targets.
* Different matrix dimensions and valid multiplication combinations.
* Duplicate or coincident points in closest-pair problems.
* Different k values in selection algorithms.
* Subset Sum instances with and without a valid solution.

The implementations will be checked against simple reference solutions or independently verified expected results wherever possible.

## 8. Theoretical and Experimental Analysis

The final analysis will compare theoretical complexity with observed performance.

The report will address:

* Whether the measured trends agree with theoretical predictions.
* How input size affects execution time.
* How input arrangement affects Quick Sort.
* When Karatsuba and Strassen become practically advantageous.
* How recursion and memory overhead affect performance.
* How Divide and Conquer reduces the computational work of the Closest-Pair problem.
* How Median of Medians guarantees worst-case linear selection time.
* How Meet-in-the-Middle reduces exponential search at the expense of additional storage.

Actual benchmark values, crossover ranges, and conclusions will be added after running the implementations.

## 9. Student Responsibilities

Both students are responsible for understanding every question and participating in the complete assignment.

### Student A

Primary responsibilities include:

* Maximum/Minimum decomposition design and mathematical analysis.
* Binary Search experimental investigation.
* Quick Sort partition investigation.
* Karatsuba algorithm derivation.
* Strassen experimental and engineering analysis.
* Closest-Pair decomposition design.
* Median of Medians investigation.
* Verification of Meet-in-the-Middle reasoning.

### Student B

Primary responsibilities include:

* Maximum/Minimum experimental validation.
* Binary Search elimination logic.
* Merge Sort and comparative Divide-and-Conquer analysis.
* Karatsuba crossover investigation.
* Strassen algebraic design and correctness.
* Closest-Pair comparative experimental evidence.
* Meet-in-the-Middle investigation.
* Verification of selection-algorithm reasoning.

**Note:** These responsibilities identify primary contributions and do not exclude either student from implementation, testing, or explaining any question during faculty evaluation.

## 10. Expected Learning Outcomes

By completing this assignment, the students should be able to:

* Design algorithms using Divide-and-Conquer principles.
* Formulate and analyse recurrence relations.
* Explain best-case, average-case, and worst-case behaviour.
* Implement and test advanced algorithms.
* Evaluate algorithmic efficiency using experimental evidence.
* Understand the relationship between asymptotic complexity and practical performance.
* Explain engineering trade-offs involving time, memory, and recursion.
* Defend algorithm design choices during viva examinations.

## 11. Conclusion

This assignment provides a practical and theoretical study of algorithm design, decomposition, elimination, recursive computation, and optimisation.

By implementing and experimentally evaluating the algorithms across all six questions, the project aims to demonstrate that algorithm selection depends not only on asymptotic complexity but also on input characteristics, implementation overhead, memory requirements, and practical execution behaviour.

The combined theoretical and experimental analysis will help establish a deeper understanding of algorithm efficiency and the trade-offs involved in choosing an appropriate algorithm for a given problem.

## 12. References

1. Thomas H. Cormen, Charles E. Leiserson, Ronald L. Rivest, and Clifford Stein, *Introduction to Algorithms*, MIT Press.
2. Jon Kleinberg and Éva Tardos, *Algorithm Design*, Pearson.
3. Robert Sedgewick and Kevin Wayne, *Algorithms*, Addison-Wesley.
4. Course materials and lecture notes for Design and Analysis of Algorithms, CO3.
5. Official Python documentation, if Python is used for implementation and benchmarking.
