# Cartesian Plane Program Documentation

Classes:

- Point
- Cartesian Plane
- Cartesian Plane Service

<br>
<br>

## Point

Properties:

- x - this is the coordinate x of the point
    - should have a setter and getter
- y - this is the coordinate y of the point
    - should have a setter and getter

Methods: 

- getCoordinates - will return the x and y coordinates of the point in an array i.e. [0,1]

<br>
<br>

## **CartesianPlane**

Properties:

- listOfPoints - this is an array of all points inside the cartesian plane
    - should have a setter and getter

Methods: 

### exec()
This method will run the main loop of the Program

### addPoint()
Used for adding a single point in the cartesian plane

### addMultiplePoints()
Used to add multiple points in the cartesian plane. Asks the user how many points to add. Input Error on 1 - send an error message if the user inputs 1 as the number of points to add.

### displayAllPoints()
Will print all points in the cartesian plane (listOfPoints)

### getPoint(input :str/int)
Will return the point using the input from the user

### getNumberOfPoints()
This will return the length of listOfPoints

### distanceBetweenTwoPoints()
Determine the distance between two points
    - should send an error message if the points are insufficient
    - should also send an error message if the points are not in the listOfIndex
    - show the points to users
    - then ask the users which point to use
    - calculate the distance between two points
    
### threePointsAreColinearOrCoplanar()
This will ask the user to input which 3 points from listOfPoints and determine if those points are colinear or coplanar.

<br>

If the 3 points are colinear, the method will invoke the service method colinearCallback(), otherwise, coplanarCallback().
    
<br>
<br>

## CartesianPlaneService
(Utility functions are used inside methods. Reusable codes). This class will be injected to CartesianPlane as the service of that class. 
This essentially handles all the background logic of CartesianPlane. (Dependency Injection)

Properties: 

### __VALID_POINT_NAMES
Private Property containing all valid Point Names

### __INDEX_TO_WORD_CONVERSION 
Private Property used for the conversion of Indices to Words

<br>

Methods:

### askUserForXandYCoordinates()
This will ask the user for x and y coordinates for a point.

### askUserForPointName()
This will ask the user for a point name.


### getPointFromIndex(index: int, listOfPoints: Point[])
This will return the point in the given index from listOfPoints


### getPointFromName(name: str, listOfPoints: Point[])
This will return the point in which the name of the point is equal to the argument


### askUserForPoints(numberOfPointsToAsk: int, numberOfPoints: int)
This method will ask the user which points to be used depending on the given numberOfPoints. If numberOfPoints is 3 then this function will only ask for 3 inputs. This will return the inputs of the user in an array/list. i.e. [a, b] for name or [0, 3] for index

```python
# GIVEN THAT SELF is CARTESIAN PLANE

## NOTE: ALL OF THESE ARE EXAMPLES OF CODES INSIDE CARTESIAN PLANE CLASS METHODS ##

# if you want to ask users which points to use for, example, solving the distance
# between two points use this function

# for unpacking/deconstructuring
firstInput, secondInput = self.service.askUserForPoints(2, self.getNumberOfPoints())

# for whole array
inputs = self.service.askUserForPoints(2, self.getNumberOfPoints())

# Point a: (x: 1, y: 2, index: 0)
# Point b: (x: 2, y: 3, index: 1)

# Enter first point to use: (name or index)
# a
# Enter second point to use: (name of index)
# b

# OUTPUT: [a, b]

# destructured values:
# firstInput = a
# secondInput = b
```


### convertInputToPoints(inputs: any[], cartesianPlane: CartesianPlane)
This method will use the inputs from __askUserForInputs and return its corresponding Point on the cartesian plane.

```python
# when you have inputs from users about which points to use, you can convert
# their inputs to Point using this function

inputs = self.service.askUserForPoints(2, self.getNumberOfPoints())
points = self.service.convertInputToPoints(inputs, self)

# inputs = [a, b]
# OUTPUT: [Point a, Point b]
```


### getXandYCoordinatesOfPoints(points: Point[])
This method will use the points returned by __convertInputToPoints and get all x and y coordinates of each point. i.e. {’firstX’: 0, ‘firstY’: 1}

```python
# Now that you have the corresponding points of the user inputs, you can get 
# the x and y coordinates of each Point with this utility function.

inputs = self.service.askUserForPoints(2, self.getNumberOfPoints())
points = self.service.convertInputToPoints(inputs, self)
coordinates = self.service.getXandYCoordinatesOfPoints(points)

# inputs = [a, b]
# points = [Point a, Point b]

# OUTPUT:
# coordinates = {
# 'firstX': 1,
# 'firstY': 2,
# 'secondX': 2,
# 'secondY': 3,
# }
# wherein firstX is the value of x coordinate of Point a and firstY is the value
# of y coordinate of Point a. So on and so forth.
```


### solveDistanceBetweenTwoPoints(coordinates: dictionary)
Using the formula sqrt((x2-x1)^2 + (y2-y1)^2), this will solve the distance between two points wherein their x and y coordinates are inside the coordinates dictionary (parameter).

```python
def distanceBetweenTwoPoints(self):
	if len(self.__listOfPoints) < 2:
			print('\nCannot execute because number of points is Insufficient\n')
		  return
	
	self.displayAllPoints()
	inputs = self.service.askUserForPoints(2, self.getNumberOfPoints())
	points = self.service.convertInputToPoints(inputs, self)
	coordinates = self.service.getXandYCoordinatesOfPoints(points)
	# use utility function to get the distance between two points 
	# pass in coordinates as an argument
	distance = self.service.solveDistanceBetweenTwoPoints(coordinates)
	print(f'\nThe distance is {distance}\n')

	#Possible to return, not necessary now
	#return distance
```


### __solveSlopeBetweenTwoPoints(ySubOne, ySubTwo, xSubOne, xSubTwo)
Using the formula y2-y1/x2-x1 this method will calculate the slope of two points using the given parameters; x2, x1, y2, and y1.


### isColinear(coordinates: dictionary, plane: CartesianPlane)
This method is used in determining whether 3 points are colinear or not.


### colinearCallback(points: Point[])
This will be invoked inside determineIfPointsAreColinearOrCoplanar method of CartesianPlane as this will find the distance of endpoints if 3 points are colinear.


### __solveAreaOfTriangle(coordinates: dictionary)
With this formula - 1/2 * abs(x1(y2-y3) + x2(y3-y1) + x3(y1-y2)), this private service function will calculate the area of a triangle. This method will be invoked inside coplanarCallback().


### coplanarCallback(coordinates: dictionary)
This is the callback function that will be invoked in determineIfPointsAreColinearOrCoplanar method of CartesianPlane when the 3 points are coplanar. This will then proceed to calculate the area of the triangle.

