# SentinelOps: DAA CO2 Debugging and Optimisation

**Course Code:** CSA06
**Course Name:** Design and Analysis of Algorithms
**Assessment:** CO2 – Debugging and Optimisation Task
**Problem Domain:** Security Operations Centre (SOC) Alert-Triage Module
**Programming Language:** Python 3
**Assessment Type:** Individual
**Maximum Marks:** 50

---

## 1. Project Overview

SentinelOps is a simulated Security Operations Centre (SOC) module designed to process security alerts, identify blocked IP addresses, detect attack signatures in log messages, and identify login attempts occurring at the closest geographical locations.

The original module developed by a junior programmer contained several logical errors that caused incorrect sorting, failed blocklist detection, inaccurate signature matching, and incorrect closest-pair calculations.

This project investigates those defects, explains their root causes, corrects the algorithms, and optimises the implementations for larger workloads.

The module is designed around the following workloads:

* Approximately 50,000 incoming security alerts.
* Repeated IP address lookups against a blocklist.
* Brute-force string matching for detecting attack signatures.
* Batches containing up to 8,000 login events.

The primary objective is to demonstrate systematic debugging, algorithmic reasoning, correctness testing, performance measurement, and optimisation while preserving the intended behaviour of the corrected algorithms.

---

## 2. Problem Statement

The original SentinelOps module exhibited four major categories of failures.

1. **Incorrect alert sorting:** Alerts were not consistently sorted by severity, and boundary errors could cause incorrect insertion.
2. **Failed IP blocklist detection:** The search function returned incorrect results for both blocked and unblocked addresses.
3. **Incorrect signature matching:** Some valid matches were missed, while the implementation could report incorrect matches.
4. **Incorrect closest-pair detection:** The algorithm selected the wrong distance objective, examined unnecessary pairs, and did not correctly handle inputs containing fewer than two events.

These defects could affect security monitoring by allowing blocked sources to pass through, hiding attack signatures, and generating misleading reports about clustered login attempts.

The project applies brute-force algorithms as a baseline and evaluates suitable optimisation techniques for production-oriented processing.

---

## 3. Objectives

The objectives of this assessment are:

* Identify and reproduce the defects in the original Python module.
* Explain the root cause and impact of every identified defect.
* Correct the algorithms without rewriting the original implementation unnecessarily.
* Verify every correction using appropriate test cases.
* Preserve alert arrival order when severities are equal.
* Improve repeated IP address lookups.
* Eliminate redundant work in string matching and closest-pair calculations.
* Analyse theoretical time and space complexity.
* Measure algorithm performance using reproducible experiments.
* Compare theoretical predictions with observed benchmark results.
* Develop clean, documented, and testable Python implementations.

---

## 4. Algorithms Implemented

The project covers four algorithmic problems.

| No. | Function           | Algorithm                                     | Purpose                                      |
| --- | ------------------ | --------------------------------------------- | -------------------------------------------- |
| 1   | `sort_alerts()`    | Insertion Sort / Stable Sorting               | Sort alerts by descending severity           |
| 2   | `is_blocked()`     | Sequential Search / Hash-Based Lookup         | Check whether an IP address is blocked       |
| 3   | `find_signature()` | Brute-Force String Matching                   | Find every occurrence of an attack signature |
| 4   | `closest_logins()` | Brute-Force Closest Pair / Divide and Conquer | Identify the two closest login locations     |

The corrected brute-force implementations provide a baseline against which the optimised implementations can be evaluated.

---

## 5. Debugging and Correction

### 5.1 Alert Sorting

**Algorithm:** Insertion Sort

**Requirement:** Sort alerts from highest to lowest severity while preserving the original arrival order of alerts having equal severity.

Example input:

```python
[
    ("A1", 3),
    ("A2", 9),
    ("A3", 5),
    ("A4", 9),
    ("A5", 1)
]
```

Expected output:

```python
[
    ("A2", 9),
    ("A4", 9),
    ("A3", 5),
    ("A1", 3),
    ("A5", 1)
]
```

The implementation must correctly handle the first element, insert each key at the appropriate position, and preserve the relative order of equal-severity alerts.

**Optimisation:** Evaluate insertion sort for nearly sorted input and compare it with Python's built-in stable sorting algorithm.

### 5.2 IP Blocklist Lookup

**Algorithm:** Sequential Search

The corrected sequential search must return:

* `True` when the IP address exists in the blocklist.
* `False` when the IP address does not exist in the blocklist.
* `False` when the blocklist is empty.

For repeated lookups, the project evaluates converting the blocklist into a Python set.

A set provides expected constant-time membership checks, subject to normal hash-table assumptions, at the cost of additional memory and the initial set-construction operation.

### 5.3 Attack Signature Matching

**Algorithm:** Brute-Force String Matching

The function must return the starting index of every occurrence of a specified pattern in a log string.

Example:

```python
log = "FAILFAIXFAIL"
pattern = "FAIL"
```

Expected output:

```python
[0, 8]
```

The corrected implementation must handle:

* Matches at the beginning of the log.
* Matches at the final possible position.
* Multiple occurrences.
* Overlapping occurrences.
* Empty logs.
* Patterns longer than the log.
* Empty patterns according to the documented implementation policy.

The matching algorithm must stop comparing characters at a candidate position immediately after detecting a mismatch.

### 5.4 Closest Login Pair

**Algorithm:** Brute-Force Closest Pair

Each login event is represented by a two-dimensional coordinate `(x, y)`.

The objective is to identify the two distinct events having the minimum Euclidean distance.

The distance between two points is:

$$
d=\sqrt{(x_1-x_2)^2+(y_1-y_2)^2}
$$

The brute-force baseline examines every unordered pair exactly once.

The optimised implementation evaluates squared distances where possible and uses a suitable divide-and-conquer closest-pair algorithm to reduce the number of candidate comparisons.

The implementation must also handle zero events and one event without attempting invalid pair calculations.

---

## 6. Repository Structure

The planned repository structure is:

```text
DAA-CO2-Debugging-Optimisation/
│
├── README.md
│
├── src/
│   ├── sentinelops_original.py
│   ├── sentinelops_debugged.py
│   └── sentinelops_optimized.py
│
├── tests/
│   └── test_sentinelops.py
│
├── benchmarks/
│   ├── benchmark_closest_pair.py
│   ├── benchmark_sorting.py
│   ├── closest_pair_results.csv
│   └── sorting_results.csv
│
├── results/
│   ├── closest_pair_comparison.png
│   └── sorting_comparison.png
│
├── docs/
│   └── DAA_CO2_Report.docx
│
└── requirements.txt
```

**Note:** Files will be added to these directories as implementation, testing, benchmarking, and report preparation progress.

---

## 7. Optimisation Techniques

### 7.1 Sorting Optimisation

Insertion sort has the following time complexities:

* Best case: \(O(n)\)
* Average case: \(O(n^2)\)
* Worst case: \(O(n^2)\)

Insertion sort can perform well when input data is already sorted or nearly sorted.

Python's built-in sorting algorithm, Timsort, has \(O(n\log n)\) worst-case time complexity and can exploit existing order in the data.

Both approaches will be evaluated using nearly sorted and randomly ordered alerts. The selected production approach must preserve descending severity order and stability.

### 7.2 Blocklist Optimisation

For a blocklist containing \(b\) IP addresses and \(q\) lookup requests:

Sequential search has worst-case total time complexity:

$$
O(qb)
$$

Building a set and performing repeated membership checks has expected total time complexity:

$$
O(b+q)
$$

This optimisation is particularly useful when many queries are performed against the same blocklist.

### 7.3 String Matching Optimisation

For a log of length \(n\) and a pattern of length \(m\), brute-force string matching has worst-case time complexity:

$$
O(nm)
$$

The corrected implementation limits candidate starting positions to valid alignments and stops character comparisons immediately after a mismatch.

### 7.4 Closest-Pair Optimisation

The number of unordered pairs of \(n\) events is:

$$
\frac{n(n-1)}{2}
$$

For 8,000 login events:

$$
\frac{8000(7999)}{2}=31,996,000
$$

Therefore, brute-force closest-pair search requires examining 31,996,000 candidate pairs in the general case.

The divide-and-conquer closest-pair algorithm has theoretical time complexity:

$$
O(n\log n)
$$

Squared distances can be compared instead of calculating square roots for every candidate pair. A square root is required only when the final distance is returned.

---

## 8. Complexity Analysis

The following table describes the expected theoretical complexities of the corrected baseline and optimised implementations.

| Function           | Corrected Baseline                    | Optimised Approach                                         |
| ------------------ | ------------------------------------- | ---------------------------------------------------------- |
| Alert sorting      | Insertion Sort: \(O(n^2)\) worst case | Timsort: \(O(n\log n)\) worst case                         |
| Blocklist lookup   | Sequential Search: \(O(b)\) per query | Set lookup: \(O(1)\) expected per query after construction |
| Signature matching | Brute Force: \(O(nm)\) worst case     | Corrected brute force: \(O(nm)\) worst case                |
| Closest login pair | Brute Force: \(O(n^2)\)               | Divide and Conquer: \(O(n\log n)\)                         |

Here:

* \(n\) represents the number of alerts, log characters, or login events, depending on the function.
* \(m\) represents the attack signature length.
* \(b\) represents the number of IP addresses in the blocklist.
* \(q\) represents the number of IP lookup requests.

The final report will include detailed operation-count derivations, space complexity, and experimental evidence.

---

## 9. Testing Strategy

The test harness will validate the corrected and optimised implementations.

### Alert Sorting Tests

* Alerts in random order.
* Alerts already sorted by severity.
* Reverse-sorted alerts.
* Equal-severity alerts.
* Empty alert list.
* Single alert.
* Verification that no alerts are lost or duplicated.

### Blocklist Tests

* IP address present in the blocklist.
* IP address absent from the blocklist.
* Empty blocklist.
* Single-entry blocklist.
* Repeated queries against the same blocklist.

### Signature Matching Tests

* Pattern at the beginning of a log.
* Pattern at the end of a log.
* Multiple matches.
* Overlapping matches.
* Pattern longer than the log.
* Empty log.
* Empty pattern.

### Closest-Pair Tests

* Zero events.
* One event.
* Two events.
* Several events with different distances.
* Duplicate coordinates.
* Multiple pairs with equal minimum distances.
* Comparison between brute-force and optimised results.

The test harness will verify correctness rather than relying solely on execution time or example outputs.

---

## 10. Experimental Performance Evaluation

Benchmarking will compare the algorithms using different input sizes and data distributions.

### Experiment A: Sorting Performance

Input sizes and ordering conditions will be varied to measure:

* Number of element comparisons.
* Number of shifts, where applicable.
* Execution time.
* Differences between nearly sorted and random inputs.

### Experiment B: Closest-Pair Performance

The following batch sizes will be evaluated:

| Experiment | Number of Events |
| ---------- | ---------------: |
| 1          |            1,000 |
| 2          |            2,000 |
| 3          |            4,000 |
| 4          |            8,000 |

The benchmark will measure distance evaluations and execution time for the brute-force and divide-and-conquer implementations.

### Results

**Experimental results are pending implementation and execution.** The final repository will include the measured CSV data and generated graphs.

Results will be interpreted alongside the theoretical complexity analysis. Execution time may vary with hardware, Python version, input distribution, and implementation details.

---

## 11. Running the Project

### Prerequisites

* Python 3.10 or later.
* Git.
* A code editor such as Visual Studio Code.

### Step 1: Clone the Repository

Replace `<your-username>` with your GitHub username.

```bash
git clone https://github.com/<your-username>/DAA-CO2-Debugging-Optimisation.git
```

### Step 2: Open the Project

```bash
cd DAA-CO2-Debugging-Optimisation
```

### Step 3: Run the Optimised Module

After the implementation is added:

```bash
python src/sentinelops_optimized.py
```

### Step 4: Run the Test Harness

```bash
python -m unittest discover -s tests -v
```

### Step 5: Run the Benchmarks

```bash
python benchmarks/benchmark_sorting.py
```

```bash
python benchmarks/benchmark_closest_pair.py
```

The benchmark scripts will be configured to save their measurements as CSV files.

**Note:** These commands assume that the files have been created using the documented structure.

---

## 12. Tools and Technologies

| Tool / Technology  | Purpose                       |
| ------------------ | ----------------------------- |
| Python 3           | Algorithm implementation      |
| Visual Studio Code | Development and debugging     |
| Git                | Version control               |
| GitHub             | Source-code hosting           |
| Python `unittest`  | Automated correctness testing |
| CSV                | Experimental result storage   |
| Matplotlib         | Benchmark visualisation       |
| Word document      | Detailed assessment report    |

---

## 13. Expected Outcomes

The project aims to demonstrate the following outcomes:

* Correct sorting of security alerts by descending severity.
* Stable ordering of alerts having equal severity.
* Reliable blocklist membership checks.
* Correct identification of all attack-signature occurrences.
* Accurate closest-pair calculations.
* Improved performance for repeated blocklist lookups.
* Reduced closest-pair computation time for larger batches.
* Measurable comparison between nearly sorted and random alert data.
* Reproducible benchmark results.
* Documented reasoning for every identified defect and correction.

These are the intended outcomes; correctness and performance will be verified through the implementation, automated tests, and experiments.

---

## 14. Conclusion

The SentinelOps debugging and optimisation project demonstrates the importance of algorithmic correctness in security-related applications.

Even small implementation mistakes can cause significant problems, including incorrect alert prioritisation, failed IP detection, missed attack signatures, and misleading login-clustering results.

Systematic debugging helps identify the underlying causes of these failures, while algorithmic optimisation improves scalability for larger workloads.

By combining corrected implementations, automated tests, theoretical analysis, and experimental benchmarking, this project provides a structured evaluation of brute-force techniques and more efficient alternatives.

---

## 15. Academic Information

**Course:** Design and Analysis of Algorithms
**Course Code:** CSA06
**Assessment:** CO2 – Debugging and Optimisation Task
**Student Name:** __________________________
**Registration Number:** ____________________
**Department:** Computer Science and Engineering
**Institution:** Saveetha Engineering College / SIMATS
**Academic Year:** 2026–2027

---

**Repository Status:** Implementation and experimental validation in progress.

**Final Submission:** Source code, automated tests, benchmark results, graphs, and the detailed Word report will be included after completion and verification.
