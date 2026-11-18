def standard_multiply(x, y):

    # Base case
    if x < 10 or y < 10:
        return x * y

    # Find the number of digits
    n = max(len(str(x)), len(str(y)))

    m = n // 2

    power = 10 ** m

    # Divide the numbers
    a = x // power
    b = x % power

    c = y // power
    d = y % power

    # Recursive multiplication
    ac = standard_multiply(a, c)
    ad = standard_multiply(a, d)
    bc = standard_multiply(b, c)
    bd = standard_multiply(b, d)

    # Combine the results
    result = (ac * power * power) + ((ad + bc) * power) + bd

    return result


x = 1234
y = 5678

result = standard_multiply(x, y)

print("First Number:", x)
print("Second Number:", y)
print("Product:", result)
