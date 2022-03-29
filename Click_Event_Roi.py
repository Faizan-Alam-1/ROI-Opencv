import cv2
cam = cv2.VideoCapture(0)
ev = 0


color = (0, 285, 0)
thikness = 3


def left_click(event, xPos, yPos, flags, param):
    global ev
    global tup1
    global tup2

    if event == cv2.EVENT_LBUTTONDOWN:
        print(event)
        ev = event
        tup1 = (xPos, yPos)
    if event == cv2.EVENT_LBUTTONUP:
        print(event)
        ev = event
        tup2 = (xPos, yPos)
    if event == cv2.EVENT_RBUTTONUP:
        print(event)
        ev = event


cv2.namedWindow("Click Me")
cv2.setMouseCallback("Click Me", left_click)
while True:
    ignore, frame = cam.read()

    if ev == 4:
        frameROI = frame[tup1[1]:tup2[1], tup1[0]: tup2[0]]
        cv2.imshow("ROI", frameROI)
        rec = cv2.rectangle(frame, tup1, tup2, (color), thikness)
    if ev == 5:
        cv2.destroyWindow("ROI")
        ev = 0

    cv2.imshow("Click Me", frame)

    if cv2.waitKey(30) & 0xff == ord('q'):
        break

cam.release()
