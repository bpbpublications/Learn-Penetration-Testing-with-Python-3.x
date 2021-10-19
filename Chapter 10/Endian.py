#!/usr/bin/env python3
# Idetify System using is Little or Big Endian
# Author Yehia Elghaly

import sys

print()
if sys.byteorder == "little":

    print("System Use Little-endian.")
else:
    print("System Use Big-endian.")

print()