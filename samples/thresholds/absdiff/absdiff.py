import cv2
import numpy as np

# Globals
# -------
window_name = "Webcam"
quit_key = ord('q')
reset_key = ord('r')
cam = cv2.VideoCapture(0)

# Processing
# ----------
# Declare windows
cv2.namedWindow(window_name + " Processed Output", cv2.WINDOW_AUTOSIZE)

# Take background sample
_, bg = cam.read()
camHeight = bg.shape[0]
camWidth = bg.shape[1]
print("Feed dimensions: {}*{}".format(camWidth, camHeight))

# cv2.getWindowProperty() will return -1 when the window is closed
while cv2.getWindowProperty(window_name + " Processed Output", 0) >= 0:
    _, frame = cam.read()

    # Take absolute difference
    diff = cv2.absdiff(bg, frame)

    # Take threshold of absolute difference
    diffthresh = cv2.threshold(diff, 75, 255, cv2.THRESH_BINARY)[1]

    # Take b/w version of absolute difference
    diffgray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    diffthreshgray = cv2.threshold(diffgray, 75, 255, cv2.THRESH_BINARY)[1]
    diffthreshgray = cv2.cvtColor(diffthreshgray, cv2.COLOR_GRAY2BGR)

    # Combine original, absolute difference, and threshold of into a single window
    frame_rs = cv2.resize(frame, None, fx=0.5, fy=0.5)
    diff_rs = cv2.resize(diff, None, fx=0.5, fy=0.5)
    diffthresh_rs = cv2.resize(diffthresh, None, fx=0.5, fy=0.5)
    diffthreshgray_rs = cv2.resize(diffthreshgray, None, fx=0.5, fy=0.5)
    hstack_1 = np.hstack((frame_rs, diff_rs))
    hstack_2 = np.hstack((diffthresh_rs, diffthreshgray_rs)) # cv2.copyMakeBorder(diffthresh_rs, bottom=0, top=0, left=0, right=diffthresh_rs.shape[1], borderType=0)
    vstack = np.vstack((hstack_1, hstack_2))
    cv2.imshow(window_name + " Processed Output", vstack)
    
    keyIn = cv2.waitKey(1) & 0xFF
    if keyIn == quit_key:
        break
    elif keyIn == reset_key:
        _, bg = cam.read()

# Cleanup
# -------
cv2.destroyWindow(window_name)