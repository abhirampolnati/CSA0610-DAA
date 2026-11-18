# CO4 – Automated Testing: Cloud Release Budget Planner

**Course:** CSA06 – Design and Analysis of Algorithms  
**Assessment:** CO4 – Cloud Release Budget Planner  
**Testing Language:** Python 3  
**Tested Application:** C++ Cloud Release Budget Planner

## 1. Overview

This project implements an automated testing system using Python to verify the correctness of the Cloud Release Budget Planner.

The testing script executes the compiled C++ program with predefined inputs, captures its output, and compares the actual results with the expected results.

It automatically identifies successful and unsuccessful test cases and displays a final testing summary.

## 2. Objectives

- Automate the execution of multiple test cases.
- Verify the correctness of the Greedy and Dynamic Programming results.
- Test normal inputs and important edge cases.
- Compare actual output with expected output.
- Generate a PASS/FAIL status for each test.
- Display the total number of passed and failed tests.

## 3. Test Cases

The script contains eight test cases:

| Test Case | Purpose |
|---|---|
| Sample 1 | Verify the first assessment example |
| Sample 2 | Verify the second assessment example |
| Zero Budget | Test behaviour when budget is zero |
| No Feature Fits | Verify when all feature costs exceed the budget |
| Every Feature Fits | Check selection when all features fit |
| Tied Optimal Values | Verify minimum-budget tie-breaking |
| Single Feature | Test the minimum number of features |
| Zero Value Feature | Verify handling of zero-value features |

## 4. Working Method

The testing process follows these steps:

1. Define the executable path.
2. Store the test cases in a Python list.
3. Execute the C++ program using `subprocess.run()`.
4. Pass the test input through standard input.
5. Capture standard output and standard error.
6. Compare actual output with expected output.
7. Print PASS or FAIL for each test.
8. Display the final test summary.

## 5. Modules Used

| Module / Function | Purpose |
|---|---|
| `subprocess` | Executes the C++ program |
| `subprocess.run()` | Runs the executable with supplied input |
| `capture_output=True` | Captures program output and errors |
| `strip()` | Removes surrounding whitespace |
| `splitlines()` | Converts output into individual lines |
| `print()` | Displays test results |

## 6. Execution

Compile the C++ program:

```bash
g++ -std=c++17 -O2 -Wall -Wextra cloud_release_planner.cpp -o cloud_release_planner
```

Run the Python test script:

```bash
python3 tests/run_tests.py
```

On Windows, update the executable path to:

```python
executable = ".\\cloud_release_planner.exe"
```

## 7. Expected Test Summary

When all eight tests pass, the expected summary is:

```text
Total Tests: 8
Passed: 8
Failed: 0
```

Actual execution results must be obtained by running the test script.

## 8. Complexity Analysis

Let `T` represent the number of test cases and `L` represent the average amount of input and output text handled per test.

- Test iteration: O(T)
- Output comparison: O(L) per test
- Overall test-harness processing: O(T × L), excluding the execution time of the C++ program.

## 9. Conclusion

The automated test runner simplifies the verification of the Cloud Release Budget Planner. It checks the supplied sample cases and additional edge cases without requiring manual comparison of every output.

The script improves testing consistency and helps identify errors in program execution and output formatting.
