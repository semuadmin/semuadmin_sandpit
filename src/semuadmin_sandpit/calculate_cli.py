"""
calculate_cli.py

CLI wrapper for Calculate class.

Just an arbitrary set of simple functions to
exercise VSCode and Github build, test and deploy
workflows.

Created on 24 Jul 2022

:author: semuadmin
:copyright: SEMU Consulting © 2022
:license: BSD 3-Clause
"""

from argparse import ArgumentDefaultsHelpFormatter, ArgumentParser

from semuadmin_sandpit._version import __version__ as VERSION
from semuadmin_sandpit.calculate import Calculate

EPILOG = (
    "© 2022 SEMU Consulting BSD 3-Clause license"
    " - https://github.com/semuadmin/sandpit/"
)


def main():
    """
    CLI Entry point.
    """

    # pylint: disable=no-member

    ap = ArgumentParser(
        epilog=EPILOG,
        formatter_class=ArgumentDefaultsHelpFormatter,
    )
    ap.add_argument("-V", "--version", action="version", version="%(prog)s " + VERSION)
    ap.add_argument(
        "--function", required=True, help="Function", choices=["add", "multiply"]
    )
    ap.add_argument(
        "--arg1",
        required=True,
        help="Argument 1",
        type=float,
    )
    ap.add_argument(
        "--arg2",
        required=True,
        help="Argument 2",
        type=float,
    )

    args = ap.parse_args()
    c = Calculate()
    print(c.calc(args.function, args.arg1, args.arg2))


if __name__ == "__main__":
    main()
