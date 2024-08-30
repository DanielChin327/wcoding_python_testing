# shape_math.py

def square(x):
    return x * x

def area_of_square(num):
    return square(num)

def perimeter_of_square(num):
    return 4 * num

def area_of_rectangle(length, width):
    return length * width

def perimeter_of_rectangle(length, width):
    return 2 * (length + width)

def area_of_circle(radius):
    # Using pi = 3.14 approximation
    pi = 3.14
    return pi * square(radius)

def circumference_of_circle(radius):
    # Using pi = 3.14 approximation
    pi = 3.14
    return 2 * pi * radius

def area_of_trapezoid(base1, base2, height):
    # Formula: ((base1 + base2) / 2) * height
    return ((base1 + base2) / 2) * height

def surface_area_of_cylinder(radius, height):
    # Using pi = 3.14 approximation
    pi = 3.14
    return 2 * pi * radius * (radius + height)

def surface_area_of_sphere(radius):
    # Using pi = 3.14 approximation
    pi = 3.14
    return 4 * pi * square(radius)

def surface_area_of_cube(side):
    # 6 sides each with area side^2
    return 6 * square(side)

def surface_area_of_cone(radius, slant_height):
    # Using pi = 3.14 approximation
    pi = 3.14
    return pi * radius * (radius + slant_height)
