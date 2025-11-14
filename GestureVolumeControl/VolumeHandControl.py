import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# Camera size
wCam, hCam = 640, 480

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

pTime = 0

# FIXED: Correct Mediapipe init! detectionCon must be keyword, not positional
detector = htm.handDetector(detectionCon=0.7, maxHands=1)

# Setup pycaw audio control
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

minVol, maxVol = volume.GetVolumeRange()[:2]
volBar = 400
volPer = 0

while True:
    success, img = cap.read()
    if not success:
        continue

    # Detect hand
    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=False)   # FIXED

    if len(lmList) != 0:
        # Landmark 4 = Thumb tip, Landmark 8 = Index fingertip
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        # Draw circles and line
        cv2.circle(img, (x1, y1), 15, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 15, (255, 0, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)
        cv2.circle(img, (cx, cy), 12, (255, 0, 255), cv2.FILLED)

        # Distance between fingers
        length = math.hypot(x2 - x1, y2 - y1)

        # Convert hand distance to volume
        vol = np.interp(length, [40, 250], [minVol, maxVol])
        volBar = np.interp(length, [40, 250], [400, 150])
        volPer = np.interp(length, [40, 250], [0, 100])

        # Set volume
        volume.SetMasterVolumeLevel(vol, None)

        # If fingers very close → green circle
        if length < 40:
            cv2.circle(img, (cx, cy), 12, (0, 255, 0), cv2.FILLED)

    # Draw volume bar
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)}%', (40, 430), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)

    # FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40, 70), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    cv2.waitKey(1)
