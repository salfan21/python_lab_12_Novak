#1
import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.x = x
        self.y = y

class Triangle:
    def __init__(self, point1, point2, point3):
        self.points = [point1, point2, point3]

    def calculate_distance(self, point1, point2):
        return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

    def perimeter(self):
        side1 = self.calculate_distance(self.points[0], self.points[1])
        side2 = self.calculate_distance(self.points[1], self.points[2])
        side3 = self.calculate_distance(self.points[2], self.points[0])
        return side1 + side2 + side3

# Приклад використання:
point1 = Point(0, 0)
point2 = Point(1, 0)
point3 = Point(0, 1)

triangle = Triangle(point1, point2, point3)
print(triangle.perimeter())

#2
import math

class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.items = []

    def isempty(self):
        return len(self.items) == 0

    def put(self, item):
        self.items.append(item)

    def get(self):
        if not self.isempty():
            return self.items.pop(0)
        else:
            raise QueueError("Queue is empty")

class SuperQueue(Queue):
    def isempty(self):
        return super().isempty()

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.points = [vertice1, vertice2, vertice3]

    def calculate_distance(self, point1, point2):
        return math.sqrt((point1.get_x() - point2.get_x())**2 + (point1.get_y() - point2.get_y())**2)

    def perimeter(self):
        side1 = self.calculate_distance(self.points[0], self.points[1])
        side2 = self.calculate_distance(self.points[1], self.points[2])
        side3 = self.calculate_distance(self.points[2], self.points[0])
        return side1 + side2 + side3

# Приклад використання:
que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue empty")

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())