from pathlib import Path
import random
import numpy
from point import Point

DATA_FILE = Path(__file__).with_name("dots.tsv")
ORIGIN = Point("ORIGIN", 0, 0)
NPOINTS_AFAR = 10
EPICENTER_RADIUS = 100

# loads the data file
def load_data(filename) -> list[Point]:
    points = []
    with open(filename, encoding="utf-8") as f:
        for line_number, line in enumerate(f, start=1):
            if line_number == 1:
                # Skip header: Name\tX\tY
                continue
            parts = line.strip("\n").split("\t")
            point = Point(parts[0], int(parts[1]), int(parts[2]))
            points.append(point)
        return points

# move a point closer to the origin
def move_point(point) -> bool:
    """Move one point one step closer to the origin.
        The coordinate farthest from the origin gets closer by one unit,
        unless they are equally away, case in which both get closer by a random
        number of units between 2 and 5 (inclusive)
    Args:
        point: Point to update in place.
    Returns:
        True if the point reaches the origin after this move, else False.
    """
    if abs(point._x) > abs(point._y):
        point._x += -numpy.sign(point._x)
    elif abs(point._y) > abs(point._x):
        point._y += -numpy.sign(point._y)
    else:
        point._x += -numpy.sign(point._x) * random.randint(2, 5)
        point._y += -numpy.sign(point._y) * random.randint(2, 5)
    return point == ORIGIN

# gets the nAfar points fartherest away from the origin
def get_points_afar(points, nAfar) -> list[Point]:
    maxPoints = []
    # as long as there are still points and maxPoints to extract ...
    while len(points) > 0 and len(maxPoints) < nAfar:
        # assume the first is our max
        maxPoint = points.pop(0)
        # and rotate and check the ones left in the points queue...
        nPointsToCheck = len(points)
        while nPointsToCheck > 0:
            # extract the point in the front of the queue ... and
            point = points.pop(0)
            # if it's a new maximum..
            if maxPoint.distance(ORIGIN) < point.distance(ORIGIN):
                # swap it with the previous maximum
                points.append(maxPoint)
                maxPoint = point
            else:
                # otherwise, put the point back to the end of the queue
                points.append(point)
            nPointsToCheck -= 1
        # now, maxPoint contains another maximum to be added to the result
        maxPoints.append(maxPoint)
    return maxPoints

# Main entry point in the program
if __name__ == "__main__":
    points = load_data(DATA_FILE)

    print(f"-------- Iterate forward through each index --------")
    # range(n) generates all numbers from 0 to n-1
    for i in range(len(points)):
        print(f"{i:3d}: {points[i]}")

    print(f"-------- Iterate backwards skipping every other index --------")
    # range(start, end, step) generates all numbers from start (inclusive) to end (exclusive) with a given step
    for i in range(len(points)-1, -1, -2):
        print(f"{i:3d}: {points[i]}")

    print(f"-------- Race all {len(points)} points towards the origin ---------")
    # rotate through each point in the list moving each a little closer towrads origin, until one reaches it.
    # the point reaching the origin is removed from the set
    while True:
        point = points.pop(0)
        if move_point(point):
            print(point)
            break
        points.append(point)

    print(f"-------- After the race, extract the {NPOINTS_AFAR} points fartherest away --------")
    maxPoints = get_points_afar(points, NPOINTS_AFAR)
    print(*maxPoints, sep="\n")

    print(f"-------- Rename the remaining {len(points)} based on position within the epicenter --------")
    for p in points:
        p._name = ("IN-" if p.distance(ORIGIN) < EPICENTER_RADIUS else "OUT-") + p._name
    print(*points, sep="\n")
