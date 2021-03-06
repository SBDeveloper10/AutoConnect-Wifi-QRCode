import os
from pyzbar.pyzbar import decode
import cv2


cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)


s = True
while s:
    s, img = cap.read()
    db = decode(img)
    for data in db:
        id, password = data.data.decode("utf-8").split("/")
        os.system(f'cmd /c "netsh wlan set hostednetwork mode=allow ssid={id} key={password}"')
        os.system(f'cmd /c "netsh wlan connect ssid={id} name={id}"')
        s = False
    cv2.imshow("Result", img)
    cv2.waitKey(1)
