"""
Test for source.answer
"""
from unittest import TestCase

import getpass
from datetime import datetime
from test.plugins.ReqTracer import job_story
from source.main import Interface


class TestAnswer(TestCase):
    """This tests answers"""

    @job_story('When I ask "What time is it?" I want to be '
               'given the current date/time so I can stay up to date')
    def test_date_time(self, inquiry=Interface()):
        """This tests date and time"""
        result = Interface.ask(inquiry, "What time is it?")
        self.assertEqual(result, 'The current time is :' +
                         datetime.utcnow().strftime("%m-%d-%Y %H:%M"))

    @job_story('When I ask "What is the n digit of fibonacci" I want'
               ' to receive the answer so I don\'t have to figure it out myself')
    def test_fibonacci_sequence(self, inquiry=Interface()):
        """This tests fibonacci sequence"""
        result = inquiry.ask("What is the 8 digit of fibonacci?")
        self.assertEqual(result, 13)

    @job_story('When I ask "What is the n digit of pi" I want to receive the'
               ' answer so I don\'t have to figure it out myself')
    def test_pi_function(self, inquiry=Interface()):
        """This tests pi"""
        result = inquiry.ask("What is the 8 digit of pi?")
        self.assertEqual(result, '6')

    @job_story('When I ask "Please clear memory" I want the application to '
               'clear user set questions and answers so I can reset the application')
    def test_clear_memory(self, inquiry=Interface()):
        """This tests clearing memory"""
        inquiry.ask("What is the acceleration of gravity?")
        inquiry.teach("-9.81 m/s/s")
        inquiry.ask("Please clear memory?")
        result = Interface.ask(inquiry, "What is the acceleration of gravity?")
        self.assertEqual(result, 'I don\'t know, please provide the answer')

    @job_story('When I say "Open the door hal", I want the application to say "I\'m afraid '
               'I can\'t do that <user name> so I know that is not an option')
    def test_user_name(self, inquiry=Interface()):
        """This tests opening a door"""
        result = inquiry.ask("Open the door hal?")
        self.assertEqual(result, "I'm afraid I can't do that " + getpass.getuser())

    @job_story('When I ask "Convert <number> <units> to <units>" I want'
               ' to receive the converted value and units so I can know the answer.')
    def test_convert_number_and_unit(self, inquiry=Interface()):
        """This tests converting a number"""
        result = inquiry.ask("Convert 4.2 meters to kilometers")
        self.assertEqual(result, "0.0042 kilometers")

    @job_story('When I ask for a numeric conversion '
               'I want at least 10 different units I can convert from/to')
    def test_convert_numeric_1(self, inquiry=Interface()):
        """This tests converting a number"""
        result = inquiry.ask("Convert 8.3 meters to gigameters")
        self.assertEqual(result, "8.3e-09 gigameters")

    @job_story('When I ask for a numeric conversion '
               'I want at least 10 different units I can convert from/to')
    def test_convert_numeric_2(self, inquiry=Interface()):
        """This tests converting a number"""
        result = inquiry.ask("Convert 8.3 meters to megameters")
        self.assertEqual(result, "8.3e-06 megameters")

    @job_story('When I ask for a numeric conversion '
               'I want at least 10 different units I can convert from/to')
    def test_convert_numeric_3(self, inquiry=Interface()):
        """This tests converting a number"""
        result = inquiry.ask("Convert 8.3 meters to kilometers")
        self.assertEqual(result, "0.0083 kilometers")

    @job_story('When I ask for a numeric conversion '
               'I want at least 10 different units I can convert from/to')
    def test_convert_numeric_4(self, inquiry=Interface()):
        """This tests converting a number"""
        result = inquiry.ask("Convert 8.3 meters to hectometers")
        self.assertEqual(result, "0.083 hectometers")

    @job_story('When I ask for a numeric conversion '
               'I want at least 10 different units I can convert from/to')
    def test_convert_numeric_5(self, inquiry=Interface()):
        """This tests converting a number"""
        result = inquiry.ask("Convert 8.3 meters to decameters")
        self.assertEqual(result, "0.83 decameters")

    @job_story('When I ask for a numeric conversion '
               'I want at least 10 different units I can convert from/to')
    def test_convert_numeric_6(self, inquiry=Interface()):
        """This tests converting a number"""
        result = inquiry.ask("Convert 8.3 meters to decimeters")
        self.assertEqual(result, "83.0 decimeters")

    @job_story('When I ask for a numeric conversion '
               'I want at least 10 different units I can convert from/to')
    def test_convert_numeric_7(self, inquiry=Interface()):
        """This tests converting a number"""
        result = inquiry.ask("Convert 8.3 meters to centimeters")
        self.assertEqual(result, "830.0 centimeters")

    @job_story('When I ask for a numeric conversion '
               'I want at least 10 different units I can convert from/to')
    def test_convert_numeric_8(self, inquiry=Interface()):
        """This tests converting a number"""
        result = inquiry.ask("Convert 8.3 meters to millimeters")
        self.assertEqual(result, "8300.0 millimeters")

    @job_story('When I ask for a numeric conversion '
               'I want at least 10 different units I can convert from/to')
    def test_convert_numeric_9(self, inquiry=Interface()):
        """This tests converting a number"""
        result = inquiry.ask("Convert 8.3 meters to micrometers")
        self.assertEqual(result, "8300000.0 micrometers")

    @job_story('When I ask for a numeric conversion '
               'I want at least 10 different units I can convert from/to')
    def test_convert_numeric_10(self, inquiry=Interface()):
        """This tests converting a number"""
        result = inquiry.ask("Convert 8.3 meters to nanometers")
        self.assertEqual(result, "8300000000.0 nanometers")

    @job_story('When I ask \'What is the meaning of life\' I want'
               ' the system to respond with \'42\' to indicate its wisdom')
    def test_meaning_life(self, inquiry=Interface()):
        """This tests the meaning of life"""
        result = inquiry.ask("What is the meaning of life?")
        self.assertEqual(result, "42")

    @job_story('When I ask \'Please make me a grilled cheese\' '
               'I want the application to say \'I can\'t make sandwiches'
               '\' because it\'s just a normal computer and shouldn\'t '
               'be able to make food')
    def test_make_sandwich(self, inquiry=Interface()):
        """This tests making a grilled cheese"""
        result = inquiry.ask("Please make me a grilled cheese?")
        self.assertEqual(result, "I can't make sandwiches")

    @job_story('When I ask \'Do you have a facebook\' I want the '
               'application to say \'No I have a life\' to indicate its wisdom')
    def test_have_facebook(self, inquiry=Interface()):
        """This tests asking about facebook"""
        result = inquiry.ask("Do you have a facebook?")
        self.assertEqual(result, "No I have a life")

    @job_story('When I ask \'What is myspace\' I want the application to say'
               ' \'I\'m sorry. I have no information on trash\' to show it has class')
    def test_myspace_is_trash(self, inquiry=Interface()):
        """This tests asking about skype"""
        result = inquiry.ask("What is myspace?")
        self.assertEqual(result, "I'm sorry. I have no information on trash")


class TestAnswer2(TestCase):
    """This tests answers"""
    @job_story('When I ask \'Do you eat\' I want the application to '
               'say "No I am a computer" to remind the user that computers don\'t eat')
    def test_computers_do_not_eat(self, inquiry=Interface()):
        """This tests if computers eat"""
        result = inquiry.ask("Do you eat?")
        self.assertEqual(result, "No I am a computer")

    @job_story('When I ask "Convert <number> <units> to <units>" I want '
               'to receive the converted value and units so I can know the answer.')
    def test_base_not_in_conversions(self, inquiry=Interface()):
        """This tests converting a number"""
        result = inquiry.ask("Convert 8 ameters to kilometers")
        self.assertEqual(result, "I don't know how to convert that.")

    @job_story('When I ask "Convert <number> <units> to <units>" I want'
               ' to receive the converted value and units so I can know the answer.')
    def test_base_as_decimal(self, inquiry=Interface()):
        """This tests converting a number"""
        result = inquiry.ask("Convert 100 centimeters to meters")
        self.assertEqual(result, "1 meter")

    @job_story('When I ask "Convert <number> <units> to <units>" I want to '
               'receive the converted value and units so I can know the answer.')
    def test_wrong_unit(self, inquiry=Interface()):
        """This tests converting a number"""
        result = inquiry.ask("Convert 12 ft to meters")
        self.assertEqual(result, "I don't know how to convert that")

    @job_story('When I ask "Convert <number> <units> to <units>" I want to'
               ' receive the converted value and units so I can know the answer.')
    def test_wrong_type_value(self, inquiry=Interface()):
        """This tests converting a number"""
        result = inquiry.ask("Convert a meter to centimeters")
        self.assertEqual(result, "Cannot convert to float")

    @job_story('When i ask "Define <word>" I want the application'
               ' to give me the definition so i don\'t have to look it up')
    def test_word_not_in_dictionary(self, inquiry=Interface()):
        """This tests defining a word"""
        result = inquiry.ask("Define dance")
        self.assertEqual(result, "I don't know the definition for that")

    @job_story('When i ask "Define <word>" I want the application to'
               ' give me the definition so i don\'t have to look it up')
    def test_define_word(self, inquiry=Interface()):
        """This tests defining a word"""
        result = inquiry.ask("Define Truck")
        self.assertEqual(result, "Any of various forms of vehicle"
                                 " for carrying goods and materials,"
                                 " usually consisting of a single"
                                 " self-propelled unit but also"
                                 " often composed of a trailer"
                                 " vehicle hauled by a tractor unit")

    @job_story('When i ask "What polygon has <# of sides> sides" I want'
               ' to receive the answer so i don\'t have to figure it out myself')
    def test_type_of_polygon_3_sides(self, inquiry=Interface()):
        """This tests type of polygon"""
        result = inquiry.ask("What polygon has 3 sides?")
        self.assertEqual(result, "Triangle")

    @job_story('When i ask "What polygon has <# of sides> sides" I want'
               ' to receive the answer so i don\'t have to figure it out myself')
    def test_type_of_polygon_4_sides(self, inquiry=Interface()):
        """This tests type of polygon"""
        result = inquiry.ask("What polygon has 4 sides?")
        self.assertEqual(result, "Quadrilateral")

    @job_story('When i ask "What polygon has <# of sides> sides" I want'
               ' to receive the answer so i don\'t have to figure it out myself')
    def test_type_of_polygon_5_sides(self, inquiry=Interface()):
        """This tests type of polygon"""
        result = inquiry.ask("What polygon has 5 sides?")
        self.assertEqual(result, "Pentagon")

    @job_story('When i ask "What polygon has <# of sides> sides" I want'
               ' to receive the answer so i don\'t have to figure it out myself')
    def test_type_of_polygon_6_sides(self, inquiry=Interface()):
        """This tests type of polygon"""
        result = inquiry.ask("What polygon has 6 sides?")
        self.assertEqual(result, "Hexagon")

    @job_story('When i ask "What polygon has <# of sides> sides" I want'
               ' to receive the answer so i don\'t have to figure it out myself')
    def test_type_of_polygon_7_sides(self, inquiry=Interface()):
        """This tests type of polygon"""
        result = inquiry.ask("What polygon has 7 sides?")
        self.assertEqual(result, "Heptagon")

    @job_story('When i ask "What polygon has <# of sides> sides" I want'
               ' to receive the answer so i don\'t have to figure it out myself')
    def test_type_of_polygon_8_sides(self, inquiry=Interface()):
        """This tests type of polygon"""
        result = inquiry.ask("What polygon has 8 sides?")
        self.assertEqual(result, "Octagon")

    @job_story('When i ask "What polygon has <# of sides> sides" I want'
               ' to receive the answer so i don\'t have to figure it out myself')
    def test_type_of_polygon_9_sides(self, inquiry=Interface()):
        """This tests type of polygon"""
        result = inquiry.ask("What polygon has 9 sides?")
        self.assertEqual(result, "Nonagon")

    @job_story('When i ask "What polygon has <# of sides> sides" I want'
               ' to receive the answer so i don\'t have to figure it out myself')
    def test_type_of_polygon_10_sides(self, inquiry=Interface()):
        """This tests type of polygon"""
        result = inquiry.ask("What polygon has 10 sides?")
        self.assertEqual(result, "Decagon")

    @job_story('When i ask "What polygon has <# of sides> sides" I want'
               ' to receive the answer so i don\'t have to figure it out myself')
    def test_type_of_polygon_invalid(self, inquiry=Interface()):
        """This tests type of polygon"""
        result = inquiry.ask("What polygon has 11 sides?")
        self.assertEqual(result, "I don't know")

    @job_story('When i ask "What is the n letter of the alphabet"'
               ' I want to receive the answer so i don\'t have to figure it out myself')
    def test_n_letter_alphabet(self, inquiry=Interface()):
        """This tests the alphabet"""
        result = inquiry.ask("What is the 5 letter of the alphabet?")
        self.assertEqual(result, "E")

    @job_story('When i ask "What is the n letter of the alphabet"'
               ' I want to receive the answer so i don\'t have to figure it out myself')
    def test_n_letter_invalid(self, inquiry=Interface()):
        """This tests the alphabet"""
        result = inquiry.ask("What is the 27 letter of the alphabet?")
        self.assertEqual(result, "Does not exist")

    @job_story('When i ask "What degree of polynomial is x^ <degree>'
               '" I want to receive the answer for my physics hw')
    def test_n_degree_polynomial(self, inquiry=Interface()):
        """This tests degree of polynomial"""
        result = inquiry.ask("What degree of polynomial is x^ 2?")
        self.assertEqual(result, "Quadratic")

    @job_story('When i ask "What is the sine of <number>"'
               ' I want to receive the answer so i can do my trig hw')
    def test_sin(self, inquiry=Interface()):
        """This tests sine of a number"""
        result = inquiry.ask("What is the sine of 150?")
        self.assertEqual(result, -0.7148764296291646)
