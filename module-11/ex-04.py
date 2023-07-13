class Point:
    def __init__(self, x, y):
        self.__x = None
        self.__y = None
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, x):
        if (type(x) == int) or (type(x) == float):
            self.__x = x

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, y):
        if (type(y) == int) or (type(y) == float):
            self.__y = y


class Vector:
    def __init__(self, coordinates: Point) -> None:
        self.coordinates = coordinates
        self.vector:dict = {0: coordinates.x, 1:coordinates.y}

    def __setitem__(self, index, value):
        if index in self.vector:
            self.vector[index] = value
        else:
            return 'Unkwown index'
            

    def __getitem__(self, index):
        return self.vector[index]