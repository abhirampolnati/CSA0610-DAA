
# M2: API Rate Limiter
# ShopSphere Scalability Audit


def audit_requests(n):
    """Count audit operations for each power of two below n."""
    i = 1
    audit_count = 0

    while i < n:
        for _ in range(i):
            audit_count += 1
        i *= 2

    return audit_count


if __name__ == "__main__":
    n = 8
    result = audit_requests(n)

    print("ShopSphere - API Rate Limiter")
    print("-----------------------------")
    print("Input size:", n)
    print("Total Audit operations:", result)

