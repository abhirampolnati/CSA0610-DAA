# DAA Assignment 1
# Experimental Performance Analysis
# Student Record Retrieval System

import time
import csv
import random
import matplotlib.pyplot as plt

from algorithms import (
    linear_search,
    binary_search,
    create_hash_table,
    hash_search
)


def benchmark_algorithms():

    # Dataset sizes for the experiment
    dataset_sizes = [1000, 10000, 100000, 1000000]

    results = []

    print("\nSTUDENT RECORD RETRIEVAL - BENCHMARK")
    print("=" * 75)

    print(
        f"{'Records':>12} | {'Linear (ms)':>12} | "
        f"{'Binary (ms)':>12} | {'Hash (ms)':>12}"
    )

    print("-" * 75)

    for size in dataset_sizes:

        # Generate unique registration numbers
        student_records = list(range(100000000, 100000000 + size))

        # Select a target near the end to make linear search meaningful
        target = student_records[-1]

        # Prepare sorted data for binary search
        sorted_records = sorted(student_records)

        # Build the hash table separately from lookup timing
        start = time.perf_counter()
        hash_table = create_hash_table(student_records)
        hash_build_time = time.perf_counter() - start

        # Measure Linear Search
        start = time.perf_counter()
        linear_result = linear_search(student_records, target)
        linear_time = time.perf_counter() - start

        # Measure Recursive Binary Search
        start = time.perf_counter()
        binary_result = binary_search(
            sorted_records,
            target,
            0,
            len(sorted_records) - 1
        )
        binary_time = time.perf_counter() - start

        # Measure Hash Table Lookup
        start = time.perf_counter()
        hash_result = hash_search(hash_table, target)
        hash_time = time.perf_counter() - start

        # Validate results
        assert linear_result != -1
        assert binary_result != -1
        assert hash_result != -1

        # Convert seconds to milliseconds
        linear_ms = linear_time * 1000
        binary_ms = binary_time * 1000
        hash_ms = hash_time * 1000
        build_ms = hash_build_time * 1000

        results.append([
            size,
            linear_ms,
            binary_ms,
            hash_ms,
            build_ms
        ])

        print(
            f"{size:>12} | {linear_ms:>12.4f} | "
            f"{binary_ms:>12.4f} | {hash_ms:>12.4f}"
        )

    # Save benchmark results to a CSV file
    with open(
        "benchmark_results.csv",
        "w",
        newline=""
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Dataset Size",
            "Linear Search (ms)",
            "Binary Search (ms)",
            "Hash Lookup (ms)",
            "Hash Table Build (ms)"
        ])

        writer.writerows(results)

    print("\nResults saved to benchmark_results.csv")

    # Generate performance graph
    sizes = [row[0] for row in results]

    plt.figure(figsize=(10, 6))

    plt.plot(
        sizes,
        [row[1] for row in results],
        marker="o",
        label="Linear Search"
    )

    plt.plot(
        sizes,
        [row[2] for row in results],
        marker="s",
        label="Recursive Binary Search"
    )

    plt.plot(
        sizes,
        [row[3] for row in results],
        marker="^",
        label="Hash Table Lookup"
    )

    plt.xscale("log")
    plt.yscale("log")

    plt.xlabel("Number of Student Records")
    plt.ylabel("Search Time (milliseconds)")
    plt.title("Performance Comparison of Search Algorithms")

    plt.legend()
    plt.grid(True)
    plt.tight_layout()

    plt.savefig("performance_plot.png", dpi=300)

    plt.show()

    print("Graph saved to performance_plot.png")


if __name__ == "__main__":
    benchmark_algorithms()

