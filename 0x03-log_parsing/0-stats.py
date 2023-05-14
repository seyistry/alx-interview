#!/usr/bin/python3
"""0x03. Log Parsing
    """

import sys
import os

allowed_status_code = [200, 301, 400, 401, 403, 404, 405, 500]
add_status_call = {}
count = 0
file_size = 0

try:
    for line in sys.stdin:
        count = count + 1
        arr = str(line).strip().split(" ")
        try:
            file_size = file_size + int(arr[-1])
        except Exception as e:
            continue
        try:
            if int(arr[-2]) in allowed_status_code:
                if int(arr[-2]) not in add_status_call:
                    add_status_call[int(arr[-2])] = 1
                else:
                    add_status_call[int(
                        arr[-2])] = add_status_call[int(arr[-2])] + 1
        except Exception as e:
            continue
        if count % 10 == 0:
            print("File size: {}".format(file_size))
            for key in sorted(add_status_call):
                print("{}: {}".format(key, add_status_call[key]))
            # file_size = 0
    print("File size: {}".format(file_size))
    for key in sorted(add_status_call):
        print("{}: {}".format(key, add_status_call[key]))
except KeyboardInterrupt:
    print("File size: {}".format(file_size))
    for key in sorted(add_status_call):
        print("{}: {}".format(key, add_status_call[key]))
