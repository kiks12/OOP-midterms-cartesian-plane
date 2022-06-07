

class Point:

    def __init__(self, x: int, y: int, name: str, index: int):
        self.__x = x
        self.__y = y
        self.name = name
        self.index = index

    def getCoordinates(self):
        return [self.__x, self.__y]

    def setX(self, x):
        self.__x = x

    def setY(self, y):
        self.__y = y

    def __str__(self):
        return f"Point {self.name} (x: {self.__x}, y: {self.__y} index: {self.index})"
