"""
Test for source.main
"""
from unittest import TestCase

from test.plugins.ReqTracer import requirements
from source.main import Interface


def blah():
    """This tests the generator function"""
    return "blah"


class TestMain(TestCase):
    """This tests the main"""


    @requirements(['#0006', '#0007', '#0010', '#0011', '#0012', '#0013'])
    def test_question_as_string(self, inquiry=Interface()):
        """This tests a question as a string"""
        result = Interface.ask(inquiry, 'What type of triangle is 1 1 1 ?')
        self.assertEqual(result, "equilateral")

    @requirements(['#0006', '#0007', '#0010'])
    def test_question_with_how(self, inquiry=Interface()):
        """This tests a question with how"""
        result = Interface.ask(inquiry, 'How do you make a triangle?')
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0006', '#0007', '#0010'])
    def test_question_with_who(self, inquiry=Interface()):
        """This tests a question with who"""
        result = Interface.ask(inquiry, 'Who wrote this code?')
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0006', '#0007', '#0010'])
    def test_question_with_where(self, inquiry=Interface()):
        """This tests a question with where"""
        result = Interface.ask(inquiry, 'Where was this code written?')
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0006', '#0007', '#0010'])
    def test_question_with_why(self, inquiry=Interface()):
        """This tests a question with why"""
        result = Interface.ask(inquiry, 'Why did you write this code?')
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0006', '#0008', '#0010'])
    def test_question_bad_type(self, inquiry=Interface()):
        """This tests a question without a proper question type"""
        result = Interface.ask(inquiry, 'When did you start this lab?')
        self.assertEqual(result, "Was that a question?")

    @requirements(['#0006', '#0008', '#0009', '#0010'])
    def test_question_no_question_mark(self, inquiry=Interface()):
        """This tests a question without a question mark"""
        result = Interface.ask(inquiry, 'Why did you start this lab')
        self.assertEqual(result, "Was that a question?")

    @requirements(['#0006', '#0007', '#0010', '#0011', '#0012', '#0013'])
    def test_question_with_keywords(self, inquiry=Interface()):
        """This tests a question with a keyword"""
        result = Interface.ask(inquiry, "What type of quadrilateral is 1 1 1 1 90 90 90 90?")
        self.assertEqual(result, "square")

    @requirements(['#0006', '#0007', '#0010', '#0011', '#0012', '#0014'])
    def test_question_with_no_answer(self, inquiry=Interface()):
        """This tests a question without an answer"""
        result = Interface.ask(inquiry, "What type of shape is 1 1 1 1 90 90 90 90?")
        self.assertEqual(result, "I don't know, please provide the answer")

    @requirements(['#0006', '#0007', '#0010', '#0015'])
    def test_answer_previous_question(self, inquiry=Interface()):
        """This tests the previous question"""
        Interface.ask(inquiry, "What is the acceleration of gravity?")
        Interface.teach(inquiry, "-9.8 m/s")
        result = Interface.ask(inquiry, "What is the acceleration of gravity?")
        self.assertEqual(result, "-9.8 m/s")

    @requirements(['#0016', '#0020'])
    def test_teach_answer_function(self, inquiry=Interface()):
        """This tests teaching an answer"""
        Interface.ask(inquiry, "What is the acceleration of gravity?")
        inquiry.teach(blah)
        result = Interface.ask(inquiry, "What is the acceleration of gravity?")
        self.assertEqual(result, blah())

    @requirements(['#0017', '#0021'])
    def test_no_previous_question_1(self, inquiry=Interface()):
        """This tests no previously asked question"""
        result = Interface.teach(inquiry, 'What type of triangle is 10 11 12 ?')
        self.assertEqual(result, "Please ask a question first")

    @requirements(['#0018'])
    def test_already_known(self, inquiry=Interface()):
        """This tests teaching an answer to an answered question"""
        inquiry.ask('What type of quadrilateral is 1 1 1 1 90 90 90 90 ?')
        result = inquiry.teach('equilateral')
        self.assertEqual(result, "I don\'t know about that. I was taught differently")

    @requirements(['#0019'])
    def test_correct_answer(self, inquiry=Interface()):
        """This tests correcting an answer"""
        Interface.ask(inquiry, "What is the acceleration of gravity?")
        inquiry.correct("9.8 m/s")
        result = Interface.ask(inquiry, "What is the acceleration of gravity?")
        self.assertEqual(result, "9.8 m/s")

    @requirements(['#0006'])
    def test_exception_not_a_string(self, inquiry=Interface()):
        """This tests raising the exception for not a string"""
        with self.assertRaises(Exception, msg="Not A String!"):
            inquiry.ask(42)

    @requirements(["#0012"])
    def test_exception_too_many_param(self, inquiry=Interface()):
        """This tests raising the exception for too many extra parameters"""
        with self.assertRaises(Exception, msg="Too many extra parameters"):
            inquiry.ask("What type of triangle is 1 1 1 1 1?")

    @requirements(["#0017", "#0021"])
    def test_no_previous_question_2(self, inquiry=Interface()):
        """This tests no previous question"""
        result = inquiry.correct("42")
        self.assertEqual(result, "Please ask a question first")

