import cv2

# Globals
# -------
window_name = "Webcam"
quit_key = ord('q')
cam = cv2.VideoCapture(0)

# Processing
# ----------
# Declare the window
cv2.namedWindow(window_name, cv2.WINDOW_AUTOSIZE)

# cv2.getWindowProperty() will return -1 when the window is closed
while cv2.getWindowProperty(window_name, 0) >= 0:
    _, frame = cam.read()
    cv2.imshow(window_name, frame)

    keyIn = cv2.waitKey(1) & 0xFF

# Cleanup
# -------
cv2.destroyWindow(window_name)