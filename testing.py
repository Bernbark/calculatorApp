"""Testing File

This script is an attempt to follow proper testing protocols and learn testing at the same time. Any advice is welcome!


"""

import unittest
import calc

class TestMethods(unittest.TestCase):

    def test_add(self):
        result = calc.add(10, 5)
        self.assertEqual(result, 15, "If 10 and 5 are added together, the result should be 15")

    def test_subtract(self):
        result = calc.subtract(10, 5)
        self.assertEqual(result, 5, "10 - 5 should equal 5.")


