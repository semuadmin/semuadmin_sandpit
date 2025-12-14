"""
Created on 19 Dec 2020

@author: semuadmin
"""

# pylint: disable=missing-class-docstring, missing-function-docstring

import unittest
from subprocess import PIPE, run

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

    def testcli(self):  # must be installed via pip first
        try:
            res = run(
                ["calculate", "--function", "add", "--arg1", "2.5", "--arg2", "3.5"],
                stdout=PIPE,
                check=False,
            )
            res = res.stdout.decode("utf-8").strip("\r\n")
            self.assertEqual(res, "6.0")
        except FileNotFoundError as err:
            print(err)


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
