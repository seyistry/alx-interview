#!/usr/bin/python3
"""0x03. Log Parsing
	"""

import fileinput
import sys
import os

allowed_status_code = [200, 301, 400, 401, 403, 404, 405, 500]
add_status_call = {}
count = 0
file_size = 0

if __name__ == '__main__':
    try:
        for fileinput_line in fileinput.input():
            count = count + 1
            arr = str(fileinput_line).strip().split(" ")
            file_size = file_size + int(arr[-1])
            # print(arr[-2])
            try:
                if int(arr[-2]) in allowed_status_code:
                    if int(arr[-2]) not in add_status_call:
                        add_status_call[int(arr[-2])] = 1
                    else:
                        add_status_call[int(
                            arr[-2])] = add_status_call[int(arr[-2])] + 1
            except:
                con
            if count == 10:
                print(f"File size: {file_size}")
                for key in sorted(add_status_call):
                    print(f"{key}: {add_status_call[key]}")
                count = 0
                file_size = 0
    except KeyboardInterrupt:
        print(f"File size: {file_size}")
        for key in sorted(add_status_call):
            print(f"{key}: {add_status_call[key]}")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
