####################################################################################3
# Usage : python Dlib_coil_detection.py --images '/content/drive/My Drive/Lennox/Images/originalImages/' 
#                                        --Model '/content/drive/My Drive/Lennox/Coildetector.dat'
#
#
#



import cv2
import numpy as np
# from google.colab.patches import cv2_imshow
from matplotlib import pyplot as plt
from imutils.video import VideoStream
import numpy as np
import argparse
import imutils
import time
import dlib
import os

def getDlibDetectionWindow(detector,image,i):

  detections = detector(resized)
  for k, d in enumerate(detections):

    print("Detection {}: Left: {} Top: {} Right: {} Bottom: {}".format(k, d.left(), d.top(), d.right(), d.bottom()))
    x,y,w,h = d.left(), d.top(), d.right(), d.bottom()
    # print('Dlib Detections-',x,y,w,h)
    cv2.rectangle(resized, (x, y), (w,h), [0,255,255], 2)
    # cv2_imshow(resized)
    
    filename=directory+'/testing'+i+'.png'
    print('result filename',filename)
    cv2.imwrite(filename,resized)
        
  return x,y,w,h


print('Imported the required files-')

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--Model", required=True,help="path to input Model")
ap.add_argument("-i", "--images", required=True,help="path to input images")
args = vars(ap.parse_args())
inputModelfile=args["Model"]

directory=os.getcwd()
print('Model is'+directory+inputModelfile)
print(args["images"])
imagesList=os.listdir(args["images"])
print(imagesList)

#load Dlib Detector

detector = dlib.simple_object_detector(inputModelfile)

for i in imagesList:
  X,Y,W,H=0,0,0,0 
  filename=directory+'/originalImages/'+i
  print(filename)
  image = cv2.imread(filename)
  print('Original Dimensions : ',image.shape)
 
  scale_percent = 40 # percent of original size
  width = int(image.shape[1] * scale_percent / 100)
  height = int(image.shape[0] * scale_percent / 100)
  dim = (width, height)
  # resize image
  resized = cv2.resize(image, dim, interpolation = cv2.INTER_AREA)
  print('Resized Dimensions : ',resized.shape)
  X,Y,W,H = getDlibDetectionWindow(detector,resized,i)
  print('Result of Dlib',X,Y,W,H)

  # gray_img = cv2.cvtColor(resized,cv2.COLOR_BGR2GRAY)

  # imgmask = np.zeros(gray_img.shape[:2], np.uint8)
  # imgmask[Y:H, X:W] =255

  # cv2.imwrite(directory+"/mask.jpg",imgmask)

  # gray_crop=gray_img[Y:H, X:W]
  # cv2.imwrite(directory+"/gray_crop.jpg",gray_crop)

  # masked_img = cv2.bitwise_or(gray_img,gray_img,mask = imgmask)

  # cv2.imwrite(directory+"/masked_img.jpg",masked_img)
  # print("After saving masked img"+directory+"/masked_img.jpg")

