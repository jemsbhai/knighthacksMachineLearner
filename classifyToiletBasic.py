import cv2
import numpy as np
import os
from skimage.measure import structural_similarity as ssim
import sys
import urllib

##usage: classifyToiletBasic.py <url of candidate image>

url = sys.argv[1]
#print "the url is" + url
full_name='candidate.jpg'
os.chdir("/home/ubuntu/toiletdata/test")
urllib.urlretrieve(url, os.path.join(os.getcwd(), full_name))
imgc = cv2.imread('candidate.jpg',0)
candidate_resized = cv2.resize(imgc, (640,480))

m1=0
m2=0
s1=0
s2=0
m3=0
s3=0
m4 = 0
s4 = 0
max_similarity = 0
similarity_index = 0

notoiletdir = "/home/ubuntu/toiletdata/no_toilet"
cleantoiletdir = "/home/ubuntu/toiletdata/clean_toilet"
dirtytoiletdir = "/home/ubuntu/toiletdata/dirty_toilet"
urinaldir = "/home/ubuntu/toiletdata/urinal"


os.chdir(notoiletdir)
filenum = 0
for filename in os.listdir(notoiletdir):
 img = cv2.imread(filename,0)
 m1 += mse(candidate_resized,img)
 s1 += ssim(candidate_resized,img)
 filenum += 1
 
m1 = m1/filenum
s1 = s1/filenum
if s1>max_similarity:
 max_similarity = s1
 similarity_index = 1

filenum = 0

os.chdir(cleantoiletdir)
for filename in os.listdir(cleantoiletdir):
 img = cv2.imread(filename,0)
 m2 += mse(candidate_resized,img)
 s2 += ssim(candidate_resized,img)
 filenum += 1

m2 = m2/filenum
s2 = s2/filenum
if s2>max_similarity:
 max_similarity = s2
 similarity_index = 2

filenum = 0

os.chdir(dirtytoiletdir)
for filename in os.listdir(dirtytoiletdir):
 img = cv2.imread(filename,0)
 m3 += mse(candidate_resized,img)
 s3 += ssim(candidate_resized,img)
 filenum += 1

m3 = m3/filenum
s3 = s3/filenum
if s3>max_similarity:
 max_similarity = s3
 similarity_index = 3

filenum = 0 

os.chdir(urinaldir)
for filename in os.listdir(urinaldir):
 img = cv2.imread(filename,0)
 m4 += mse(candidate_resized,img)
 s4 += ssim(candidate_resized,img)
 filenum += 1

m4 = m4/filenum
s4 = s4/filenum

if s4>max_similarity:
 max_similarity = s4
 similarity_index = 4
 
#print s1
#print s2
#print s3

if max_similarity=0:
 label = "undetermined"

if similarity_index == 1:
 label = "no toilet"

if similarity_index == 2:
 label = "clean toilet"

if similarity_index == 3:
 label = "dirty toilet"

if similarity_index == 4:
 label = "urinal"

print label 