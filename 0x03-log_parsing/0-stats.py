#!/usr/bin/env python3
""" a script that reads stdin line by line and computes metrics"""

import sys


total_size = 0
lines_dict = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0,
              '404': 0, '405': 0, '500': 0}
line_count = 0


try:
    for line in sys.stdin:
        line_list = line.split(" ")

        if len(line_list) > 4:
            status_code = line_list[-2]
            file_size = int(line_list[-1])

            if status_code in lines_dict.keys():
                lines_dict[status_code] += 1

            total_size += file_size

            line_count += 1

            if line_count == 10:
                line_count = 0
                print('File size: {}'.format(total_size))

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
