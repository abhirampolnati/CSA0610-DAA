# Design and Analysis of Algorithms (DAA)

## Assignment 2 – CO2: Brute-Force and Exhaustive-Search Techniques

**Department:** Computer Science and Engineering
**Course:** Design and Analysis of Algorithms
**Assignment:** Assignment 2 – CO2
**Assignment Type:** Individual
**Total Marks:** 50
**Duration:** 1 Week

---

## 1. Project Overview

This project investigates the design, implementation, and experimental analysis of algorithms covered under CO2 of the Design and Analysis of Algorithms course.

The assignment focuses on understanding how brute-force and exhaustive-search techniques behave under different input conditions. Rather than implementing algorithms alone, this project examines their computational behavior through carefully designed experiments, mathematical analysis, operation counting, and performance comparisons.

The primary objective is to understand the relationship between input characteristics, algorithmic design, computational effort, and scalability.

The algorithms are evaluated using measurable evidence such as comparisons, swaps, movements, character comparisons, distance calculations, and candidate solutions examined. Execution time is considered supplementary evidence rather than the sole measure of performance.

## 2. Objectives

The main objectives of this project are:

* Implement the sorting algorithms Selection Sort, Bubble Sort, and Insertion Sort.
* Investigate the behavior of sorting algorithms under different input arrangements.
* Analyze Sequential Search using successful and unsuccessful searches across different dataset sizes.
* Implement Brute-Force String Matching and measure character comparisons.
* Develop a Brute-Force Closest-Pair solution and investigate its computational growth.
* Design and implement a Brute-Force Convex Hull algorithm using geometric principles.
* Implement an Exhaustive-Search solution for a constrained package-selection problem.
* Analyze theoretical time complexity and compare it with experimental observations.
* Identify computational bottlenecks and develop a redesigned strategy.
* Validate algorithmic improvements using comparable experimental conditions.
* Draw evidence-based conclusions about algorithm selection and scalability.

## 3. Assignment Coverage

This assignment contains seven questions.

| Question  | Algorithm / Technique                       | Application Scenario                               |  Marks |
| --------- | ------------------------------------------- | -------------------------------------------------- | -----: |
| Q1        | Selection Sort, Bubble Sort, Insertion Sort | E-Commerce Order Processing                        |      6 |
| Q2        | Sequential Search                           | Aircraft Maintenance Tool Tracking                 |      4 |
| Q3        | Brute-Force String Matching                 | Cybersecurity Log Screening                        |      6 |
| Q4        | Brute-Force Closest Pair                    | Drone Collision-Risk Monitoring                    |      6 |
| Q5        | Brute-Force Convex Hull                     | Wildlife Reserve Boundary Monitoring               |      7 |
| Q6        | Exhaustive Search                           | Humanitarian Airlift Planning                      |      8 |
| Q7        | Diagnose, Redesign, and Validate            | Optimization of a Computationally Limited Solution |     13 |
| **Total** |                                             |                                                    | **50** |

## 4. Problem Statements and Investigation

### Q1. Sorting Under Different Data Conditions

**Application:** E-Commerce Order Processing

Selection Sort, Bubble Sort, and Insertion Sort are implemented and evaluated using deliberately designed datasets.

The investigation considers:

* Randomly ordered data.
* Nearly sorted data.
* Already sorted or significantly disordered data.
* An additional edge-case dataset.

The algorithms are compared using operation counts and, where useful, execution time. The final objective is to recommend an appropriate sorting algorithm for a fulfilment centre where approximately 95% of existing orders are already correctly ordered.

### Q2. Sequential Search

**Application:** Aircraft Maintenance Tool Tracking

Sequential Search is evaluated for locating tools in a changing list of issued equipment.

The experiments investigate:

* Successful searches at different positions.
* Unsuccessful searches.
* Different dataset sizes.
* The relationship between list size and search frequency.

The results are used to establish the conditions under which Sequential Search remains a reasonable engineering choice and when an alternative strategy becomes necessary.

### Q3. Brute-Force String Matching

**Application:** Cybersecurity Log Screening

A Brute-Force String Matching algorithm is developed to search for character patterns within text-based system logs.

Three test conditions are designed to investigate how text and pattern characteristics influence computational effort.

The number of character comparisons is recorded, and the observed results are compared with predictions to explain why inputs of similar sizes can require different amounts of work.

### Q4. Brute-Force Closest Pair

**Application:** Drone Collision-Risk Monitoring

A Brute-Force Closest-Pair algorithm identifies the two closest points in a collection of two-dimensional coordinates.

The investigation includes:

* Mathematical derivation of the number of unique candidate pairs.
* Avoidance of duplicate pair comparisons.
* Implementation of Euclidean distance calculations.
* Experiments using multiple input sizes.
* Comparison of theoretical and experimental growth.
* Identification of the limitations of examining every possible pair.

### Q5. Brute-Force Convex Hull

**Application:** Wildlife Reserve Boundary Monitoring

A Brute-Force Convex Hull solution is developed using the geometric principle that a candidate boundary line must have all remaining points on an appropriate single side.

The investigation covers:

* Derivation of a geometric decision rule.
* Pseudocode development.
* Implementation and testing with different point configurations.
* Visualization of the resulting boundary.
* Analysis of computational growth.
* A geometric explanation of why accepted edges belong to the outer boundary.

### Q6. Exhaustive Search

**Application:** Humanitarian Airlift Planning

An Exhaustive-Search algorithm selects a combination of packages that maximizes total humanitarian value without exceeding a helicopter's payload capacity.

The implementation investigates:

* Representation of package combinations.
* Generation of candidate solutions.
* Feasibility checking.
* Evaluation of feasible solutions.
* Identification of the optimal combination.
* Mathematical analysis of the solution-space growth.
* Experimental validation using multiple problem sizes.

The results are used to estimate the largest problem size that could reasonably be handled within a defined response-time limit.

### Q7. Diagnose, Redesign, and Validate

The final challenge selects one solution from Q1–Q6 that exhibits a significant computational limitation.

The investigation includes:

1. Diagnosing the computational bottleneck.
2. Defining a measurable redesign objective.
3. Developing a revised computational strategy.
4. Predicting the expected improvement before testing.
5. Implementing and validating the redesigned solution.
6. Comparing the original and redesigned implementations.
7. Evaluating improvements, trade-offs, and remaining limitations.

The redesign is justified through algorithmic reasoning and experimental evidence rather than relying solely on the name of a known algorithm.

## 5. Methodology

The following methodology is used throughout the assignment.

**Step 1: Problem Understanding**

Understand the application scenario, identify the input and output, and define the computational problem.

**Step 2: Algorithm Design**

Develop the algorithmic approach and write pseudocode where required.

**Step 3: Theoretical Analysis**

Determine the relevant time complexity, mathematical growth, and expected computational behavior.

**Step 4: Experimental Design**

Construct test datasets that expose meaningful differences in algorithm behavior.

**Step 5: Implementation**

Implement the algorithms using Python and validate their basic correctness.

**Step 6: Operation Counting**

Record algorithm-specific measures such as comparisons, swaps, movements, character comparisons, distance calculations, and candidate solutions examined.

**Step 7: Experimental Validation**

Execute the implementations using controlled test conditions and collect actual results.

**Step 8: Comparative Analysis**

Compare theoretical predictions with experimental observations using tables and graphs where appropriate.

**Step 9: Engineering Decision**

Identify practical limitations and justify recommendations using the collected evidence.

**Step 10: Redesign and Evaluation**

For Q7, develop and test an improved strategy against the original solution using comparable conditions.

## 6. Technologies Used

| Technology            | Purpose                                          |
| --------------------- | ------------------------------------------------ |
| Python 3              | Algorithm implementation and experimentation     |
| Visual Studio Code    | Code development and execution                   |
| Git and GitHub        | Version control and project submission           |
| CSV                   | Storage of raw experimental results              |
| Matplotlib            | Graph generation and visualization               |
| Mathematical Analysis | Complexity derivation and theoretical prediction |

The use of each tool depends on the requirements of the individual question.

## 7. Repository Structure

```text
DAA-Assignment-2-CO2/
│
├── README.md
│
├── src/
│   ├── sorting_algorithms.py
│   ├── sequential_search.py
│   ├── brute_force_string_matching.py
│   ├── closest_pair.py
│   ├── convex_hull.py
│   ├── exhaustive_search.py
│   └── redesigned_solution.py
│
├── experiments/
│   ├── benchmark.py
│   └── benchmark_results.csv
│
├── results/
│   ├── sorting_comparison.png
│   ├── string_matching_comparison.png
│   ├── closest_pair_growth.png
│   ├── convex_hull_visualization.png
│   └── exhaustive_search_growth.png
│
└── report/
    └── DAA_Assignment_2_CO2.pdf
```

**Note:** The structure represents the planned organization of the project. Files, experimental results, and graphs will be added as the corresponding implementations and experiments are completed.

## 8. Experimental Evaluation

The algorithms are evaluated using measures appropriate to their operations.

| Algorithm                   | Primary Experimental Measures                   |
| --------------------------- | ----------------------------------------------- |
| Selection Sort              | Comparisons and swaps                           |
| Bubble Sort                 | Comparisons, swaps, and movements               |
| Insertion Sort              | Comparisons and movements                       |
| Sequential Search           | Number of element comparisons                   |
| Brute-Force String Matching | Number of character comparisons                 |
| Brute-Force Closest Pair    | Unique pairs examined and distance calculations |
| Brute-Force Convex Hull     | Geometric tests and computational operations    |
| Exhaustive Search           | Candidate combinations generated and evaluated  |
| Redesigned Solution         | Comparable operation counts and execution time  |

Execution time may also be recorded to provide additional information about practical performance.

Operation counts are treated as primary evidence because they help explain how computational work grows independently of some hardware and system-specific timing variations.

## 9. Complexity Analysis

The project investigates how computational effort changes as the input size increases.

The analysis considers the following general growth categories wherever applicable:

* **Constant time:** O(1)
* **Logarithmic time:** O(log n)
* **Linear time:** O(n)
* **Linearithmic time:** O(n log n)
* **Quadratic time:** O(n²)
* **Exponential time:** O(2ⁿ)

The actual complexity of each implementation will be derived from its algorithmic operations and the relevant assumptions. Experimental results will be used to examine whether the observed behavior agrees with the theoretical prediction.

## 10. Expected Outcomes

Upon completion of the assignment, the project is expected to demonstrate:

* A working implementation of each required algorithm.
* A clear understanding of brute-force and exhaustive-search techniques.
* Correctness checks using deliberately designed test cases.
* Mathematical derivations supporting operation counts and complexity analysis.
* Experimental datasets documenting actual algorithmic behavior.
* Tables and visualizations comparing computational performance.
* Evidence-based recommendations for practical algorithm selection.
* A redesigned solution supported by comparative testing.
* A clear understanding of the trade-offs between simplicity, computational cost, and scalability.

## 11. Conclusion

This assignment provides an experimental study of brute-force and exhaustive-search algorithms through realistic engineering scenarios.

By combining algorithm implementation, mathematical analysis, carefully designed experiments, and evidence-based evaluation, the project examines both the strengths and limitations of straightforward computational strategies.

The final redesign challenge extends this investigation by requiring a computational bottleneck to be diagnosed and addressed through a justified alternative strategy.

The overall goal is to develop the ability to design algorithms, measure their behavior, analyze their scalability, and make technically defensible engineering decisions.

---

**Course:** Design and Analysis of Algorithms
**Assignment:** Assignment 2 – CO2
**Department:** Computer Science and Engineering
