#!/usr/bin/python3
"""
Reads stdin line by line and computes metrics
based on the input format.
"""


import sys


# Initialize variables
total_file_size = 0
status_codes = {}

try:
    for count, line in enumerate(sys.stdin, start=1):
        # Parse the line
        parts = line.split(" ")
        if len(parts) >= 7:
            status_code = parts[-2]
            file_size = int(parts[-1])

            # Update total file size
            total_file_size += file_size

            # Update status codes count
            if status_code in status_codes:
                status_codes[status_code] += 1
            else:
                status_codes[status_code] = 1

        # Print metrics every 10 lines
        if count % 10 == 0:
            print("File size: {}".format(total_file_size))
            sorted_codes = sorted(status_codes.items(), key=lambda x: x[0])
            for code, count in sorted_codes:
                print("{}: {}".format(code, count))

except KeyboardInterrupt:
    # Print final metrics on keyboard interruption
    print("File size: {}".format(total_file_size))
    sorted_codes = sorted(status_codes.items(), key=lambda x: x[0])
    for code, count in sorted_codes:
        print("{}: {}".format(code, count))
