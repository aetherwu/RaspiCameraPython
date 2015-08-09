#!/usr/bin/env python

import time
import picamera

with picamera.PiCamera() as camera:
    camera.resolution = (1280, 770)
    camera.start_preview()
    camera.exposure_compensation = 2
    # Give the camera some time to adjust to conditions
    time.sleep(2)

    for i, filename in enumerate(camera.capture_continuous('/home/pi/pic/img{timestamp:_%Y%m%d_%H%M%s}.jpg')):
        #save file
        print('Captured image %s' % filename)
	time.sleep(20)
