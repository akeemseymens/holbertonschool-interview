#!/usr/bin/python3
"""
UTF8 function checking
"""


def validUTF8(data):
    """
    check if array of UTF-8 is valid
    """
    bytes_behind = 0
    for byte in data:
        if bytes_behind:
            if byte >> 6 != 0b10:
                return False
            bytes_behind -= 1
        else:
            if byte >> 7 == 0:
                continue
            elif byte >> 3 == 0b11110:
                bytes_behind = 3
            elif byte >> 4 == 0b1110:
                bytes_behind = 2
            elif byte >> 5 == 0b110:
                bytes_behind = 1
            else:
                return False

    return bytes_behind == 0