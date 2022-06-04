
class CartesianPlaneService:


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
                if name in self.__INVALID_POINT_NAMES:
                    print("\nInvalid Input! cannot set symbols as a name of point!\n")

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
    def askUserForPoints(self, numberOfPoints: int):
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
        xComponent = (coordinates.get('secondX') - coordinates.get('firstX')) ** 2
        yComponent = (coordinates.get('secondY') - coordinates.get('firstY')) ** 2
        return (xComponent + yComponent) ** 0.5


    # A = 1/2 * abs(x1y2 + x2y3 + x3y1 - x1y3 - x2y1 - x3y2)
    def __solveAreaOfTriangle(self, coordinates):
        firstX = coordinates.get('firstX')
        firstY = coordinates.get('firstY')
        secondX = coordinates.get('secondX')
        secondY = coordinates.get('secondY')
        thirdX = coordinates.get('thirdX')
        thirdY = coordinates.get('thirdY')

        firstSolution = (firstX*secondY) + (secondX*thirdY) + (thirdX*firstY) - (firstX*thirdY) - (secondX*firstY) - (thirdX*secondY)
        return abs(firstSolution) / 2


    def coplanarCallback(self, coordinates):
        print("\nThe 3 points are Coplanar\n")
        area = self.__solveAreaOfTriangle(coordinates)
        print(f"\nThe area of the triangle is {area}\n")







