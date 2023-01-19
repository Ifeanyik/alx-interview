#!/usr/bin/python3
"""This script reads stdin by line and computes metrics"""
from sys import stdin


line_number = 1
total_file_size = 0
status_code_counts = {}

try:
    for line in stdin:
        if len(line) == 1:
            break

        try:
            status_code, file_size = line.split()[-2:]
            total_file_size += int(file_size)
            if status_code_counts.get(int(status_code)) is None:
                status_code_counts[int(status_code)] = 0
            status_code_counts[int(status_code)] += 1
        except ValueError:
            pass

        if line_number % 10 == 0:
            print('File size:', total_file_size)
            for code, count in sorted(status_code_counts.items()):
                print('{}: {}'.format(code, count))

        line_number += 1
except KeyboardInterrupt:
    pass
finally:
    print('File size:', total_file_size)
    for code, count in sorted(status_code_counts.items()):
        print('{}: {}'.format(code, count))
