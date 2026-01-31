"""
helpers.py

Created on 24 Jul 2022

:author: semuadmin
:copyright: SEMU Consulting © 2022
:license: BSD 3-Claus
"""

import struct
from typing import Any

ATTTYPE = {
    "S": type(-1),
    "R": type(1.1),
    "U": type(1),
    "X": type(b"0"),
    "C": type("X"),
}


def attsiz(att: str) -> int:
    """
    Helper function to return attribute size in bytes.

    :param str: attribute type e.g. 'U002'
    :return: size of attribute in bytes, or -1 if variable length
    :rtype: int

    """

    try:
        return int(att[1:4])
    except ValueError:
        return -1


def atttyp(att: str) -> str:
    """
    Helper function to return attribute type as string.

    :param str: attribute type e.g. 'U002'
    :return: type of attribute as string e.g. 'U'
    :rtype: str

    """

    return att[0:1]


def bytes2val(valb: bytes, att: str) -> object:
    """
    Convert bytes to value for given attribute type.

    :param bytes valb: attribute value in byte format e.g. b'\\\\x19\\\\x00\\\\x00\\\\x00'
    :param str att: attribute type e.g. 'U004'
    :return: attribute value as int, float, str or bytes
    :rtype: object
    :raises: TypeError

    """

    if atttyp(att) == "X":  # bytes
        val = valb
    elif atttyp(att) == "C":  # string
        val = valb.decode("utf-8", errors="backslashreplace")
    elif atttyp(att) in ("S", "U"):  # integer
        val = int.from_bytes(valb, byteorder="little", signed=atttyp(att) == "S")
    elif atttyp(att) == "R":  # floating point
        val = struct.unpack("<f" if attsiz(att) == 4 else "<d", valb)[0]
    else:
        raise TypeError(f"Unknown attribute type {att}")
    return val


def nomval(att: str) -> object:
    """
    Get nominal value for given attribute type.

    :param str att: attribute type e.g. 'U004'
    :return: attribute value as int, float, str or bytes
    :rtype: object
    :raises: TypeError

    """

    if atttyp(att) == "X":
        val = b"\x00" * attsiz(att)
    elif atttyp(att) == "C":
        val = " " * attsiz(att)
    elif atttyp(att) == "R":
        val = 0.0
    elif atttyp(att) in ("S", "U"):
        val = 0
    else:
        raise TypeError(f"Unknown attribute type {att}")
    return val


def val2bytes(val: Any, att: str) -> bytes:
    """
    Convert value to bytes for given attribute type.

    :param Any val: attribute value e.g. 25
    :param str att: attribute type e.g. 'U004'
    :return: attribute value as bytes
    :rtype: bytes
    :raises: TypeError

    """
    try:
        if not isinstance(val, ATTTYPE[atttyp(att)]):
            raise TypeError(
                f"Attribute type {att} value {val} must be {ATTTYPE[atttyp(att)]}, not {type(val)}"
            )
    except KeyError as err:
        raise TypeError(f"Unknown attribute type {att}") from err

    valb = val
    if atttyp(att) == "X":  # byte
        valb = val
    elif atttyp(att) == "C":  # string
        # v = val.encode("utf-8", errors="backslashreplace")
        # valb = v + b"\x20" * (attsiz(att) - len(v))  # right pad with spaces
        valb = f"{val:<{attsiz(att)}}".encode("utf-8", errors="backslashreplace")
    elif atttyp(att) in ("S", "U"):  # integer
        valb = val.to_bytes(attsiz(att), byteorder="little", signed=atttyp(att) == "S")
    elif atttyp(att) == "R":  # floating point
        valb = struct.pack("<f" if attsiz(att) == 4 else "<d", float(val))
    return valb
