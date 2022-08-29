"""Testing File

This script is an attempt to follow proper testing protocols and learn testing at the same time. Any advice is welcome!
TKinter is required as some of the UI elements need to be partially recreated to test

This script requires that 'tkinter' be installed within the Python environment you are running this script in.

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
