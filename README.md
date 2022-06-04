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

### addPoint()
Used for adding a single point in the cartesian plane

### addMultiplePoints()
Used to add multiple points in the cartesian plane. Asks the user how many points to add. Input Error on 1 - send an error message if the user inputs 1 as the number of points to add.

### displayAllPoints()
will print all points in the cartesian plane (listOfPoints)

### getPoint(input :str/int)
will return the point using the input from the user

### getNumberOfPoints()
this will return the length of listOfPoints

### distanceBetweenTwoPoints()
determine the distance between two points
    - should send an error message if the points are insufficient
    - should also send an error message if the points are not in the listOfIndex
    - show the points to users
    - then ask the users which point to use
    - calculate the distance between two points
    
<br>
<br>

## CartesianPlaneService
(Utility functions are used inside methods. Reusable codes). This class will be injected to CartesianPlane as the service of that class. 
This essentially handles all the background logic of CartesianPlane. (Dependency Injection)

### askUserForXandYCoordinates()
This will only ask the user for x and y coordinates for a point.

### askUserForPointName()
This will ask the user for a point name.


### getPointFromIndex(index: int, listOfPoints: Point[])
This will return the point in the given index from listOfPoints


### getPointFromName(name: str, listOfPoints: Point[])
This will return the point in which the name of the point is equal to the argument


### askUserForPoints(numberOfPointsToAsk: int, numberOfPoints: int)
This function will ask the user which points to be used depending on the given numberOfPoints. If numberOfPoints is 3 then this function will only ask for 3 inputs. This will return the inputs of the user in an array/list. i.e. [a, b] for name or [0, 3] for index

```python
# GIVEN THAT SELF is CARTESIAN PLANE

## NOTE: ALL OF THESE ARE EXAMPLES OF CODES INSIDE CARTESIAN PLANE CLASS METHODS ##

# if you want to ask users which points to use for, example, solving the distance
# between two points use this function

# for unpacking/deconstructuring
firstInput, secondInput = self.service.askUserForPoints(2, self.getNumberOfPoints)

# for whole array
inputs = self.service.askUserForPoints(2, self.getNumberOfPoints)

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
This function will use the inputs from __askUserForInputs and return its corresponding Point on the cartesian plane.

```python
# when you have inputs from users about which points to use, you can convert
# their inputs to Point using this function

inputs = self.service.askUserForPoints(2, self.getNumberOfPoints)
points = self.service.convertInputToPoints(inputs, self)

# inputs = [a, b]
# OUTPUT: [Point a, Point b]
```


### getXandYCoordinatesOfPoints(points: Point[])
This function will use the points returned by __convertInputToPoints and get all x and y coordinates of each point. i.e. {’firstX’: 0, ‘firstY’: 1}

```python
# Now that you have the corresponding points of the user inputs, you can get 
# the x and y coordinates of each Point with this utility function.

inputs = self.service.askUserForPoints(2, self.getNumberOfPoints)
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
	inputs = self.service.askUserForPoints(2, self.getNumberOfPoints)
	points = self.service.convertInputToPoints(inputs, self)
	coordinates = self.service.getXandYCoordinatesOfPoints(points)
	# use utility function to get the distance between two points 
	# pass in coordinates as an argument
	distance = self.service.solveDistanceBetweenTwoPoints(coordinates)
	print(f'\nThe distance is {distance}\n')

	#Possible to return, not necessary now
	#return distance
```
