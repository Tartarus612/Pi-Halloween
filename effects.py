# import the necessary packages
from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import numpy as np
import random

camera = PiCamera()
camera.resolution = (640, 480)
camera.framerate = 15
rawCapture = PiRGBArray(camera, size=(640, 480))

time.sleep(0.1)
camera.image_effect = "negative"
camera.iso = 800
bigTexture = cv2.imread('/home/pi/Halloween/texture.jpg')
y = 0
x = 0
#cv2.namedWindow("window", cv2.WND_PROP_FULLSCREEN)
#cv2.setWindowProperty("window",cv2.WND_PROP_FULLSCREEN,cv2.WINDOW_FULLSCREEN)

for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        # grab the raw NumPy array representing the image, then initialize the timestamp
        # and occupied/unoccupied text
        image = frame.array
        #if (random.randint(0, 1) == 0):
        #    x = x + 1
        #else:
        y = y + 1
        if(y > 2000):
            y = 0
        #if(x > 3000):
        #    x = 0
        texture = bigTexture[y:y+480, x:x+640]

 
        # show the frame
        cv2.imshow("Frame", cv2.addWeighted(image,0.6,texture,0.4,0))
        #cv2.imshow("window", cv2.addWeighted(image,0.6,texture,0.4,0))
        key = cv2.waitKey(1) & 0xFF
 
        # clear the stream in preparation for the next frame
        rawCapture.truncate(0)
 
        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
                break
