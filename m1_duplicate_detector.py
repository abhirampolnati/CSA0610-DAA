# M1: Duplicate-Listing Detector
# ShopSphere Scalability Audit

def detect_duplicates(products):
    comparisons = 0
    duplicates = []

    n = len(products)

    for i in range(n - 1):
        for j in range(i + 1, n):
            comparisons += 1

            if (
                products[i]["title"] == products[j]["title"]
                and products[i]["seller"] == products[j]["seller"]
            ):
                duplicates.append(j)

    return duplicates, comparisons


# Sample product catalogue
products = [
    {"title": "iPhone 15", "seller": "Seller A"},
    {"title": "Samsung S24", "seller": "Seller B"},
    {"title": "iPhone 15", "seller": "Seller A"},
    {"title": "iPhone 15", "seller": "Seller C"},
]

duplicates, comparisons = detect_duplicates(products)

print("ShopSphere - Duplicate Listing Detector")
print("----------------------------------------")
print("Total products:", len(products))
print("Duplicate product indices:", duplicates)
print("Total comparisons:", comparisons)