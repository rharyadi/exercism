NORTH = (0,1)
EAST = (1,0)
SOUTH = (0,-1)
WEST = (-1,0)


class Robot(object):
    def __init__(self, bearing=NORTH, x=0, y=0):
        self.bearing = bearing
        self.coordinates = x, y
        self.update_components()

    def update_components(self):
        self.bearing_x, self.bearing_y = self.bearing
        self.x, self.y = self.coordinates

    def advance(self):
        self.coordinates = (self.x + self.bearing_x, self.y + self.bearing_y)
        self.update_components()
    
    # Ref: https://en.wikipedia.org/wiki/Rotation_matrix
    def turn_left(self):
        self.bearing = -self.bearing_y, self.bearing_x
        self.update_components()

    def turn_right(self):
        self.bearing = self.bearing_y, -self.bearing_x
        self.update_components()

    def simulate(self,instructions):
        for ins in instructions:
            if ins == 'A':
                self.advance()
            if ins == 'L':
                self.turn_left()
            if ins == 'R':
                self.turn_right()
