import math
class circle:
    def __init__(circle, rad):
        circle.rad = rad

    def area(circle):
        cal_circle = math.pi * circle.rad ** 2
        print()
        print("Area =", cal_circle)

    def perimeter(circle):
        cal_circle = 2 * math.pi * circle.rad
        print("Perimeter =", cal_circle)


num_rad = float(input("Enter the value of radius: "))

circle = circle(num_rad)

circle.area()
circle.perimeter()