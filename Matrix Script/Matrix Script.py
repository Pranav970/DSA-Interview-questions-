#!/bin/python3

import math
import os
import random
import re
import sys

# The provided function skeleton (input reading)
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# ---  My code to decode the matrix ---
decoded_script = ""
for j in range(m):
    for i in range(n):
        decoded_script += matrix[i][j]

# Use regex to replace non-alphanumeric characters between alphanumeric characters with a space
print(re.sub(r'(?<=[A-Za-z0-9])([ !@#$%&]+)(?=[A-Za-z0-9])', ' ', decoded_script))
