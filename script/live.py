# This script will detect faces via your webcam.
# Tested with OpenCV3
import os
import random
import threading

import cv2
import  uuid
import time
from camapp.models import Ipaddress


def run_live():
    ipadd = Ipaddress.objects.filter(group_id="22")
    Ip_add=0
    for IP in ipadd:
        Ip_add = IP.ip
    cap = cv2.VideoCapture(0)
    i=1
    # cascPath = sys.argv[1]
    # faceCascade = cv2.CascadeClassifier(cascPath)

    # Create the haar cascade
    faceCascade = cv2.CascadeClassifier(os.path.dirname(os.path.realpath(__file__))+"/haarcascade_frontalface_default.xml")
    flagtime = time.time()
    t1=threading.currentThread()
    while getattr(t1,"flag",True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        # Our operations on the frame come here
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Detect faces in the image
        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(30, 30),
        )

        # Draw a rectangle around the faces

        if len(faces) >= 0 and flagtime + 2.5 < time.time():
            cv2.imwrite(os.path.dirname(os.path.realpath(__file__))+"/store/" + str(i) + ".jpg", frame)
            i=i+1
            flagtime = time.time()

        # Display the resulting frame
        # cv2.imshow('frame', frame)
        # if cv2.waitKey(1) & 0xFF == ord('q'):
        #     break

    # When everything done, release the capture
    cap.release()
    cv2.destroyAllWindows()

if __name__ == '__main__':
    # test1.py executed as script
    # do something
    run_live()
