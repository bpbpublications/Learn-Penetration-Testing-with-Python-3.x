#!/usr/bin/env python3
# Extract Geolocation from Images
# Author Yehia Elghaly

import exifread

photo=exifread.process_file(open('001.jpg','rb'))
time=photo['Image DateTime']
print(time)

latitude=photo['GPS GPSLatitude']
print(latitude)

longitude=photo['GPS GPSLongitude']
print(longitude)