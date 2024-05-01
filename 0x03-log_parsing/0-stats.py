#!/usr/bin/python3
""" a script that reads stdin line by line and computes metrics"""

import sys


# a count of all status code in a dict presentation
lines_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
              '404': 0, '405': 0, '500': 0}
line_count = 0
total_size = 0  # keeps the count of the numbs counted


try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            # checks whether the code status exists in the dict
            # and increments its count
            if status_code in lines_dict.keys():
                lines_dict[status_code] += 1

            # updates the total size
            total_size += file_size

            # updates the count of lines
            line_count += 1

            if line_count == 10:
                line_count = 0  # resets count
                print('File size: {}'.format(total_size))

                # prints out the status code count
                for key, value in sorted(lines_dict.items()):
                    if value != 0:
                        print('{}: {}'.format(key, value))

except Exception as err:
    pass

finally:
    print('File size: {}'.format(total_size))
    for key, value in sorted(lines_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))
