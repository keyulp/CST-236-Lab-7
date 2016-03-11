"""Tests for performance"""
from unittest import TestCase
from source.main import Interface
from test.plugins.ReqTracer import requirements


class TestPerformance(TestCase):
    """This tests performance"""

    @requirements({"#0050", "#0051", "#0052"})
    def test_writes_to_log_file(self, inquiry=Interface()):
        """This tests that input is written to the log file"""
        result = inquiry.ask('What is myspace?')
        self.assertEqual(result, 'I\'m sorry. I have no information on trash')

    @requirements({"#0053"})
    def test_100_digit_of_fibonacci(self, inquiry=Interface()):
        """This tests the 100th digit of fibonacci"""
        result = inquiry.ask("What is the 100 digit of fibonacci?")
        self.assertEqual(result, 218922995834555169026L)

    @requirements({"#0054"})
    def test_100_digit_of_pi(self, inquiry=Interface()):
        """This tests the 100th digit of pi"""
        result = inquiry.ask("What is the 100 digit of pi?")
        self.assertEqual(result, '9')

    @requirements({"#0055"})
    def test_sine_of_30000(self, inquiry=Interface()):
        """This tests the sin of 3000"""
        result = inquiry.ask("What is the sine of 30000?")
        self.assertEqual(result, -0.802665441867374)

    @requirements({"#0056"})
    def test_letter_alphabet_perf(self, inquiry=Interface()):
        """This tests the nth letter of the alphabet"""
        result = inquiry.ask("What is the 23 letter of the alphabet?")
        self.assertEqual(result, "W")

    @requirements({"#0057"})
    def test_convert_performance(self, inquiry=Interface()):
        """This tests the conversion of numbers"""
        result = inquiry.ask("Convert 22156 meters to kilometers")
        self.assertEqual(result, "22.156 kilometers")
