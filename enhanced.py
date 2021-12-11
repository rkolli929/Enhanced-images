import os
import cv2 as cv
import matplotlib.pyplot as plt
mask = cv.imread("sample_data/edge/4.jpg",0)
img2 = cv.imread("sample_data/original/0004.jpg")
mask_inv = cv.bitwise_not(mask)
img2_fg = cv.bitwise_or(img2,img2,mask = mask_inv)
plt.imshow(img2_fg)

edge = os.listdir("sample_data/edge") 
edge = sorted(edge)
print(edge)
orig = os.listdir("sample_data/original") 
orig = sorted(orig)
print(orig)
k=0
for f, b in zip(edge, orig):
 mask = cv.imread('sample_data/edge/'+f,0)
 print("sample_data/"+f)
 img2 = cv.imread('sample_data/original/'+b)
 print("sample_data/"+b)
 mask_inv = cv.bitwise_not(mask)
 img2_fg = cv.bitwise_or(img2,img2,mask = mask_inv)
 plt.imshow(img2_fg)
 cv.imwrite("sample_data/enhanced/"+str(k)+'.jpg', img2_fg)
 k = k+1
