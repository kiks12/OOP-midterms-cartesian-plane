
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
        xCoordinate = int(input('Enter x coordinate of point: '))
        yCoordinate = int(input('Enter y coordinate of point: '))
        return (xCoordinate, yCoordinate)


    def __getPointName(self):
        name = str(input("Enter the name of point: "))
        if len(name) > 1: 
            print("\nMake sure you are using a one letter name (a, A, b, B)\n")
        if name in self.__INVALID_POINT_NAMES:
            print("\nInvalid Input! cannot set symbols as a name of point!\n")

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
        print()
    

    def __getPointFromIndex(self, index: int):
        if index > len(self.__listOfPoints) - 1:
            print('\nIndex out of Range\n')
            return None

        return self.__listOfPoints[index]
    

    def __getPointFromName(self, name: str):
        for point in self.__listOfPoints:
            if point.name == name:
                return point
        return None


    def getPoint(self, _input):
        if _input in self.__VALID_POINT_NAMES:
            return self.__getPointFromName(_input)
        return self.__getPointFromIndex(int(_input))


    def getNumberOfPoints(self):
        return len(self.__listOfPoints)


    # this is the private utility function handling the user input collection
    # based on the given numberOfPoints parameter, the function will ask the same number of points 
    # as an input. i.e. numberOfPoints=3, input 1, input 2, and input 3 
    # this will return the inputs
    def __askUserForPoints(self, numberOfPoints: int):
        inputs = [None] * numberOfPoints 

        print("Make sure to be consistent, if you used name for the first point, then use name for the second point.\n")
        for i in range(numberOfPoints):
            while True:
                point = input(f"Enter {self.__INDEX_TO_WORD_CONVERSION.get(i)} point to use: (name or index): ")

                if point in self.__VALID_POINT_NAMES and len(point) > 1:
                    print('\nERROR\n')
                    continue
                
                break
            inputs[i] = point

        return inputs 


    # a reusable private utility function which converts the user inputs to its corresponding point
    # i.e. inputs [a, b] from point a, point b point c choices
    # the return value would be an array of all points corresponding to the inputs of the user
    # ---- NOTE: it is possible to use name or index as an input i.e. [a,b,C,D] for name or [0, 4, 2] for index ----
    def __convertInputToPoints(self, inputs):
        return [self.getPoint(val) for val in inputs]


    # this is a reusable private utility function, used for getting coordinates of all points
    # in an array/list. i.e. [PointA, PointB],
    # return value is a dictionary of all coordinates {'firstX': 0, 'firstY': 1, ...}
    def __getXandYCoordinatesOfPoints(self, arr):
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
    def __solveDistanceBetweenTwoPoints(self, coordinates):
        xComponent = (coordinates.get('secondX') - coordinates.get('firstX')) ** 2
        yComponent = (coordinates.get('secondY') - coordinates.get('firstY')) ** 2
        return (xComponent + yComponent) ** 0.5

                
    # This method is the main function handling the distanceBetweenTwoPoints feature of the class
    # calls all private utility functions inside
    def distanceBetweenTwoPoints(self):
        if len(self.__listOfPoints) < 2:
            print('\nCannot execute because number of points is Insufficient\n')
            return

        self.displayAllPoints()
        inputs = self.__askUserForPoints(2)
        points = self.__convertInputToPoints(inputs)
        coordinates = self.__getXandYCoordinatesOfPoints(points)
        distance = self.__solveDistanceBetweenTwoPoints(coordinates) 
        print(f'\nThe distance is {distance}\n')

        # Possible to return, not necessary now
        #return distance


cart = CartesianPlane()
cart.addMultiplePoints()
cart.distanceBetweenTwoPoints()

