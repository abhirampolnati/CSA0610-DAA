 #M5: Sales Analytics Engine
# ShopSphere Scalability Audit
# Recurrence: T(n) = 2T(n/2) + n log2(n)


import math


def sales_analytics(n):
    if n <= 1:
        return 1

    half = n // 2

    # Recursively process both halves
    left_work = sales_analytics(half)
    right_work = sales_analytics(half)

    # Additional sorting and merging work
    processing_work = n * math.log2(n)

    return left_work + right_work + int(processing_work)


# Demonstration
n = 8

total_work = sales_analytics(n)

print("ShopSphere - Sales Analytics Engine")
print("-----------------------------------")
print("Input size:", n)
print("Estimated recurrence work:", total_work)
print("Theoretical time complexity: Theta(n * (log n)^2)")
