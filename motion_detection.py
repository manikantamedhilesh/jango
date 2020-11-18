# Python program to implement
# Webcam Motion Detector

# importing OpenCV, time,os and Pandas library
import cv2, time, pandas
import os
from datetime import datetime





def motion_detection_1(directory,parent_dir):
    """
     directory:parameter (str )
         direactory folder name
     parent_dir :parameter (str)
         full path of the directory

     """

    # Capturing video
    video = cv2.VideoCapture(0)
    count = 0
    check, frame = video.read()
    static_back=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Taking first frame of the video

    # Creating destination file path
    path = os.path.join(parent_dir, directory) # str:
    # Create the directory
    try:
        os.makedirs(path)
    except:
        print('directory already exists')


    # Infinite while loop to treat stack of image as video
    while True:
        # Reading frame(image) from video
        check, frame = video.read()

        # Initializing motion = 0(no motion)
        motion = 0
        # print(frame)
        if count % 30 == 0:  # Updating static background after every 30 frames
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            # In first iteration we assign the value
            # of static_back to our first frame
            if static_back is None:
                static_back = gray
                continue

        if count % 60 == 0:  # Taking one frame for every 60 frames
            print(count)
            # Converting color image to gray_scale image
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            # Converting gray scale image to GaussianBlur
            # so that change can be find easily
            gray = cv2.GaussianBlur(gray, (21, 21), 0)

            # Difference between static background
            # and current frame(which is GaussianBlur)
            diff_frame = cv2.absdiff(static_back, gray)
            static_back = None
            # If change in between static background and
            # current frame is greater than 30 it will show white color(255)
            thresh_frame = cv2.threshold(diff_frame, 30, 255, cv2.THRESH_BINARY)[1]
            thresh_frame = cv2.dilate(thresh_frame, None, iterations=2)

            # Finding contour of moving object
            cnts, _ = cv2.findContours(thresh_frame.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for contour in cnts:
                if cv2.contourArea(contour) < 50000:
                    continue
                motion = 1

                # Saving frame into the specified folder when motion detected
                cv2.imwrite(path+'/image_'+str(count)+'.jpg',frame)

        count += 1
        key = cv2.waitKey(1)
        #         # if q entered whole process will stop
        if key == ord('q'):
            break



    video.release()

    # Destroying all the windows
    cv2.destroyAllWindows()

parent_dir='/home/akhil/workspace/projects/lennox'
directory='detected_plates'
motion_detection_1(directory,parent_dir)
