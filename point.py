class Point:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def printAttributes(self):
        print("x =", self.__x, "\ny =", self.__y)

    def translate(self, dx, dy):
        self.__x += dx  # syntax tips: same as self.x = self.x + dx
        self.__y += dy

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self, newX):
        self.__x = newX

    def setY(self, newY):
        self.__y = newY