
# ShopSphere Scalability Audit
# Generate CSV results using Python

import csv
import math

SERVER_RATE = 10**8
N = 1_000_000


def calculate_m1(n):
    return n * (n - 1) // 2


def calculate_m2(n):
    if n <= 1:
        return 0

    return 2 ** math.ceil(math.log2(n)) - 1


def calculate_m3(n):
    return math.ceil(math.log2(n + 1))


def calculate_m4_current(n):
    # Illustrative recurrence model:
    # T(n) = 4T(n/2) + n
    # T(1) = 1, with n a power of 2
    return 2 * n**2 - n


def calculate_m4_redesigned(n):
    # Illustrative recurrence model:
    # T(n) = 2T(n/2) + n
    # T(1) = 1, with n a power of 2
    return n * (math.log2(n) + 1)


def calculate_m5(n):
    # Asymptotic growth indicator only.
    # Not an exact operation count.
    return n * (math.log2(n) ** 2)


results = [
    ("M1 - Duplicate Detector", calculate_m1(N), "Theta(n^2)"),
    ("M2 - API Rate Limiter", calculate_m2(N), "Theta(n)"),
    ("M3 - Binary Search", calculate_m3(N), "Theta(log n)"),
    ("M4 - Current Recommendation", calculate_m4_current(N), "Theta(n^2)"),
    ("M4 - Redesigned Recommendation", calculate_m4_redesigned(N), "Theta(n log n)"),
    ("M5 - Sales Analytics", calculate_m5(N), "Theta(n(log n)^2)"),
]


with open("scalability_results.csv", "w", newline="") as file:
    writer = csv.writer(file)

    writer.writerow([
        "Module",
        "Input_Size",
        "Operation_Count_or_Growth_Indicator",
        "Time_Complexity",
        "Estimated_Time_Seconds",
        "Result_Type"
    ])

    for module, operations, complexity in results:
        runtime = operations / SERVER_RATE

        result_type = (
            "Asymptotic growth indicator; not an exact count"
            if module == "M5 - Sales Analytics"
            else "Recurrence/model-based estimate"
            if module.startswith("M4")
            else "Operation-count estimate"
        )

        writer.writerow([
            module,
            N,
            operations,
            complexity,
            runtime,
            result_type
        ])

print("CSV file generated successfully!")
print("File: scalability_results.csv")
print("Input size:", N)
print("Server rate:", f"{SERVER_RATE:,} operations/second")
