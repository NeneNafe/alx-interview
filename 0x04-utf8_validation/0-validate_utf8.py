#!/usr/bin/python3
"""a method that determines if a given data set represents
a valid UTF-8 encoding"""


def validUTF8(data):
    """Determines whether given data set represents a valid UTF-8"""
    expected_len = 0  # Initialize expected length of the sequence

    for n in data:  # Iterate through each byte in the data
        if expected_len == 0:
            if n >> 5 == 0b110 or n >> 5 == 0b1110:
                # Check if byte is the start of a 2 or 3-byte sequence
                expected_len = 1
            elif n >> 4 == 0b1110:
                expected_len = 2
            elif n >> 3 == 0b11110:
                expected_len = 3

            # If byte is a continuation byte (starts with 10) return False
            elif n >> 7 == 0b1:
                return False
        else:  # If this is a continuation byte
            if n >> 6 != 0b10:
                return False
            # Decrement the expected length of each continuation byte
            expected_len -= 1
    return expected_len == 0  # True if expected matches actual length
