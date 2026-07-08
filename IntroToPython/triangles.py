from pathlib import Path
from point import Point

# Given a list of 2D Points, loaded from a DATA_FILE, print to the console
# the triplets of Points which are forming isoscelles triangles.
# Each Point is a line in DATA_FILE and it contains a name and the x,y coordinates

DATA_FILE = Path(__file__).with_name("shapes.tsv")

# loads the data file
def load_data(filename) -> list[Point]:
    points = []
    with open(filename, encoding="utf-8") as f:
        line_iter = iter(f)
        # skip the header line, then read the first line, if any
        next(line_iter, None)
        line = next(line_iter, None)
        while line is not None:
            name, x, y = line.strip("\n").split("\t")
            points.append(Point(name, int(x), int(y)))
            line = next(line_iter, None)
    return points

# create a map of segments: { distance : [{p1, p2},..] }
# the segment is a set since set operations are going to be needed later
def map_segments(points) -> dict[float, list[set[Point]]]:
    segments_map = {}
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            p1 = points[i]
            p2 = points[j]
            d = p1.distance(p2)
            if d not in segments_map:
                segments_map[d] = []
            segments_map[d].append({p1, p2})
    return segments_map

# create a map of isocelles triangles: { distance, [[p1, p2, p3],..] }
# the vertex common to the two equal sides is the first in the triangle
def map_triangles(distances) -> dict[float, list[list[Point]]]:
    triangles_map = {}
    for distance, segments in distances.items():
        triangles = []
        for i in range(len(segments)):
            for j in range(i+1, len(segments)):
                if len(segments[i] | segments[j]) == 3:
                    common_vertex = segments[i] & segments[j]
                    triangle = []
                    triangle.extend(common_vertex)
                    triangle.extend(segments[i] - common_vertex)
                    triangle.extend(segments[j] - common_vertex) 
                    triangles.append(triangle)
        if len(triangles) > 0:
            triangles_map[distance] = triangles
    return triangles_map

# Main entry point in the program
if __name__ == "__main__":
    points = load_data(DATA_FILE)
    segments = map_segments(points)
    triangles = map_triangles(segments)
    isoscelles = []
    for triangles in triangles.values():
        isoscelles.extend(triangles)
    for i, triangle in enumerate(isoscelles):
        print(f"{i+1:<2d} > {triangle[0]._name} {triangle[1]._name} {triangle[2]._name}")
