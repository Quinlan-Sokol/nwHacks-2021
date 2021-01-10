from graphics import *
from math import sqrt, atan2, cos, ceil

class BackgroundCircle:
    def __init__(self, p, c, r, v):
        self.pos = p
        self.color = c
        self.radius = r
        self.vector = v

    def update(self, wSize, lst):
        prevPos = self.pos.clone()
        self.pos = Point(self.pos.x + self.vector.x,
                         self.pos.y + self.vector.y)

        # check circle collisions
        for c in lst:
            if c.pos != self.pos:
                d = sqrt((c.pos.x - self.pos.x)**2 + (c.pos.y - self.pos.y)**2)
                if d <= self.radius * 2:
                    self.pos = prevPos

                    # calculate collision
                    norm = Point(c.pos.x - self.pos.x,
                                 c.pos.y - self.pos.y)
                    length = sqrt(norm.x**2 + norm.y**2)
                    norm = Point(norm.x / length,
                                 norm.y / length)
                    tangent = Point(-norm.y, norm.x)

                    vel1 = self.vector
                    vel2 = c.vector
                    vel1Norm = vel1.x * norm.x + vel1.y * norm.y
                    vel1Tan = vel1.x * tangent.x + vel1.y * tangent.y
                    vel2Norm = vel2.x * norm.x + vel2.y * norm.y
                    vel2Tan = vel2.x * tangent.x + vel2.y * tangent.y

                    newVel1Norm = vel2Norm
                    newVel2Norm = vel1Norm

                    self.vector = Point(norm.x * newVel1Norm + tangent.x * vel1Tan,
                                        norm.y * newVel1Norm + tangent.y * vel1Tan)
                    c.vector = Point(norm.x * newVel2Norm + tangent.x * vel2Tan,
                                     norm.y * newVel2Norm + tangent.y * vel2Tan)

        #check borders
        left = self.pos.x - self.radius
        right = self.pos.x + self.radius
        bottom = self.pos.y + self.radius
        top = self.pos.y - self.radius
        if left < 0:
            self.vector = Point(self.vector.x * -1, self.vector.y)
            self.pos = prevPos
        elif right > wSize[0]:
            self.vector = Point(self.vector.x * -1, self.vector.y)
            self.pos = prevPos
        if top < 0:
            self.vector = Point(self.vector.x, self.vector.y * -1)
            self.pos = prevPos
        elif bottom > wSize[1]:
            self.vector = Point(self.vector.x, self.vector.y * -1)
            self.pos = prevPos
