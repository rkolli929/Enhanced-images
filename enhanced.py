import os
import cv2 as cv
import matplotlib.pyplot as plt
'''
mask = cv.imread("Sample/edge/4.jpg",0)
img2 = cv.imread("Sample/original/0004.jpg")
mask_inv = cv.bitwise_not(mask)
img2_fg = cv.bitwise_or(img2,img2,mask = mask_inv)
plt.imshow(img2_fg)
'''
edge = os.listdir("Sample/edge") 
edge = sorted(edge)
print(edge)
orig = os.listdir("Sample/original") 
orig = sorted(orig)
print(orig)
k=0
for f, b in zip(edge, orig):
 mask = cv.imread('Sample/edge/'+f,0)
 img2 = cv.imread('Sample/original/'+b)
 mask_inv = cv.bitwise_not(mask)
 img2_fg = cv.bitwise_or(img2,img2,mask = mask_inv)
 #plt.imshow(img2_fg)
 cv.imwrite("Sample/enhanced_images/"+str(k)+'.jpg', img2_fg)
 k = k+1
