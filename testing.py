"""Testing File

This script is an attempt to follow proper testing protocols and learn testing at the same time. Any advice is welcome!

"""

import unittest
import calc
import calcUI


class TestCalcFunctionalityMethods(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15, "If 10 and 5 are added together, the result should be 15")

    def test_subtract(self):
        result = calc.subtract(10, 5)
        self.assertEqual(result, 5, "10 - 5 should equal 5.")

    def test_divide(self):
        result = calc.divide(12, 6)
        self.assertEqual(result, 2, "12 / 6 should equal 2")

    def test_zero_division(self):
        result = calc.divide(12, 0)
        self.assertEqual(result, "Undefined", "Anything divided by 0 should report back as undefined")


class TestUIFunctionality(unittest.TestCase):

    def test_output_for_zero_start(self):
        result = "07"                           # starting off the string with a 0 should not be allowed, it should be 7
        testStr = calcUI.CalcUI().display_number("7")    # calling on the class within the file, and setting a number

        self.assertNotEqual(result, testStr, "0 shouldn't display at the start of a number")

    def test_output_for_equality(self):
        """ This checks for equality of the label versus the expected result of 7

        :return: true if it's equal
        """
        result = "7"
        testStr = calcUI.CalcUI().display_number("7")    # calling on the class within the file, and setting a number

        self.assertEqual(result, testStr)

    def test_output_for_addition(self):
        result = "0 + 7 + "
        teststr = calcUI.CalcUI().add_button("0")
        teststr += calcUI.CalcUI().add_button("7")

        self.assertEqual(result, teststr)

    def test_output_for_division(self):
        result = "0 / 7 / "
        teststr = calcUI.CalcUI().divide("0")
        teststr += calcUI.CalcUI().divide("7")

        self.assertEqual(result,teststr)

    def test_clear_button(self):
        result = "0"                                    # make sure that when we clear, there is a number inside output
        teststr = calcUI.CalcUI().clear()               # clear() returns the text inside of CalcUI().output

        self.assertEqual(result, teststr)

    def test_equals_button_division(self):
        result = "6.0"
        test_string = calcUI.CalcUI().equals("12 / 2")

        self.assertEqual(result, test_string)

    def test_divide_by_zero(self):
        result = "Undefined"
        test_string = calcUI.CalcUI().equals("12 / 0")
        self.assertEqual(result, test_string)

    def test_delete_button_whitespace(self):
        result = "12 /"
        test_string = calcUI.CalcUI().delete("12 / 0")
        self.assertEqual(result, test_string)

    def test_delete_button_decimal(self):
        """ If the decimal is the last char after deleting, it should be deleted automatically"""
        result = "123"
        test_string=calcUI.CalcUI().delete("123.4")
        self.assertEqual(result, test_string)

    def test_decimal_placement(self):
        result = "123."
        test_string = calcUI.CalcUI().display_special_character(".", "123")
        self.assertEqual(result, test_string)

    def test_decimal_duplication_prevention(self):
        result = "123."
        test_string=calcUI.CalcUI().display_special_character(".","123.")
        self.assertEqual(result, test_string)

    # NEXT UP: Adding decimals breaks the division system, need to check string for decimals and work around them