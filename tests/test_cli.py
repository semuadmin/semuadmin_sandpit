"""
Created on 19 Dec 2020

@author: semuadmin
"""

# pylint: disable=missing-class-docstring, missing-function-docstring

import unittest
import subprocess
from subprocess import PIPE, run


class StaticTest(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testcli(self):  # must be installed via pip first
        res = subprocess.run(
            ["calculate", "--function", "add", "--arg1", "2.5", "--arg2", "3.5"],
            stdout=PIPE,
            check=False,
        )
        res = res.stdout.decode("utf-8").strip("\r\n")
        self.assertEqual(res, "6.0")


if __name__ == "__main__":
    # import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
