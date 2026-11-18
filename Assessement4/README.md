# CO4 – Cloud Release Budget Planner

**Course Code:** CSA06 – Design and Analysis of Algorithms  
**Assessment:** CO4 – Assessment Tool 1: Coding Challenge  
**Programming Language:** C++  
**Problem:** Cloud Release Budget Planner

## 1. Problem Overview

A SaaS company has proposed `n` microservice features for its next monthly release. Each feature has a name, deployment cost, and estimated business value.

The company has a fixed monthly cloud budget `W`. Each feature must either be deployed completely or not deployed at all. Partial deployment and selecting the same feature multiple times are not allowed.

The objective is to select a combination of features that maximizes the total business value without exceeding the available budget.

The program implements two approaches:

- Greedy Algorithm – selects features based on decreasing value-to-cost ratio.
- Dynamic Programming – uses the 0/1 Knapsack algorithm to calculate the optimal maximum value.

## 2. Problem Objective

Maximize the total business value while satisfying the budget constraint.

Let:

- `n` = Number of available features
- `W` = Available budget
- `cost[i]` = Deployment cost of feature `i`
- `value[i]` = Business value of feature `i`
- `x[i]` = Selection variable (0 or 1)

The mathematical formulation is:

**Maximize:**

\[
\sum_{i=1}^{n} value[i] \times x[i]
\]

**Subject to:**

\[
\sum_{i=1}^{n} cost[i] \times x[i] \leq W
\]

Where:

\[
x[i] \in \{0,1\}
\]

This is the **0/1 Knapsack Problem**.

## 3. Input Format

The first line contains two integers:

`n W`

The next `n` lines contain:

`feature_name cost value`

Feature names are single words.

### Constraints

| Parameter | Constraint |
|---|---|
| Number of features | 1 ≤ n ≤ 200 |
| Available budget | 0 ≤ W ≤ 10,000 |
| Feature cost | 1 ≤ cost[i] ≤ 1,000 |
| Feature value | 0 ≤ value[i] ≤ 1,000 |
| Time limit | 2 seconds |

## 4. Output Format

The program prints exactly four lines:

```text
Greedy Value = G
Maximum Value = V
Selected = feature_names
Budget Used = B
```

Where:

- `G` represents the value obtained using the greedy approach.
- `V` represents the maximum achievable business value.
- `feature_names` contains the selected features in their original input order.
- `NONE` is printed if no feature is selected.
- `B` represents the total cost of the selected features.

### Tie-Breaking Rule

If multiple selections produce the same maximum value, the selection with the smallest total budget used must be reported.

If multiple selections have both the same maximum value and the same minimum budget, any one of them is accepted.

## 5. Algorithms Used

### 5.1 Greedy Algorithm

The greedy approach calculates the value-to-cost ratio of each feature.

\[
Ratio[i] = \frac{value[i]}{cost[i]}
\]

The features are sorted in decreasing order of this ratio.

The algorithm then considers the features one by one and selects a feature if it fits within the remaining budget.

The greedy approach provides a comparison value but does not guarantee an optimal solution for the 0/1 Knapsack Problem.

#### Why Greedy Does Not Always Produce the Optimal Solution

Consider Sample 1 with a budget of 50.

| Feature | Cost | Value | Value/Cost Ratio |
|---|---:|---:|---:|
| Auth | 10 | 60 | 6 |
| Search | 20 | 100 | 5 |
| Payments | 30 | 120 | 4 |

The greedy algorithm selects Auth and Search.

Total Cost = 10 + 20 = 30

Total Value = 60 + 100 = 160

However, selecting Search and Payments produces:

Total Cost = 20 + 30 = 50

Total Value = 100 + 120 = 220

Therefore, the greedy approach does not always produce the maximum possible value.

### 5.2 Dynamic Programming – 0/1 Knapsack

Dynamic Programming is used to find the optimal combination of features.

#### DP State

Define:

\[
DP[i][w]
\]

as the maximum business value obtainable using the first `i` features with a budget capacity of `w`.

#### Base Cases

\[
DP[0][w] = 0
\]

When no features are available, the maximum value is zero.

\[
DP[i][0] = 0
\]

When the available budget is zero, no feature can be selected because every feature has a positive cost.

#### Recurrence Relation

If the current feature cannot fit within the available capacity:

\[
DP[i][w] = DP[i-1][w]
\]

Otherwise:

\[
DP[i][w] =
\max
\begin{cases}
DP[i-1][w]\\
value[i] + DP[i-1][w-cost[i]]
\end{cases}
\]

The algorithm considers two possibilities:

1. Exclude the current feature.
2. Include the current feature and add its value to the optimal result for the remaining capacity.

The maximum of these two choices is stored in the DP table.

#### Table-Filling Order

The DP table is filled row by row.

- Rows represent the number of features considered.
- Columns represent the available budget.
- Each cell is calculated using values from the previous row.

This ensures that every feature is considered only once.

The final maximum value is obtained from:

\[
DP[n][W]
\]

## 6. Reconstruction of Selected Features

After filling the DP table, the selected features are reconstructed by tracing backwards through the table.

The reconstruction process follows these steps:

1. Find the smallest budget capacity that produces the maximum value.
2. Start from the last feature and move backwards.
3. Compare the current DP value with the value in the previous row.
4. If the values differ, the current feature is selected.
5. Subtract the selected feature's cost from the remaining capacity.
6. Reverse the selected feature list to maintain the original input order.

If no feature is selected, the program prints `NONE`.

This process also satisfies the minimum-budget tie-breaking rule.

## 7. Complexity Analysis

Let:

- `n` = Number of features
- `W` = Available budget

| Operation | Time Complexity |
|---|---|
| Greedy sorting | O(n log n) |
| Greedy selection | O(n) |
| DP table construction | O(nW) |
| Minimum budget search | O(W) |
| Feature reconstruction | O(n) |

### Overall Time Complexity

\[
O(nW)
\]

### Space Complexity

\[
O(nW)
\]

The DP table contains `(n+1) × (W+1)` entries.

### Why Is Dynamic Programming Pseudo-Polynomial?

The time complexity depends on the numerical value of the budget `W`, rather than the number of bits required to represent it.

The binary representation of `W` requires only O(log W) bits, but the algorithm performs O(nW) operations.

Therefore, the 0/1 Knapsack dynamic programming solution is called pseudo-polynomial.

At the maximum constraints, the DP table contains:

\[
201 \times 10001 = 2,010,201
\]

entries, which is manageable for the given constraints.

## 8. Test Cases

The implementation is tested using the two provided sample cases and additional edge cases.

| Test Case | Description | Expected Behaviour |
|---|---|---|
| Sample 1 | Three features with budget 50 | Greedy value 160 and maximum value 220 |
| Sample 2 | Six features with budget 15 | Greedy value 146 and maximum value 170 |
| Zero Budget | Available budget is zero | No feature selected |
| No Service Fits | All feature costs exceed the budget | Print NONE |
| Every Service Fits | Total cost of all features is within budget | All positive-value features can be selected |
| Tied Optima | Multiple combinations produce the same maximum value | Select a minimum-budget solution |
| Single Service | Only one feature is available | Select it if it fits and improves the objective |
| Large Input | Maximum allowed number of features and budget | Verify correctness and execution performance |

Actual test outputs and benchmark measurements will be documented after executing the implementation.

## 9. Compilation and Execution

### Compilation

Using g++:

```bash
g++ -std=c++17 -O2 -Wall -Wextra cloud_release_planner.cpp -o cloud_release_planner
```

### Execution

On Linux / Ubuntu:

```bash
./cloud_release_planner
```

On Windows PowerShell:

```powershell
.\cloud_release_planner.exe
```

The program reads input from standard input and prints the required output to standard output.

## 10. Repository Structure

```text
CO4-Cloud-Release-Budget-Planner/
│
├── README.md
├── cloud_release_planner.cpp
│
├── tests/
│   ├── sample1.txt
│   ├── sample2.txt
│   └── edge_cases.txt
│
├── benchmarks/
│   ├── generate_input.py
│   ├── run_benchmarks.py
│   └── results.csv
│
└── report/
    └── CO4_Cloud_Release_Budget_Planner_Report.docx
```

## 11. Conclusion

The Cloud Release Budget Planner demonstrates the difference between greedy optimization and dynamic programming.

The greedy algorithm selects features based on their value-to-cost ratio, but it may fail to produce the optimal combination.

The 0/1 Knapsack dynamic programming approach evaluates both inclusion and exclusion decisions for every feature and finds the maximum achievable business value within the available budget.

The reconstruction process identifies the selected features, maintains their original input order, and applies the minimum-budget tie-breaking rule.
