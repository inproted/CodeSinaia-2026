import math

class Point:
	"""A point in 2D Euclidean space."""

	# Class attributes:
	__slots__ = (
		"_name", # text
		"_x",    # float
		"_y"     # float
	)

	# Called automatically when creating a new Point(x, y).
	def __init__(self, name, x, y):
		self._name = name
		self._x = x
		self._y = y

	# Called by print(obj) and str(obj) for a user-friendly text.
	def __str__(self):
		"""
		Returns a description string of the object. I.e.: "Point_P(x=1, y=2)
		"""
		return f"Point_{self.__repr__()}"
	
	# Called by repr(obj) and often used for priting objects within a tuple, list, set, dictionary, or for debugging
	def __repr__(self):
		"""
		Returns a debug string of the object. I.e: "P(x=1, y=2)"
		"""
		return f"{self._name}(x={self._x}, y={self._y})"

	# Called for == to compare two Point objects by their coordinates.
	def __eq__(self, other):
		return self._x == other._x and self._y == other._y if isinstance(other, Point) else False

	def __hash__(self):
		return hash(self._name)

	# Compute straight line distance to another point.
	def distance(self, other) -> int:
		"""
		Return the Euclidean distance from this point to another point.
		Args:
			other: Another Point object.
		Returns:
			A float representing the straight-line distance between the two points.
		"""
		return math.sqrt((self._x - other._x)**2 + (self._y - other._y)**2)

print(f"Point.py: __name__ = {__name__}")
if __name__ == "__main__":
	orig = Point("Origin", 0, 0)
	p1 = Point("A", 10, 10)
	p2 = Point("B", 10, 10)
	
	# print all points as a sequence of parameters: uses __str__
	print(orig.__repr__(), p1, p2, sep="\n", end="\n--------\n")
	# print all points grouped into one tuple: uses __repr__
	print(f"All points: {(orig, p1, p2)}", end="\n--------\n")

	def yes_no(test):
		return "Yes" if test else "No"
	
	print(f"is {p1._name} the ORIGIN ?> {yes_no(orig == p1)}")
	print(f"is {p1._name} same as {p2._name} ?> {yes_no(p1 == p2)}")
	print(f"distance between {p1._name} and {p2._name} = {p1.distance(p2)}")
	print(f"distance of {p1._name} from ORIGIN = {p1.distance(orig)}")
