from pathlib import Path
from point import Point

ORIGIN = Point("Origin", 0, 0)
DATA_FILE = Path(__file__).with_name("dots.tsv")

# loads the data file
def load_data(filename) -> list[Point]:
	with open(filename, encoding="utf-8") as f:
		next(f)  # Skip header
		return [Point(parts[0], int(parts[1]), int(parts[2]))
				for parts in (line.strip().split("\t")
				for line in f)]
	
def strings_name_distance(points):
	for p in points:
		yield f"{p._name} {p.distance(ORIGIN):.2f}"

# Main entry point in the program
if __name__ == "__main__":
	points = load_data(DATA_FILE)
	print("---- Points sorted alphabetically ----")
	sorted_by_names = sorted(points, key=lambda p : p._name)
	[print(p.__repr__()) for p in sorted_by_names]

	print("---- Points sorted on distance to origin ----")
	sorted_by_distance = sorted(points, key=lambda p: -p.distance(ORIGIN))
	[print(s) for s in strings_name_distance(sorted_by_distance)]