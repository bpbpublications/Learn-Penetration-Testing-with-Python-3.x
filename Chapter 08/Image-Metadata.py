#!/usr/bin/env python3
# Image Metadata
#Author Yehia Elghaly

import os,sys
from PIL import Image
from PIL.ExifTags import TAGS

photo = "DSCN0010.jpg"
info = Image.open(photo)

exif =  {}

for tag, value in info.getexif().items():
	if tag in TAGS:
		exif[TAGS[tag]] = value

print (exif)