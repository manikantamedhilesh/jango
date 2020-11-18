import cv2

video_path = ' PATH TO VIDEO'

cap = cv2.VideoCapture(video_path)  # Reading video
template = cv2.imread('PATH TO TEMPLATE IMAGE', 0) # Template image
method=cv2.TM_CCORR_NORMED # matching method
threshold=0.8 # threshold value
# count=0
while (True):

    ret, frame = cap.read()
    # count+=1
    try:
        # cv2.imwrite(
        #     '/home/akhil/workspace/projects/lennox/data/video_frames/autobrazer/' + 'frame_' + str(count) + '.jpg',
        #     frame)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        w, h = template.shape[::-1]

        res = cv2.matchTemplate(gray, template, method)




        # loc = np.where(res >= threshold)
        # print(loc[::-1])
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)

        # If the method is TM_SQDIFF or TM_SQDIFF_NORMED, take minimum
        if max_val>threshold:
            if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
                top_left = min_loc
            else:
                top_left = max_loc
            # top_left = min_loc
            bottom_right = (top_left[0] + w, top_left[1] + h)

            cv2.rectangle(frame, top_left, bottom_right, 255, 1)
            cv2.putText(frame, 'Slab Detected: ', (top_left[0], top_left[1] - 10),
                        cv2.FONT_HERSHEY_PLAIN, 1.0, (255, 255, 255))

            cv2.imshow('Test', frame)
    except:
        print('error')

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()