class Robot:
	def __init__(self, direction=NORTH, xCoord=0, yCoord=0):
		self.bearing = direction
		self.coordinates = [xCoord, yCoord]


	def simulate(self, string):
		# Move according to string


	def advance(self):
		# Move forward one unit


	def turn_right(self):
		# Turn right


	def turn_left(self):
		# Turn left


class NORTH:
	def __init__(self):
		self = self


class EAST:
	def __init__(self):
		self = self


class SOUTH:
	def __init__(self):
		self = self


class WEST:
	def __init__(self):
		self = self