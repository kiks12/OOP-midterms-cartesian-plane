
from point import Point
from cartesianPlaneService import CartesianPlaneService


class CartesianPlane:

    def __init__(self, service):
        self.__listOfPoints = []
        self.service = service

    def exec(self):
        while True:
            """
            print instructions
            """
            print('\nCARTESIAN PLANE PROGRAM\n')
            print('\nInstructions\n')
            print('[1] Add a single Point')
            print('[2] Add Multiple Points')
            print('[3] Show Number of Points')
            print('[4] Display All Points')
            print('[5] Check Distance between two points')
            print('[6] Check if 3 points are Colinear or Coplanar')
            print('[0] exit\n')

            try:
                option = int(input("Enter your option: "))
                if option not in [0,1,2,3,4,5,6]:
                    print('\nError: unknown option, please input only 0-6')
                    continue
            except ValueError:
                print('\nError: input only integers from 0-6')
                continue

            if option == 1:
                cartesian.addPoint()
                continue

            if option == 2:
                cartesian.addMultiplePoints()
                continue

            if option == 3:
                print(f"\nThe number of points in the Cartesian Plane is {self.getNumberOfPoints()}") 
                continue

            if option == 4:
                cartesian.displayAllPoints()
                continue

            if option == 5:
                cartesian.distanceBetweenTwoPoints()
                continue

            if option == 6:
                cartesian.determineIfPointsAreColinearOrCoplanar()
                continue

            if option == 0:
                print('Exiting...')
                break

    def addPoint(self):
        print("\nADD POINT\n")
        xCoordinate, yCoordinate = self.service.askUserForXandYCoordinates()
        name = self.service.askUserForPointName()
        _index = len(self.__listOfPoints)

        self.__listOfPoints.append(Point(xCoordinate, yCoordinate, name, _index))
        print(f"\nPoint {name}: (x: {xCoordinate}, y: {yCoordinate}) added in the Cartesian Plane\n")

    def addMultiplePoints(self):
        print("\nADD MULTIPLE POINTS\n")
        numberOfPoints = int(input("\nEnter number of points to add: "))

        if numberOfPoints <= 1:
            print("\nCannot add only 1 point, if you want to add only one point use Add Point method\n")
            return 

        for _ in range(numberOfPoints):
            self.addPoint()

    def displayAllPoints(self):
        if len(self.__listOfPoints) == 0:
            print('\nNo Points in the Cartesian Plane\n')
            return 

        print('\nALL POINTS\n')
        for point in self.__listOfPoints:
            print(point)
        print()

    def getPoint(self, _input):
        if _input in self.service.VALID_POINT_NAMES:
            return self.service.getPointFromName(_input, self.__listOfPoints)
        return self.service.getPointFromIndex(int(_input), self.__listOfPoints)

    def getNumberOfPoints(self):
        return len(self.__listOfPoints)

    def __getSlope(self, ySubOne, ySubTwo, xSubOne, xSubTwo):
        try:
            slope = (ySubTwo - ySubOne) / (xSubTwo - xSubOne)
            return slope
        except:
            print('\nThe Slope is undefined\n')
            return None

    def distanceBetweenTwoPoints(self):
        if len(self.__listOfPoints) < 2:
            print('\nCannot execute because number of points is Insufficient\n')
            return

        self.displayAllPoints()
        print('\nDISTANCE BETWEEN TWO POINTS\n')
        inputs = self.service.askUserForPoints(2, self.getNumberOfPoints())
        points = self.service.convertInputToPoints(inputs, self)
        coordinates = self.service.getXandYCoordinatesOfPoints(points)
        distance = self.service.solveDistanceBetweenTwoPoints(coordinates) 
        print(f'\nThe distance is {distance}\n')
        return distance

    def __pointsAreColinear(self, coordinates):
        firstX, firstY, secondX, secondY, thirdX, thirdY = coordinates.values()

        firstSecondSlope = self.__getSlope(firstY, secondY, firstX, secondX)
        secondThirdSlope = self.__getSlope(secondY, thirdY, secondX, thirdX)
        firstThirdSlope = self.__getSlope(firstY, thirdY, firstX, thirdX)

        return firstSecondSlope == secondThirdSlope and secondThirdSlope == firstThirdSlope 

    def determineIfPointsAreColinearOrCoplanar(self):
        if (len(self.__listOfPoints) < 3):
            print('\nCannot execute because number of points is Insufficient\n')
            return

        self.displayAllPoints()
        print('\nDETERMINE IF 3 POINTS ARE COLINEAR OR COPLANAR\n')
        inputs = self.service.askUserForPoints(3, self.getNumberOfPoints())
        points = self.service.convertInputToPoints(inputs, self)
        coordinates = self.service.getXandYCoordinatesOfPoints(points)

        if (self.__pointsAreColinear(coordinates)):
            return self.service.colinearCallback(points)

        self.service.coplanarCallback(coordinates)


cartesian = CartesianPlane(CartesianPlaneService())
cartesian.exec()
