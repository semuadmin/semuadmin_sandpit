"""
Created on 19 Dec 2020

@author: semuadmin
"""

# pylint: disable=missing-class-docstring, missing-function-docstring

import unittest
from subprocess import PIPE, run

from semuadmin_sandpit.calculate import Calculate
from semuadmin_sandpit.helpers import val2bytes, bytes2val, nomval


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

    def testVal2Bytes(self):  # test conversion of value to bytes
        INPUTS = [
            (2345, "U002"),
            (b"\x44\x55", "X002"),
            (23.12345678, "R004"),
            (-23.12345678912345, "R008"),
            ("test1234", "C008"),
            ("test1234", "C016"),
        ]
        EXPECTED_RESULTS = [
            b"\x29\x09",
            b"\x44\x55",
            b"\xd7\xfc\xb8\x41",
            b"\x1f\xc1\x37\xdd\x9a\x1f\x37\xc0",
            b"test1234",
            b"test1234        ",
        ]
        for i, inp in enumerate(INPUTS):
            (val, att) = inp
            res = val2bytes(val, att)
            self.assertEqual(res, EXPECTED_RESULTS[i])

    def testVal2BytesInvalid(self):
        with self.assertRaisesRegex(TypeError, "Unknown attribute type Y002"):
            res = val2bytes(1234, "Y002")

    def testBytes2Val(self):  # test conversion of bytes to value
        INPUTS = [
            (b"\x29\x09", "U002"),
            (b"\x44\x55", "X002"),
            (b"\xd7\xfc\xb8\x41", "R004"),
            (b"\x1f\xc1\x37\xdd\x9a\x1f\x37\xc0", "R008"),
            (b"test1234", "C008"),
        ]
        EXPECTED_RESULTS = [
            2345,
            b"\x44\x55",
            23.12345678,
            -23.12345678912345,
            "test1234",
        ]
        for i, inp in enumerate(INPUTS):
            (valb, att) = inp
            res = bytes2val(valb, att)
            if att == "R004":
                self.assertAlmostEqual(res, EXPECTED_RESULTS[i], 6)
            elif att == "R008":
                self.assertAlmostEqual(res, EXPECTED_RESULTS[i], 14)
            else:
                self.assertEqual(res, EXPECTED_RESULTS[i])

    def testBytes2ValInvalid(self):
        with self.assertRaisesRegex(TypeError, "Unknown attribute type Y002"):
            res = bytes2val(b"\x12\x34", "Y002")

    def testNomval(self):  # test conversion of value to bytes
        INPUTS = [
            "U002",
            "X002",
            "R004",
            "R008",
            "C008",
        ]
        EXPECTED_RESULTS = [
            0,
            b"\x00\x00",
            0.0,
            0.0,
            "        ",
        ]
        for i, att in enumerate(INPUTS):
            res = nomval(att)
            self.assertEqual(res, EXPECTED_RESULTS[i])

    def testNomValInvalid(self):
        with self.assertRaisesRegex(TypeError, "Unknown attribute type Y002"):
            res = nomval("Y002")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
