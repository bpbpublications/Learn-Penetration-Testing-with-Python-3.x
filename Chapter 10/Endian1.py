#!/usr/bin/env python3
# Convert Little or Big Endian
# Author Yehia Elghaly

import struct
print ("Big-Endian")
print (struct.pack('>I', 12454278))
print ()
print ("Little-Endian")
print (struct.pack('<I', 12454278))
print ()
print ("Size")
print (struct.calcsize('>I'))