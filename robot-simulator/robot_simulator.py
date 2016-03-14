class NORTH:
	pass

class SOUTH:
	pass

class EAST:
	pass

class WEST:
	pass


class Robot:
	def __init__(self, direction=NORTH, xCoord=0, yCoord=0):
		self.bearing = direction
		self.coordinates = (xCoord, yCoord)
		self.directions = [NORTH, EAST, SOUTH, WEST]

	def simulate(self, string):
		for command in string:
			if command == 'L':
				self.turn_left()
			elif command == 'R':
				self.turn_right()
			else:
				self.advance()

	def advance(self):
		x, y = self.coordinates
		if self.bearing == NORTH:
			y += 1
		elif self.bearing == SOUTH:
			y -= 1
		elif self.bearing == EAST:
			x += 1
		else:
			x -= 1
		self.coordinates = (x, y)

	def turn_right(self):
		index = self.directions.index(self.bearing)
		if index  < len(self.directions) - 1:
			self.bearing = self.directions[index + 1]
		else:
			self.bearing = self.directions[0]
		print(self.bearing, ' + ', index)

	def turn_left(self):
		index = self.directions.index(self.bearing)
		if index < len(self.directions):
			self.bearing = self.directions[index - 1]
		else:
			self.bearing = self.directions[0]
		print(self.bearing, ' + ', index)