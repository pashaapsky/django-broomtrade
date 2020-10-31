
class Square():
    def __init__(self,height, width):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height


class Qube(Square):
    def __init__(self, height, width, z):
        super(Qube, self).__init__(width,height)
        self.z = z
    def volume(self):
        return self.area() * self.z


a = Qube(100,40,5)
c = a.area()
v = a.volume()



