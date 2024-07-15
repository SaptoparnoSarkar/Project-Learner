import cv2
import numpy as np
import time 

#Capturing the Video Feed
capture = cv2.VideoCapture(0) 
#The argument 0 specifies the camera to use. In this case, 0 usually refers to the default camera, which is often the built-in webcam.

#Allowing the Camera to Load
time.sleep(2)
background = None

#Time to Capture the Background
for i in range(30): #Reads 30 frames from a video capture device.
    ret, background = capture.read()

#Fliping the Background
background = np.flip(background, axis=1)

while(capture.isOpened()):
    ret, frame = capture.read()

    if not ret:
        break
    #flip the frame
    frame = np.flip(frame, axis=1)
    #convert the frame into HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #To define our colour Range which is I chose as Blue
    heavy_blue = np.array([94,80,2])
    lighter_blue =np.array([126,255,255])

    #Mask for the blue colour
    mask1 = cv2.inRange(hsv, heavy_blue, lighter_blue)

    #Refining the Mask to remove artifacts
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3,3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3,3), np.uint8))

    #Creating an inverted mask to segment out the blue color from the frame
    mask2 = cv2.bitwise_not(mask1)

    # Segment the blue color out of the frame using bitwise and with the inverted mask
    res1 = cv2.bitwise_and(frame, frame, mask=mask2)

    #Combining the background and current Frame
    res2 = cv2.bitwise_and(background,background, mask=mask1)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("Invisible Cloak", final_output)

    #Break loop by pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Release the video capture and close windows 
capture.release()
cv2.destroyAllWindows()
