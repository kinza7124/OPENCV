import cv2
import time
import numpy as np
import HandTrackingModule as htm
import math
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

################################
wCam, hCam = 640, 480
################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(detectionCon=0.7, maxHands=1)

# Audio controller
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))

volRange = volume.GetVolumeRange()
minVol, maxVol = volRange[0], volRange[1]

vol = 0
volBar = 400
volPer = 0

colorVol = (255, 0, 0)

while True:
    success, img = cap.read()
    if not success:
        continue

    img = detector.findHands(img)
    lmList, bbox = detector.findPosition(img, draw=True)

    if len(lmList) != 0 and bbox != []:

        # Calculate hand bounding area
        area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100

        # Filter hand area
        if 250 < area < 2000:

            # Distance between thumb tip (4) and index tip (8)
            length, img, lineInfo = detector.findDistance(4, 8, img)

            # Convert length → volume %
            volBar = np.interp(length, [40, 180], [400, 150])
            volPer = np.interp(length, [40, 180], [0, 100])

            # Smoothing
            smoothness = 5
            volPer = smoothness * round(volPer / smoothness)

            # Detect finger states
            fingers = detector.fingersUp()

            # Pinky down means adjust volume
            if fingers[4] == 0:
                volume.SetMasterVolumeLevelScalar(volPer / 100, None)
                cv2.circle(img, (lineInfo[4], lineInfo[5]), 12, (0, 255, 0), cv2.FILLED)
                colorVol = (0, 255, 0)
            else:
                colorVol = (255, 0, 0)

    # Draw volume bar
    cv2.rectangle(img, (50, 150), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (85, 400), (255, 0, 0), cv2.FILLED)

    cv2.putText(img, f'{int(volPer)} %', (40, 450),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cVol = int(volume.GetMasterVolumeLevelScalar() * 100)
    cv2.putText(img, f'Vol Set: {cVol}', (350, 50),
                cv2.FONT_HERSHEY_COMPLEX, 1, colorVol, 3)

    # FPS
    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (40, 70),
                cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 3)

    cv2.imshow("Img", img)
    cv2.waitKey(1)
