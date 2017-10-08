import cv2
import numpy as np
import os
import sys

##usage: preprocessBasic.py <path of labelled images directory>

imagepath = sys.argv[1]

os.chdir(imagepath)
for filename in os.listdir(imagepath):
  if filename.endswith(".JPG") or filename.endswith(".jpg"):
     img = cv2.imread(filename,0)
     gray_resized = cv2.resize(img, (640, 480))
     fileout = "grayResized"+filename
     cv2.imwrite(fileout,gray_resized)

print "done"
