############################################################################################
#   Usage :python templateMatchLennox.py --inputImg 962.jpg --template False
#    --inputImg = image for which template needs to be matched
#
#
#
#



import argparse
import imutils
import cv2
from google.colab.patches import cv2_imshow
import matplotlib.pyplot as plt
import numpy as np
import os



def getTemplateWindow(template,frame):
  
  templateGray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
  w, h = templateGray.shape[::-1]
 
  gray_frame = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  res = cv2.matchTemplate(gray_frame,templateGray, cv2.TM_SQDIFF_NORMED)
  min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
  min_thresh = (min_val + 1e-6) * 1.0
  match_locations = np.where(res<=min_thresh)
  w, h = templateGray.shape[::-1]
  for (x, y) in zip(match_locations[1], match_locations[0]):
        print('Dimensions----->',x,y,w,h)   
        cv2.rectangle(frame, (x, y), (x+w, y+h), [0,255,255], 2)
        # cv2.rectangle(resized, (x, y), (x+w, y+h), [0,255,255], 2)
        cv2.imwrite(directory+"/result.jpg",frame)
        print("Result Saved",directory+"/result.jpg")
        # cv2_imshow(frame)
        X,Y,W,H=x,y,x+w,y+h

  return X,Y,W,H


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--inputImg", required=True,help="path to input image")
ap.add_argument("-t", "--template", required=True,help="path to input image")
args = vars(ap.parse_args())
directory=os.getcwd()

print('Imported the required files-')
inputImagefile=args["inputImg"]
print(inputImagefile)
image = cv2.imread(inputImagefile)
# image = cv2.imread('962.jpg')
print('Image Dimensions : ',image.shape)

plt.imshow(image)
scale_percent = 40 # percent of original size
width = int(image.shape[1] * scale_percent / 100)
height = int(image.shape[0] * scale_percent / 100)
dim = (width, height)
# resize image
resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
print('Resized Dimensions : ',resized.shape)

#check this flag if using for the first time
template_reqd=args["template"]
# template_reqd=True
print('Template Reqd',template_reqd)

print('Working Directory',directory)
X,Y,W,H=0,0,0,0
if template_reqd==True:

  crop=resized[150:300,0:580]
  plt.imshow(crop)
  cv2.imwrite(directory+"/template.jpg",crop)
  print("After saving template"+directory+"template.jpg")   
  # directory="C:\\Users\\user\\Documents\\object_tracking\\CoilTemplateMatch\\"
  print(os.listdir(directory)) 
  # print('Successfully saved')

template = cv2.imread("template.jpg")
print('Template Dimensions : ',template.shape)

X,Y,W,H=getTemplateWindow(template,resized)
gray_img = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)

imgmask = np.zeros(gray_img.shape[:2], np.uint8)
imgmask[Y:H, X:W] =255
cv2.imwrite(directory+"/mask.jpg",imgmask)

gray_crop=gray_img[Y:H, X:W]
cv2.imwrite(directory+"/gray_crop.jpg",gray_crop)



masked_img = cv2.bitwise_or(gray_img,gray_img,mask = imgmask)
# cv2_imshow(imgmask)
cv2.imwrite(directory+"/masked_img.jpg",masked_img)
print("After saving masked img"+directory+"masked_img.jpg") 







