import math


def distance(p1, p2):

    return math.sqrt(
        (p1[0] - p2[0]) ** 2 +
        (p1[1] - p2[1]) ** 2
    )


def brute_force(points):

    min_dist = float('inf')
    pair = None

    for i in range(len(points)):

        for j in range(i + 1, len(points)):

            d = distance(points[i], points[j])

            if d < min_dist:

                min_dist = d
                pair = (points[i], points[j])

    return pair, min_dist


def closest_pair_recursive(px, py):

    n = len(px)

    # Base case
    if n <= 3:
        return brute_force(px)

    mid = n // 2

    midpoint = px[mid]

    # Divide points into two halves
    left_x = px[:mid]
    right_x = px[mid:]

    left_set = set(left_x)

    left_y = []
    right_y = []

    for point in py:

        if point in left_set:
            left_y.append(point)
        else:
            right_y.append(point)

    # Recursive calls
    left_pair, left_dist = closest_pair_recursive(
        left_x, left_y
    )

    right_pair, right_dist = closest_pair_recursive(
        right_x, right_y
    )

    # Find minimum distance
    if left_dist <= right_dist:

        min_pair = left_pair
        min_dist = left_dist

    else:

        min_pair = right_pair
        min_dist = right_dist

    # Create strip around dividing line
    strip = [
        point for point in py
        if abs(point[0] - midpoint[0]) < min_dist
    ]

    # Check points in the strip
    for i in range(len(strip)):

        for j in range(i + 1, min(i + 8, len(strip))):

            d = distance(strip[i], strip[j])

            if d < min_dist:

                min_dist = d
                min_pair = (strip[i], strip[j])

    return min_pair, min_dist


def closest_pair(points):

    if len(points) < 2:
        raise ValueError("At least two points are required.")

    if len(set(points)) != len(points):
        raise ValueError("Points must be distinct.")

    px = sorted(points, key=lambda p: (p[0], p[1]))

    py = sorted(points, key=lambda p: (p[1], p[0]))

    return closest_pair_recursive(px, py)


points = [
    (2, 3),
    (12, 30),
    (40, 50),
    (5, 1),
    (12, 10),
    (3, 4)
]

pair, min_distance = closest_pair(points)

print("Closest Pair:", pair)
print("Minimum Distance:", round(min_distance, 4))
