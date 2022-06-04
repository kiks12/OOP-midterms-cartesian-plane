
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
            print('\nCARTESIAN PLANE PROGRAM1\n')
            print('\nInstructions\n')
            print('[1] Add a single Point')
            print('[2] Add Multiple Points')
            print('[3] Number of Points')
            print('[4] Display Points')
            print('[5] Check Distance between two points')
            print('[6] Check if 3 points are Colinear or Coplanar')
            print('[0] exit\n')

            option = int(input("Enter your option: "))

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
        print("\nAdd Point\n")
        xCoordinate, yCoordinate = self.service.askUserForXandYCoordinates()
        name = self.service.askUserForPointName()
        _index = len(self.__listOfPoints)

        self.__listOfPoints.append(Point(xCoordinate, yCoordinate, name, _index))
        print(f"\nPoint {name}: (x: {xCoordinate}, y: {yCoordinate}) added in the Cartesian Plane\n")

    
    def addMultiplePoints(self):
        numberOfPoints = int(input("Enter number of points to add: "))

        if numberOfPoints <= 1:
            print("\nCannot add only 1 point, if you want to add only one point use Add Point method\n")
            return 

        for _ in range(numberOfPoints):
            self.addPoint()

    
    def displayAllPoints(self):
        if len(self.__listOfPoints) == 0:
            print('\nNo Points in the Cartesian Plane\n')
            return 

        print('\nDisplaying Points...\n')
        for point in self.__listOfPoints:
            print(point)
        print('\n')
    

    def getPoint(self, _input):
        if _input in self.service.VALID_POINT_NAMES:
            return self.service.getPointFromName(_input, self.__listOfPoints)
        return self.service.getPointFromIndex(int(_input), self.__listOfPoints)


    def getNumberOfPoints(self):
        return len(self.__listOfPoints)


    def __getSlope(self, ySubOne, ySubTwo, xSubOne, xSubTwo):
        slope = (ySubTwo - ySubOne) / (xSubTwo - xSubOne)
        return slope

                
    def distanceBetweenTwoPoints(self):
        if len(self.__listOfPoints) < 2:
            print('\nCannot execute because number of points is Insufficient\n')
            return

        self.displayAllPoints()
        inputs = self.service.askUserForPoints(2, self.getNumberOfPoints())
        points = self.service.convertInputToPoints(inputs, self)
        coordinates = self.service.getXandYCoordinatesOfPoints(points)
        distance = self.service.solveDistanceBetweenTwoPoints(coordinates) 
        print(f'\nThe distance is {distance}\n')
        return distance


    def __pointsAreColinear(self, coordinates):
        firstX = coordinates.get('firstX')
        firstY = coordinates.get('firstY')
        secondX = coordinates.get('secondX')
        secondY = coordinates.get('secondY')
        thirdX = coordinates.get('thirdX')
        thirdY = coordinates.get('thirdY')

        firstSecondSlope = self.__getSlope(firstY, secondY, firstX, secondX)
        secondThirdSlope = self.__getSlope(secondY, thirdY, secondX, thirdX)
        firstThirdSlope = self.__getSlope(firstY, thirdY, firstX, thirdX)

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


    def __colinearCallback(self, points, coordinates):
        print("\nThe 3 points are Colinear\n")
        minPoint, maxPoint = self.__getLineEndpoints(points)
        #print(f"min: {minPoint}, max: {maxPoint}")
        coordinates = self.service.getXandYCoordinatesOfPoints([minPoint, maxPoint])
        distance = self.service.solveDistanceBetweenTwoPoints(coordinates)
        print(f"The distance of endpoints is {distance}")


    def determineIfPointsAreColinearOrCoplanar(self):
        if (len(self.__listOfPoints) < 3):
            print('\nCannot execute because number of points is Insufficient\n')
            return

        self.displayAllPoints()
        inputs = self.service.askUserForPoints(3, self.getNumberOfPoints())
        points = self.service.convertInputToPoints(inputs, self)
        coordinates = self.service.getXandYCoordinatesOfPoints(points)

        if (self.__pointsAreColinear(coordinates)):
            return self.__colinearCallback(points, coordinates)

        self.service.coplanarCallback(coordinates)


cartesian = CartesianPlane(CartesianPlaneService())
cartesian.exec()

