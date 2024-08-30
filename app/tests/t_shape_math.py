# tests/t_shape_math.py

import shape_math

def test_squaring_number():
    assert shape_math.square(5) == 25
    assert shape_math.square(-3) == 9

def test_area_of_square():
    assert shape_math.area_of_square(5) == 25
    assert shape_math.area_of_square(6) == 36
    assert shape_math.area_of_square(7) == 49

def test_perimeter_of_square():
    assert shape_math.perimeter_of_square(5) == 20
    assert shape_math.perimeter_of_square(6) == 24

def test_area_of_rectangle():
    assert shape_math.area_of_rectangle(5, 3) == 15
    assert shape_math.area_of_rectangle(7, 2) == 14

def test_perimeter_of_rectangle():
    assert shape_math.perimeter_of_rectangle(5, 3) == 16
    assert shape_math.perimeter_of_rectangle(7, 2) == 18

def test_area_of_circle():
    assert shape_math.area_of_circle(3) == 28.26
    assert shape_math.area_of_circle(5) == 78.5

def test_circumference_of_circle():
    assert shape_math.circumference_of_circle(3) == 18.84
    assert shape_math.circumference_of_circle(5) == 31.400000000000002

def test_area_of_trapezoid():
    assert shape_math.area_of_trapezoid(3, 5, 4) == 16
    assert shape_math.area_of_trapezoid(7, 10, 5) == 42.5

def test_surface_area_of_cylinder():
    assert round(shape_math.surface_area_of_cylinder(3, 5), 2) == 150.72
    assert round(shape_math.surface_area_of_cylinder(4, 6), 2) == 251.2

def test_surface_area_of_sphere():
    assert shape_math.surface_area_of_sphere(3) == 113.04
    assert shape_math.surface_area_of_sphere(5) == 314.0

def test_surface_area_of_cube():
    assert shape_math.surface_area_of_cube(3) == 54
    assert shape_math.surface_area_of_cube(4) == 96

def test_surface_area_of_cone():
    assert round(shape_math.surface_area_of_cone(3, 5), 2) == 75.36
    assert round(shape_math.surface_area_of_cone(4, 6), 2) == 125.6
