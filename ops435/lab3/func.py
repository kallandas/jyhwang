#!/usr/bin/env python3


def get_circle_area(radius):
    "returns area of a cricle"
    PI = 3.1415
    area = PI * radius ** 2
    # print("the area of this was " + str(area))  Function test purpose line.
    return area

radius = 28.5
area = 0.0
area = get_circle_area(radius)
print("The area of a circle with " + str(radius) + " as radius is " + str(area) + ".")
