import cv2
import numpy as np
import os
from skimage.measure import structural_similarity as ssim
import sys
import urllib

##usage: classifyBasic.py <url of candidate image>

url = sys.argv[1]
#print "the url is" + url
full_name='candidate.jpg'
os.chdir("/home/ubuntu/data/test")
urllib.urlretrieve(url, os.path.join(os.getcwd(), full_name))
imgc = cv2.imread('candidate.jpg',0)
candidate_resized = cv2.resize(imgc, (640,480))

m1=0
m2=0
s1=0
s2=0
m3=0
s3=0

flooddir = "/home/ubuntu/data/flood_images_labelled"
downlinedir = "/home/ubuntu/data/downedLines_images_labelled"
treedir = "/home/ubuntu/data/fallentree_images_labelled"


os.chdir(flooddir)
filenum = 0
for filename in os.listdir(flooddir):
 img = cv2.imread(filename,0)
 m1 += mse(candidate_resized,img)
 s1 += ssim(candidate_resized,img)
 filenum += 1
 
m1 = m1/filenum
s1 = s1/filenum
filenum = 0

os.chdir(downlinedir)
for filename in os.listdir(downlinedir):
 img = cv2.imread(filename,0)
 m2 += mse(candidate_resized,img)
 s2 += ssim(candidate_resized,img)
 filenum += 1

m2 = m2/filenum
s2 = s2/filenum
filenum = 0

os.chdir(treedir)
for filename in os.listdir(treedir):
 img = cv2.imread(filename,0)
 m3 += mse(candidate_resized,img)
 s3 += ssim(candidate_resized,img)
 filenum += 1

m3 = m3/filenum
s3 = s3/filenum

#print s1
#print s2
#print s3

if s1==s2 and s1==s3:
 print "undetermined"

if s1>s2 and s1>s3:
 print "flood"

if s2>s1 and s2>s3:
 print "downed power line"

if s3>s1 and s3>s2:
 print "fallen tree"

