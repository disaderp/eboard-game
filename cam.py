import cv2
import numpy as np

def checkDice():
	min_threshold = 10                      # these values are used to filter our detector.
	max_threshold = 200                     # they can be tweaked depending on the camera distance, camera angle, ...
	min_area = 100                          # ... focus, brightness, etc.
	min_circularity = .3
	min_inertia_ratio = .5
	 
	cap = cv2.VideoCapture(0)               # '0' is the webcam's ID. usually it is 0 or 1. 'cap' is the video object.
	cap.set(15, -4)                         # '15' references video's brightness. '-4' sets the brightness.

	if not cap.isOpened():
		print("not opened")
		exit()
		
	counter = 0                             # script will use a counter to handle FPS.
	readings = [0, 0]                       # lists are used to track the number of pips.
	display = [0, 0]
	
	while True:
		if counter >= 90000:                # set maximum sizes for variables and lists to save memory.
			counter = 0
			readings = [0, 0]
			display = [0, 0]

		ret, im = cap.read()                                    # 'im' will be a frame from the video.
		
		params = cv2.SimpleBlobDetector_Params()                # declare filter parameters.
		params.filterByArea = True
		params.filterByCircularity = True
		params.filterByInertia = True
		params.minThreshold = min_threshold
		params.maxThreshold = max_threshold
		params.minArea = min_area
		params.minCircularity = min_circularity
		params.minInertiaRatio = min_inertia_ratio

		detector = cv2.SimpleBlobDetector_create(params)        # create a blob detector object.

		keypoints = detector.detect(im)                         # keypoints is a list containing the detected blobs.
		reading = len(keypoints)                                # 'reading' counts the number of keypoints (pips).

		if counter % 10 == 0:                                   # enter this block every X frames.
			readings.append(reading)                            # note the reading from this frame.

			if readings[-1] == readings[-2] == readings[-3]:    # if the last 3 readings are the same...
				display.append(readings[-1])                    # ... then we have a valid reading.
	 
			# if the most recent valid reading has changed, and it's something other than zero, then print it.
			if display[-1] != display[-2] and display[-1] != 0:
				return str(display[-1])
				
		counter += 1