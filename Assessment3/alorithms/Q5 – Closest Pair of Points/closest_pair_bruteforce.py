import math


def closest_pair(points):

    min_distance = float('inf')
    closest_points = None

    n = len(points)

    for i in range(n):

        for j in range(i + 1, n):

            x1, y1 = points[i]
            x2, y2 = points[j]

            distance = math.sqrt(
                (x2 - x1) ** 2 +
                (y2 - y1) ** 2
            )

            if distance < min_distance:

                min_distance = distance
                closest_points = (points[i], points[j])

    return closest_points, min_distance


points = [
    (2, 3),
    (12, 30),
    (40, 50),
    (5, 1),
    (12, 10),
    (3, 4)
]

pair, distance = closest_pair(points)

print("Closest Pair:", pair)
print("Minimum Distance:", round(distance, 4))
