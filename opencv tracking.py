import cv2 as cv
import numpy as np

# Initialize the webcam
cap = cv.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read(a
    if not ret:
        break

    # Convert BGR to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    # define range of orange color in HSV
    lower_orange = np.array([10, 100, 100])
    upper_orange = np.array([25, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_orange, upper_orange)

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(hsv, hsv, mask= mask)

    # Find contours in the mask
    contours, _ = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    
    # If any contours are found, draw a bounding box around the largest one
    if contours:
        # for contour in contours:
        #     # Get the bounding box coordinates
        #     x, y, w, h = cv.boundingRect(contour)
            
        #     # Draw the bounding box on the original frame
        #     if contour[0,0,0] * contour[0,0,1] > 200000:
        #         cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
        
        # Find the largest contour by area
        largest_contour = max(contours, key=cv.contourArea)
        
        # Get the bounding box coordinates
        x, y, w, h = cv.boundingRect(largest_contour)
        
        # Draw the bounding box on the original frame
        cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        
            

    # Display the resulting frame
    cv.imshow('Frame', frame)
    cv.imshow('Mask', mask)
    # cv.imshow('res',res)

    # Break the loop if the user presses 'ESC'
    if cv.waitKey(1) & 0xFF == 27:
        break

# When everything is done, release the capture and close windows
cap.release()
cv.destroyAllWindows()
