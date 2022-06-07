

class CartesianPlaneService:


    VALID_POINT_NAMES = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
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
        pass

    def askUserForXandYCoordinates(self):
        while True:
            try:
                xCoordinate = int(input('Enter x coordinate of point: '))
                yCoordinate = int(input('Enter y coordinate of point: '))
                return [xCoordinate, yCoordinate]
            except ValueError:
                print('\nError: input only integer\n')
                continue

    def askUserForPointName(self):
        while True:
            try:
                name = str(input("Enter the name of point: "))
                if len(name) > 1: 
                    print("\nMake sure you are using a one letter name (a, A, b, B)\n")
                    continue

                if name not in self.VALID_POINT_NAMES:
                    print("\nInvalid Input! cannot set symbols as a name of point!\n")
                    continue

                return name
            except ValueError:
                print('\nError: input only 1 character\n')
                continue

    def getPointFromIndex(self, index: int, listOfPoints):
        if index > len(listOfPoints) - 1:
            print('\nIndex out of Range\n')
            return None

        return listOfPoints[index]

    def getPointFromName(self, name: str, listOfPoints):
        for point in listOfPoints:
            if point.name == name:
                return point
        return None

    # this is the private utility function handling the user input collection
    # based on the given numberOfPoints parameter, the function will ask the same number of points 
    # as an input. i.e. numberOfPoints=3, input 1, input 2, and input 3 
    # this will return the inputs
    def askUserForPoints(self, numberOfPointsToAsk: int, numberOfPoints: int):
        inputs = [None] * numberOfPointsToAsk
        print("Be consistent, if you used name for the first point, then use name for the rest of the points.\n")
        for i in range(numberOfPointsToAsk):
            while True:
                inputPoint = input(f"Enter {self.__INDEX_TO_WORD_CONVERSION.get(i)} point to use: (name or index): ")

                if inputPoint not in self.VALID_POINT_NAMES and len(inputPoint) > 1:
                    print('\nError: Invalid name\n')
                    continue
    
                try:
                     if int(inputPoint) > numberOfPoints - 1:
                        print('\nError: index out of range\n')
                        continue
                except ValueError:
                    # do nothing then break
                    pass

                break

            inputs[i] = inputPoint

        return inputs 

    # a reusable private utility function which converts the user inputs to its corresponding point
    # i.e. inputs [a, b] from point a, point b point c choices
    # the return value would be an array of all points corresponding to the inputs of the user
    # ---- NOTE: it is possible to use name or index as an input i.e. [a,b,C,D] for name or [0, 4, 2] for index ----
    def convertInputToPoints(self, inputs, cartesianPlane):
        return [cartesianPlane.getPoint(val) for val in inputs]

    # this is a reusable private utility function, used for getting coordinates of all points
    # in an array/list. i.e. [PointA, PointB],
    # return value is a dictionary of all coordinates {'firstX': 0, 'firstY': 1, ...}
    def getXandYCoordinatesOfPoints(self, arr):
        coordinates = {}
        for idx, val in enumerate(arr):
            x, y = val.getCoordinates()
            coordinates[F"{self.__INDEX_TO_WORD_CONVERSION.get(idx)}X"] = x
            coordinates[F"{self.__INDEX_TO_WORD_CONVERSION.get(idx)}Y"] = y

        return coordinates

    # solution for distance between two points 
    # d = sqrt((x2-x1)^2 + (y2-y1)^2)
    # this is a private utility function for the distanceBetweenTwoPoints method
    # returns the distance between two points 
    def solveDistanceBetweenTwoPoints(self, coordinates):
        firstX, firstY, secondX, secondY = coordinates.values()
        xComponent = (secondX - firstX) ** 2
        yComponent = (secondY - firstY) ** 2
        return (xComponent + yComponent) ** 0.5

    def colinearCallback(self, points):
        print("\nThe 3 points are Colinear\n")
        #minPoint, maxPoint = self.__getLineEndpoints(points)
        pointsFirstSecond = points[:2]
        pointsSecondThird = points[1:]
        pointsFirstThird = [point for idx, point in enumerate(points) if idx == 0 or idx == 2]
        coordinatesFirstSecond = self.getXandYCoordinatesOfPoints(pointsFirstSecond)
        coordinatesSecondThird = self.getXandYCoordinatesOfPoints(pointsSecondThird)
        coordinatesFirstThird = self.getXandYCoordinatesOfPoints(pointsFirstThird)
        distanceFirstSecond = self.solveDistanceBetweenTwoPoints(coordinatesFirstSecond)
        distanceSecondThird = self.solveDistanceBetweenTwoPoints(coordinatesSecondThird)
        distanceFirstThird = self.solveDistanceBetweenTwoPoints(coordinatesFirstThird)
        print(f"The distance of endpoints is {max([distanceFirstSecond, distanceSecondThird, distanceFirstThird])}")

    # A = 1/2 * abs(x1(y2-y3) + x2(y3-y1) + x3(y1-y2))
    def __solveAreaOfTriangle(self, coordinates):
        firstX, firstY, secondX, secondY, thirdX, thirdY = coordinates.values()

        firstSolution = firstX*(secondY-thirdY) + secondX*(thirdY-firstY) + thirdX*(firstY-secondY)
        try:
            areaOfTriangle = abs(firstSolution) / 2
            print(f"\nThe area of the triangle is {areaOfTriangle}\n")
        except ZeroDivisionError:
            print("\nDivision by Zero, answer is undefined\n")
            return None

    def coplanarCallback(self, coordinates):
        print("\nThe 3 points are Coplanar\n")
        self.__solveAreaOfTriangle(coordinates)


