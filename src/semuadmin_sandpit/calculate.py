"""
calculate.py

Just an arbitrary set of simple functions to
exercise VSCode and Github build, test and deploy
workflows.

Created on 24 Jul 2022

:author: semuadmin
:copyright: SEMU Consulting © 2022
:license: BSD 3-Clause
"""


class Calculate:
    """
    Calculate class.
    """

    def __init__(self):
        """
        Constructor
        """

    def calc(self, function: str, arg1: float, arg2: float):
        """
        Perform designated calculation.

        :param str function: function (add/multiply)
        :param float arg1: argument 1
        :param float arg2: argument 2
        :return: result
        :rtype: float
        :raises: ValueError
        """

        if function == "add":
            return self.add(arg1, arg2)
        if function == "multiply":
            return self.multiply(arg1, arg2)
        raise ValueError("Invalid function")

    def add(self, arg1: float, arg2: float) -> float:
        """
        Add 2 arguments.

        :param float arg1: argument 1
        :param float arg2: argument 2
        :return: result
        :rtype: float
        """

        return arg1 + arg2

    def multiply(self, arg1: float, arg2: float) -> float:
        """
        Multiply 2 arguments.

        :param float arg1: argument 1
        :param float arg2: argument 2
        :return: result
        :rtype: float
        """

        return arg1 * arg2
