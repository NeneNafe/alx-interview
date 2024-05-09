#!/usr/bin/python3
"""a method that determines if a given data set represents
a valid UTF-8 encoding"""


def validUTF8(data):
    """Determines whether given data set represents a valid UTF-8"""
    if data == []:
        return True

    # Now we convert each num in the data list to binary representation
    # with 8 bits
    bin_data = [bin(num)[2:].zfill(8) for num in data]

    # check if the bin_num starts with a 0
    if any(bin_num.startswith("0") for bin_num in bin_data):
        return False

    # Checks if any bin_num in bin_data except the first one start with '10'
    if any(not bin_num.startswith("10") for bin_num in bin_data[1:]):
        return False

    # Now we will convert the binary data back to original characters

    # Check if any of the resulting code points falls within the specific range
    decoded_chars = [int(bin_num, 2) for bin_num in bin_data]
    if any(0xD800 <= code_point <= 0xDFFF for code_point in decoded_chars):
        return False

    # Now we re-encode the chars to binary using UTF-8 encoding
    decoded_str = "".join(chr(char) for char in decoded_chars)
    reencoded_data = decoded_str.encode("utf-8")
    if bin_data != [bin(byte)[2:].zfill(8) for byte in reencoded_data]:
        return False

    # if any code point exceeds maxi value, return false
    if any(code_point > 0x10FFFF for code_point in decoded_chars):
        return False

    # Validate the sequence length
    # enumerate is used to iterate over each binary num in bin_data
    expected_len = 0
    for n, bin_num in enumerate(bin_data):
        if n == 0:
            if bin_num.startswith("110"):
                expected_len = 2
            elif bin_num.startswith("1110"):
                expected_len = 3
            elif bin_num.startswith("11110"):
                expected_len = 4
            else:
                continue
        elif bin_num.startswith("10"):
            expected_len -= 1  # continuation bytes
        else:
            return False
    if expected_len > 0:
        return False

    return True
