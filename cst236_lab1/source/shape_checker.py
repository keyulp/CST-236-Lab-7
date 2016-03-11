"""
:mod:`source.source1` -- Example source code
============================================

The following example code determines if a set
of 3 sides of a triangle is equilateral, scalene or isosceles
"""

# pylint: disable= no-member
# I'm ignoring no member because if it's a dictionary, list, or tuple, it will have those members
# pylint: disable= too-many-arguments
# Because the function needs all 8 arguments
# pylint:disable=too-many-return-statements
# Because there is no way to bo through this
# code without the number of statements and branches we have
# pylint:disable= too-many-branches


def get_triangle_type(variable1=0, variable2=0, variable3=0):
    """
    Determine if the given triangle is equilateral, scalene or Isosceles

    :param variable1: line a
    :type variable1: float or int or tuple or list or dict

    :param variable2: line b
    :type variable2: float

    :param variable3: line c
    :type variable3: float

    :return: "equilateral", "isosceles", "scalene" or "invalid"
    :rtype: str
    """
    if isinstance(variable1, (tuple, list)) and len(variable1) == 3:
        variable3 = variable1[2]
        variable2 = variable1[1]
        variable1 = variable1[0]

    if isinstance(variable1, dict) and len(variable1.keys()) == 3:
        values = []
        for value in variable1.values():
            values.append(value)
        variable1 = values[0]
        variable2 = values[1]
        variable3 = values[2]

    if not (isinstance(variable1, (int, float)) and
            isinstance(variable2, (int, float)) and
            isinstance(variable3, (int, float))):
        return "invalid"

    if variable1 <= 0 or variable2 <= 0 or variable3 <= 0:
        return "invalid"

    if variable1 == variable2 and variable2 == variable3:
        return "equilateral"

    if variable1 == variable2 or variable1 == variable3 or variable2 == variable3:
        return "isosceles"
    else:
        return "scalene"


def get_quadrilateral_type_length(variable1=0, variable2=0, variable3=0, variable4=0):
    """
    Determine if the given

    :param variable1: line a
    :type variable1: float

    :param variable2: line b
    :type variable2: float

    :param variable3: line c
    :type variable3: float

    :param variable4: line d
    :type variable4: float

    :return: "square", "rectangle", "rhombus" or "disconnected"
    :rtype: str
    """

    if not (isinstance(variable1, (int, float)) and isinstance(variable2, (int, float))):
        if not (isinstance(variable3, (int, float)) and isinstance(variable4, (int, float))):
            return "invalid"

    if variable1 <= 0 or variable2 <= 0 or variable3 <= 0 or variable4 <= 0:
        return "invalid"

    if variable1 == variable2 and variable2 == variable3 and variable3 == variable4:
        return "square"

    if variable1 == variable3 and variable2 == variable4\
            and variable1 != variable2 and variable3 != variable4:
        return "rectangle"


def get_quadrilateral_type(variable1=0, variable2=0, variable3=0,
                           variable4=0, angle_a=0, angle_b=0, angle_c=0, angle_d=0):
    """
    Determine if the given

    :param variable1: line a
    :type variable1: float

    :param variable2: line b
    :type variable2: float

    :param variable3: line c
    :type variable3: float

    :param variable4: line d
    :type variable4: float

    :param angle_a: line angle_a
    :type angle_a: float

    :param angle_b: line angle_b
    :type angle_b: float

    :param angle_c: line angle_c
    :type angle_c: float

    :param angle_d: line angle_d
    :type angle_d: float

    :return: "square", "rectangle", "rhombus" or "disconnected"
    :rtype: str
    """

    if not (isinstance(variable1, (int, float)) and isinstance(variable2, (int, float))):
        if not (isinstance(variable3, (int, float)) and isinstance(variable4, (int, float))):
            return "invalid"

    if variable1 <= 0 or variable2 <= 0 or variable3 <= 0 or variable4 <= 0:
        return "invalid"

    if angle_a <= 0 or angle_b <= 0 or angle_c <= 0 or angle_d <= 0:
        return "invalid"

    if (((angle_a) + (angle_b)) + (angle_c)) + (angle_d) != 360:
        return "disconnected"

    if variable1 == variable2 and variable2 == variable3 and variable3 == variable4:
        if angle_a == angle_b and angle_b == angle_c and angle_c == angle_d:
            if angle_a == 90:
                return "square"

    if variable3 == variable1 and variable2 == variable4 and\
                    variable1 != variable2 and variable3 != variable4:
        if angle_a == angle_b and angle_b == angle_c and angle_c == angle_d:
            if angle_a == 90:
                return "rectangle"

    if variable1 == variable2 and variable2 == variable3 and variable3 == variable4:
        if angle_a == angle_c and angle_b == angle_d:
            return "rhombus"
