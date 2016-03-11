"""
Test for source.shape_checker
"""
from unittest import TestCase

from test.plugins.ReqTracer import requirements
from source.shape_checker import get_triangle_type, \
    get_quadrilateral_type, get_quadrilateral_type_length


class TestGetTriangleType(TestCase):
    """
    This is for testing shapes
    """
    @requirements(['#0001', '#0002'])
    def test_get_triangle_all_float(self):
        """This tests floats"""
        result = get_triangle_type(100000.9999999, 100000.9999999, 100000.9999999)
        self.assertEqual(result, 'equilateral')

    def test_get_triangle_invalid_zero(self):
        """This tests zero input"""
        result = get_triangle_type(0, 0, 0)
        self.assertEqual(result, 'invalid')

    def test_get_triangle_all_char(self):
        """This tests char input"""
        result = get_triangle_type('a', 'b', 'c')
        self.assertEqual(result, 'invalid')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_equi_all_int(self):
        """This tests equilateral all int"""
        result = get_triangle_type(100000, 100000, 100000)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_isos_all_int(self):
        """This tests isosceles all int"""
        result = get_triangle_type(1000000, 1000000, 30000)
        self.assertEqual(result, 'isosceles')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_scal_all_int(self):
        """This tests scalene all int"""
        result = get_triangle_type(100000000, 20000000, 30000000)
        self.assertEqual(result, 'scalene')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_tuple(self):
        """This tests tuple"""
        tuple1 = (1000, 1000, 1000)
        result = get_triangle_type(tuple1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_list(self):
        """This tests list"""
        list1 = [10000, 10000, 10000]
        result = get_triangle_type(list1)
        self.assertEqual(result, 'equilateral')

    @requirements(['#0001', '#0002'])
    def test_get_triangle_dictionary(self):
        """This tests dictionary"""
        dictionary = {'one': 100000, 'two': 100000, 'three': 100000}
        result = get_triangle_type(dictionary)
        self.assertEqual(result, 'equilateral')


class TestGetQuadrilateralTypeLength(TestCase):
    """This is for testing quadrilaterals with only a length"""

    def test_get_quadrilateral_len_char(self):
        """This tests char input"""
        result = get_quadrilateral_type_length("a", "b", "c", "d")
        self.assertEqual(result, "invalid")

    def test_get_quadrilateral_len_0(self):
        """This tests zero input"""
        result = get_quadrilateral_type_length(0, 0, 0, 0)
        self.assertEqual(result, "invalid")

    def test_get_quad_length_float(self):
        """This tests float input"""
        result = get_quadrilateral_type_length(1.7, 2.5, 1.7, 2.5)
        self.assertEqual(result, "rectangle")

    def test_get_square_length(self):
        """This tests square by lengths"""
        result = get_quadrilateral_type_length(1, 1, 1, 1)
        self.assertEqual(result, 'square')

    def test_get_rectangle_length(self):
        """This tests rectangle by lengths"""
        result = get_quadrilateral_type_length(1, 2, 1, 2)
        self.assertEqual(result, 'rectangle')


class TestGetQuadrilateralType(TestCase):
    """This tests quadrilaterals with a length and an angle"""

    def test_get_quadrilateral_all_char(self):
        """This tests char input"""
        result = get_quadrilateral_type("a", "b", "c", "d")
        self.assertEqual(result, "invalid")

    def test_get_quadrilateral_angles_0(self):
        """This tests angle as 0 input"""
        result = get_quadrilateral_type(5, 5, 5, 5, -32767, 0, -5, -40)
        self.assertEqual(result, "invalid")

    def test_get_quadrilateral_zero(self):
        """This tests length as zero input"""
        result = get_quadrilateral_type(0, 0, 0, 0)
        self.assertEqual(result, "invalid")

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_rhombus_all_float(self):
        """This tests float input"""
        result = get_quadrilateral_type(1.7, 1.7, 1.7, 1.7, 179.9, .1, 179.9, .1)
        self.assertEqual(result, "rhombus")

    def test_get_disconnected(self):
        """This tests if a shape is disconnected"""
        result = get_quadrilateral_type(1, 1, 1, 1, 60, 90, 60, 90)
        self.assertEqual(result, "disconnected")

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_square(self):
        """This tests square with length and angle"""
        result = get_quadrilateral_type(1, 1, 1, 1, 90, 90, 90, 90)
        self.assertEqual(result, "square")

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_rectangle(self):
        """This tests rectangle with length and angle"""
        result = get_quadrilateral_type(1, 2, 1, 2, 90, 90, 90, 90)
        self.assertEqual(result, "rectangle")

    @requirements(['#0003', '#0004', '#0005'])
    def test_get_rhombus(self):
        """This tests rhombus with length and angle"""
        result = get_quadrilateral_type(1, 1, 1, 1, 120, 60, 120, 60)
        self.assertEqual(result, "rhombus")
