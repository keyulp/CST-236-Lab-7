"""
This contains the definitions for functions called in main
"""
from math import factorial
import math
from decimal import Decimal, getcontext
import string

# pylint: disable= invalid-name
# Because I should be able to name my variables however i want to


def fibonacci_sequence(number):
    """This contains functionality to calculate fibonacci sequence"""
    previous_number = 0
    if number > 0:
        num = 1
        count = 1
        while count < number:
            temp = num
            num = previous_number + temp
            previous_number = temp
            count += 1

    return previous_number


def pi_func(number):
    """This contains functionality to calculate pi"""
    number = int(number)
    getcontext().prec = number+1
    pi = Decimal(0)
    for variable1 in range(number):
        variable2 = ((-1)**variable1)*(factorial(6*variable1))*(13591409+545140134*variable1)
        denominator = factorial(3*variable1)*(factorial(variable1)**3)*(640320**(3*variable1))
        pi += Decimal(variable2)/Decimal(denominator)
    pi = pi * Decimal(12)/Decimal(640320 ** 1.5)
    pi = 1/pi
    pistring = str(pi)
    return pistring[number]

list_for_conversions = {"nano": 1000000000, "micro": 1000000, "milli": 1000, "centi": 100,
                        "deci": 10, "": 1, "deca": .1, "hecto": .01, "kilo": .001,
                        "mega": .000001, "giga": .000000001}


def convert_check(value, base, output):
    """This contains functionality to convert numbers with units"""
    if (base not in list_for_conversions) or (output not in list_for_conversions):
        return "I don't know how to convert that."
    converted_value = (value / list_for_conversions[base]) * list_for_conversions[output]
    if Decimal(converted_value) == Decimal(1.0):
        return "1 " + output + "meter"
    return str(float(converted_value)) + " " + output + "meters"


def convert(value, base, output):
    """This contains functionality to convert numbers with units"""
    if("meter" not in base) or ("meter" not in output):
        return "I don't know how to convert that"
    base = base.replace("meters", "")
    base = base.replace("meter", "")
    output = output.replace("meters", "")
    output = output.replace("meter", "")
    return convert_check(value, base, output)

Vehicles = dict(Bike="A vehicle with two wheels in tandem, "
                     "usually propelled by pedals connected to the rear wheel by"
                     " a chain, and having handlebars for steering and a "
                     "saddlelike seat.",
                Car="A passenger vehicle designed for operation"
                    " on ordinary roads and typically having four wheels"
                    " and a gasoline or diesel internal-combustion engine.",
                Train="A self-propelled, connected group of rolling stock.",
                Boat="A vessel for transport by water, constructed to "
                     "provide buoyancy by excluding water and shaped"
                     " to give stability and permit propulsion.",
                Bus="A large motor vehicle, having a long body, "
                    "equipped with seats or benches for passengers"
                    ", usually operating as part of a scheduled service",
                Motorcycle="A motor vehicle similar to a bicycle but "
                           "usually larger and heavier, chiefly for "
                           "one rider but sometimes having two saddles"
                           " or an attached sidecar for passengers",
                Truck="Any of various forms of vehicle for carrying goods"
                      " and materials, usually consisting of a single"
                      " self-propelled unit but also often composed"
                      " of a trailer vehicle hauled by a tractor unit",
                SUV="A rugged vehicle with a trucklike chassis and"
                    " four-wheel drive, designed for occasional off-road use.",
                Jeep="A small, rugged military motor vehicle having"
                     " four-wheel drive and a quarter-ton capacity:"
                     " widely used by the U.S. Army during and"
                     " after World War II.")


def check_dictionary(word):
    """This contains functionality to check dictionary"""
    if word not in Vehicles:
        return "I don't know the definition for that"
    return Vehicles[word]


list2 = {3: "Triangle", 4: "Quadrilateral", 5: "Pentagon", 6: "Hexagon",
         7: "Heptagon", 8: "Octagon", 9: "Nonagon", 10: "Decagon"}


def shape_checker_2(number):
    """This contains functionality to calculate shape"""
    if 3 <= number <= 10:
        return list2[number]

    else:
        return "I don't know"


def alphabet_checker(letter):
    """This contains functionality to check the alphabet"""
    if 1 <= letter <= 26:
        letter = int(letter)
        letter = (letter-1)
        is_upper = True
        return string.letters[letter+is_upper*26]

    if letter < 1 or letter > 26:
        return "Does not exist"

Polynomial_Degrees = {0: "Constant", 1: "Linear", 2: "Quadratic",
                      3: "Cubic", 4: "Quartic", 5: "Quintic"}


def polynomial_checker(number):
    """This contains functionality to check a polynomial"""
    return Polynomial_Degrees[number]


def sin_calculator(number):
    """This contains functionality to perform sine"""
    return math.sin(number)

