#! python3

from random import randint
import turtle


class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def falls_in_rectangle(self, rectangle):
        if rectangle.point1.x < self.x < rectangle.point2.x \
        and rectangle.point1.y < self.y < rectangle.point2.y:
            return True
        else:
            return False
        
class Rectangle:
    
    def __init__(self, point1, point2):
        self.point1 = point1
        self.point2 = point2
        
    def area(self):
        return (self.point2.x - self.point1.x) * \
                (self.point2.y - self.point1.y)
                
class TurtleRectangle(Rectangle):
    
    def draw(self, canvas):
        length = self.point2.x - self.point1.x
        height = self.point2.y - self.point1.y
        # Go to specific coordinates
        canvas.penup()
        canvas.goto(self.point1.x *10, self.point1.y *10)

        canvas.pendown()
        canvas.forward(length * 10)
        canvas.left(90)
        canvas.forward(height * 10)
        canvas.left(90)
        canvas.forward(length * 10)
        canvas.left(90)
        canvas.forward(height * 10)

class TurtlePoint(Point):
    
    def draw(self, canvas, size=7, color="red"):
        canvas.penup()
        canvas.goto(self.x * 10, self.y * 10)
        canvas.down()
        canvas.dot(size,color)


# Create a rectangle object                
rectangle = TurtleRectangle(Point(randint(0,9), randint(0,9)), Point(randint(10,19), randint(10,19)))

# Print rectangle coordinates
print(f"Rectangle Coordinates: {rectangle.point1.x},{rectangle.point1.y}",
      f"and {rectangle.point2.x},{rectangle.point2.y}")

# Get point and area guesses from user
user_point = TurtlePoint(float(input("Guess X: ")), float(input("Guess Y: ")))
user_area = float(input("Guess rectangle area: "))

# Print game results
print(f"Your point was inside the rectangle: {user_point.falls_in_rectangle(rectangle)}")
print(f"Your area was off by: {rectangle.area() - user_area}")

myturtle = turtle.Turtle()
rectangle.draw(canvas=myturtle)
user_point.draw(canvas=myturtle)
turtle.done()