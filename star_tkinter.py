import numpy

class Star:
    width = 0.
    height = 0.
    speed = 0.
    colors = ['white', 'white', 'white', 'white', 'yellow', 'red', 'blue', 'white', 'white', 'white']

    def __init__(self, w, h, s):
        Star.width = w
        Star.height = h
        Star.speed = s
        Star.Rng = numpy.random.default_rng()

        self.appear()


    def get_screen_coords(self):
        return (self.x + Star.width/2, self.y + Star.height/2, self.radius * (1- self.z / (2 * Star.width)))

    def resize(self, w, h):
        Star.width = w
        Star.height = h

    def appear(self):
        self.x = Star.Rng.integers(low = - self.width/2 - 1, high = self.width/2+1)
        self.y = Star.Rng.integers(low = - self.height/2-1, high = self.height/2 + 1)
        self.z = 2 * Star.width * Star.Rng.random()
        self.radius = 6 * Star.Rng.random()
        self.color = Star.colors[Star.Rng.integers(low = 0, high = 10)]

    def update(self):
        if self.z == 0:
            self.appear()

        if (self.x != 0):
            self.x = self.x + numpy.sign(self.x) * int(Star.speed / self.z * Star.width)
        if (self.y != 0):
            self.y = self.y + numpy.sign(self.y) * int(Star.speed / self.z * Star.height)

        if (self.x == 0 and self.y == 0):
            self.appear()

        if (numpy.absolute(self.x) > Star.width/2 or numpy.absolute(self.y) > Star.height/2):
            self.appear()

        self.z = self.z - Star.speed

        