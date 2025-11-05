"""
Created on 19 Dec 2020

@author: semuadmin
"""

# pylint: disable=missing-class-docstring, missing-function-docstring

import unittest
from tkinter import Tk, Entry, TclError

from semuadmin_sandpit.calculate import Calculate


class StaticTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testadd(self):
        c = Calculate()
        self.assertEqual(c.add(2.5, 3.5), 6)

    def testmultiply(self):
        c = Calculate()
        self.assertEqual(c.multiply(2.5, 3.5), 8.75)

    def testcalculate(self):
        c = Calculate()
        self.assertEqual(c.calc("add", 2.5, 3.5), 6)
        self.assertAlmostEqual(c.calc("multiply", 2.5, 3.5), 8.75, 6)

    def testcalculateerror(self):
        # pylint: disable=unused-variable
        c = Calculate()
        with self.assertRaisesRegex(ValueError, "Invalid function"):
            res = (
                c.calc("divide", 2.5, 3.5),
                0.7142857142857143,
            )

    def testtk(self):  # test if Tk instance can be instantiated in GitHub test action

        try:
            root = Tk()
            ent = Entry(root)
        except TclError as err:
            if str(err) == "no display name and no $DISPLAY environment variable":
                print(f"{err}\nCan't execute this test without Window environment")
            else:
                raise TclError from err


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
