
from point import Point



class CartesianPlane:


    __VALID_POINT_NAMES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    __INVALID_POINT_NAMES = "0123456789-=+_)(*&^%$#@!`~{[]}\|:;,<>./?"     
    __INDEX_TO_WORD_CONVERSION = {
        0: 'first',
        1: 'second',
        2: 'third',
        3: 'fourth',
        4: 'fifth',
        5: 'sixth',
        6: 'seventh',
        7: 'eighth',
        8: 'ninth',
        9: 'tenth'
    }
    

    def __init__(self):
        self.__listOfPoints = []


    def __getPointXandYCoordinates(self):
        while True:
            try:
                xCoordinate = int(input('Enter x coordinate of point: '))
                yCoordinate = int(input('Enter y coordinate of point: '))
                break
            except ValueError: 
                print('\nERROR: please input a correct value for coordinate (integer)\n')
                continue
        return (xCoordinate, yCoordinate)


    def __getPointName(self):
        while True:
            try:
                name = str(input("Enter the name of point: "))
                if len(name) > 1: 
                    print("\nMake sure you are using a one letter name (a, A, b, B)\n")
                    continue
                if name in self.__INVALID_POINT_NAMES:
                    print("\nInvalid Input! cannot set symbols as a name of point!\n")
                    continue
                break
            except ValueError:
                print('\nError\n')
                continue

        return name


    def addPoint(self, index=None):
        print("\nAdd Point\n")
        xCoordinate, yCoordinate = self.__getPointXandYCoordinates()
        name = self.__getPointName()
        _index = len(self.__listOfPoints) if index == None else index

        self.__listOfPoints.append(Point(xCoordinate, yCoordinate, name, _index))
        print(f"\nPoint {name}: (x: {xCoordinate}, y: {yCoordinate}) added in the Cartesian Plane\n")

    
    def addMultiplePoints(self):
        numberOfPoints = int(input("Enter number of points to add: "))

        if numberOfPoints <= 1:
            print("\nCannot add only 1 point, if you want to add only one point use Add Point method\n")
            return 

        for i in range(numberOfPoints):
            self.addPoint(i)

    
    def displayAllPoints(self):
        if len(self.__listOfPoints) == 0:
            print('\nNo Points in the Cartesian Plane\n')
            return 

        print('\nDisplaying Points...\n')
        for point in self.__listOfPoints:
            print(point)
        print('\n')
    

    def getPointFromIndex(self, index: int):
        if index > len(self.__listOfPoints) - 1:
            print('\nIndex out of Range\n')
            return None

        return self.__listOfPoints[index]
    

    def getPointFromName(self, name: str):
        for point in self.__listOfPoints:
            if point.name == name:
                return point
        return None


    def getNumberOfPoints(self):
        return len(self.__listOfPoints)


    def __askUserForPoints(self, numberOfPoints: int):
        points = [None] * numberOfPoints 

        print("Make sure to be consistent, if you used name for the first point, then use name for the second point.\n")
        for i in range(numberOfPoints):
            while True:
                point = input(f"Enter {self.__INDEX_TO_WORD_CONVERSION.get(i)} point to use: (name or index): ")

                if point in self.__VALID_POINT_NAMES and len(point) > 1:
                    print('\nERROR\n')
                    continue
                
                break
            points[i] = (point)

        return points


    def __convertInputToPoints(self, inputs):
        if inputs[0] in self.__VALID_POINT_NAMES:
            return [self.getPointFromName(val) for val in inputs]

        return [self.getPointFromIndex(int(val)) for val in inputs]


    def __getXandYCoordinatesOfPoints(self, arr):
        coordinates = {}
        for idx, val in enumerate(arr):
            x, y = val.getCoordinates()
            coordinates[F"{self.__INDEX_TO_WORD_CONVERSION.get(idx)}X"] = x
            coordinates[F"{self.__INDEX_TO_WORD_CONVERSION.get(idx)}Y"] = y

        return coordinates


    def __getSlope(self, ySubOne, ySubTwo, xSubOne, xSubTwo):
        slope = (ySubTwo - ySubOne) / (xSubTwo - xSubOne)
        return slope



    # solution for distance between two points 
    # d = sqrt((x2-x1)^2 + (y2-y1)^2)
    # this is a private utility function for the distanceBetweenTwoPoints method
    def __solveDistanceOfPoints(self, coordinates):
        xComponent = (coordinates.get('secondX') - coordinates.get('firstX')) ** 2
        yComponent = (coordinates.get('secondY') - coordinates.get('firstY')) ** 2
        return (xComponent + yComponent) ** 0.5

                
    def distanceBetweenTwoPoints(self):
        if len(self.__listOfPoints) < 2:
            print('\nCannot execute because number of points is Insufficient\n')
            return

        self.displayAllPoints()
        firstPoint, secondPoint = self.__askUserForPoints(2)
        points = self.__convertInputToPoints([firstPoint, secondPoint])
        coordinates = self.__getXandYCoordinatesOfPoints(points)
        distance = self.__solveDistanceOfPoints(coordinates) 
        print(f'\nThe distance is {distance}\n')
        return distance


    def __pointsAreColinear(self, firstY, firstX, secondY, secondX, thirdY, thirdX):
        firstSecondSlope = self.__getSlope(firstY, secondY, firstX, secondX)
        secondThirdSlope = self.__getSlope(secondY, thirdY, secondX, thirdX)
        firstThirdSlope = self.__getSlope(firstY, thirdY, firstX, thirdX)
        print(f"""
            slope#1 = {firstSecondSlope}
            slope#2 = {secondThirdSlope}
            slope#3 = {firstThirdSlope}
              """)
        return firstSecondSlope == secondThirdSlope and secondThirdSlope == firstThirdSlope 

    
    def __getLineEndpoints(self, points):
        maxX = points[0].getCoordinates()[0]
        minX = points[0].getCoordinates()[0]
        maxY = points[0].getCoordinates()[1]
        minY = points[0].getCoordinates()[1]
        _min = points[0]
        _max = points[0]

        for point in points:
            x, y = point.getCoordinates()
            if x >= maxX and y >= maxY:
                _max = point
                maxX = x
                maxY = y

            if x <= minX and y <= minY:
                _min = point
                minX = x
                minY = y

        return [_min, _max]


    # A = 1/2 * abs(x1y2 + x2y3 + x3y1 - x1y3 - x2y1 - x3y2)
    def __solveAreaOfTriangle(self, firstY, firstX, secondY, secondX, thirdY, thirdX):
        firstSolution = (firstX*secondY) + (secondX*thirdY) + (thirdX*firstY) - (firstX*thirdY) - (secondX*firstY) - (thirdX*secondY)
        return abs(firstSolution) / 2


    def determineIfPointsAreColinearOrCoplanar(self):
        if (len(self.__listOfPoints) < 3):
            print('\nCannot execute because number of points is Insufficient\n')
            return

        self.displayAllPoints()
        firstPoint, secondPoint, thirdPoint = self.__askUserForPoints(3)
        points = self.__convertInputToPoints([firstPoint, secondPoint, thirdPoint])
        coordinates = self.__getXandYCoordinatesOfPoints(points)
        firstX = coordinates.get('firstX')
        firstY = coordinates.get('firstY')
        secondX = coordinates.get('secondX')
        secondY = coordinates.get('secondY')
        thirdX = coordinates.get('thirdX')
        thirdY = coordinates.get('thirdY')

        if (self.__pointsAreColinear(firstY, firstX, secondY, secondX, thirdY, thirdX)):
            print("\nThe 3 points are Colinear\n")
            minPoint, maxPoint = self.__getLineEndpoints(points)
            coordinates = self.__getXandYCoordinatesOfPoints([minPoint, maxPoint])
            distance = self.__solveDistanceOfPoints(coordinates)
            print(f"The distance of endpoints is {distance}")
            return 

        print("\nThe 3 points are Coplanar\n")
        print(coordinates)
        area = self.__solveAreaOfTriangle(firstY, firstX, secondY, secondX, thirdY, thirdX)
        print(f"\nThe area of the triangle is {area}\n")



cart = CartesianPlane()
cart.addMultiplePoints()
#cart.distanceBetweenTwoPoints()
cart.determineIfPointsAreColinearOrCoplanar()

