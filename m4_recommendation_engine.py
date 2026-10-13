# M4: Recommendation Engine
# ShopSphere Scalability Audit

# Current design: T(n) = 4T(n/2) + n
def current_design(n):
    if n <= 1:
        return 1

    half = n // 2

    # Four recursive calls
    work = (
        current_design(half)
        + current_design(half)
        + current_design(half)
        + current_design(half)
    )

    # Linear merging work
    work += n

    return work


# Redesigned version: T(n) = 2T(n/2) + n
def redesigned_design(n):
    if n <= 1:
        return 1

    half = n // 2

    # Two recursive calls
    work = (
        redesigned_design(half)
        + redesigned_design(half)
    )

    # Linear merging work
    work += n

    return work


# Demonstration
n = 8

current_work = current_design(n)
redesigned_work = redesigned_design(n)

print("ShopSphere - Recommendation Engine")
print("----------------------------------")
print("Input size:", n)

print("\nCurrent Design")
print("Estimated recurrence work:", current_work)

print("\nRedesigned Version")
print("Estimated recurrence work:", redesigned_work)

