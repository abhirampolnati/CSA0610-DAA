def karatsuba(x, y):

    # Base case
    if x < 10 or y < 10:
        return x * y

    # Find the maximum number of digits
    n = max(len(str(x)), len(str(y)))

    m = n // 2

    power = 10 ** m

    # Divide the numbers
    a = x // power
    b = x % power

    c = y // power
    d = y % power

    # Three recursive multiplications
    p = karatsuba(a, c)
    q = karatsuba(b, d)
    r = karatsuba(a + b, c + d)

    # Calculate the middle term
    middle = r - p - q

    # Combine the results
    result = (p * power * power) + (middle * power) + q

    return result


x = 1234
y = 5678

result = karatsuba(x, y)

print("First Number:", x)
print("Second Number:", y)
print("Product:", result)
