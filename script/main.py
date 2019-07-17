import glob
import threading
from . import live
from . import test1
import os
import shutil
import time

def start():
    t=threading.currentThread()
    for image in glob.glob(os.path.dirname(os.path.realpath(__file__))+"/store/*.jpg"):
        length = len(image)
        len_s = len(os.path.dirname(os.path.realpath(__file__))+"/store/")
        img = image[len_s:length]
        os.rename(image, os.path.dirname(os.path.realpath(__file__))+"/repo/"+img)

    for image in glob.glob(os.path.dirname(os.path.realpath(__file__))+"/test/*.jpg"):
        length = len(image)
        len_s = len(os.path.dirname(os.path.realpath(__file__))+"/test/")
        img = image[len_s:length]
        os.rename(image, os.path.dirname(os.path.realpath(__file__))+"/repo/"+img)

    cur = time.time()
    flag_test = 0

    t1 = threading.Thread(target=live.run_live)
    t1.flag = True
    t1.start()
    v = 1

    while getattr(t,"flag",True):

        images = glob.glob(os.path.dirname(os.path.realpath(__file__))+"/store/*.jpg")
        no_of_images_store = len(images)


        if (flag_test == 0 and cur + 13 < time.time() and no_of_images_store >= 7):
            i = 0
            # for image in glob.glob(os.path.dirname(os.path.realpath(__file__))+"/store/*.jpg"):
            while (i <= 5):

                image = os.path.dirname(os.path.realpath(__file__))+"/store/" + str(v) + ".jpg"
                length = len(image)
                len_s = len(os.path.dirname(os.path.realpath(__file__))+"/store/")
                img = image[len_s:length]
                os.rename(image, os.path.dirname(os.path.realpath(__file__))+"/test/" + img)
                v = v + 1
                i = i + 1
            flag_test = 1
            v = v - 6


        if (flag_test == 1 and getattr(t,"flag",True)):
            test1.run_test1()
            i = 0
            # for image in glob.glob(os.path.dirname(os.path.realpath(__file__))+"/test/*.jpg"):
            while (i <= 5 and getattr(t,"flag",True)):

                image = os.path.dirname(os.path.realpath(__file__))+"/test/" + str(v) + ".jpg"
                length = len(image)
                len_s = len(os.path.dirname(os.path.realpath(__file__))+"/test/")
                # length = len(os.path.dirname(os.path.realpath(__file__))+"/test/"+str(j1)+".jpg")
                img = image[len_s:length]
                os.rename(image, os.path.dirname(os.path.realpath(__file__))+"/repo/" + img)
                v=v+1
                i = i + 1
            flag_test = 2

        images = glob.glob(os.path.dirname(os.path.realpath(__file__))+"/store/*.jpg")
        no_of_images_store = len(images)
        if (flag_test == 2 and getattr(t,"flag",True)  and no_of_images_store>=7):
            i = 0
            # for image in glob.glob(os.path.dirname(os.path.realpath(__file__))+"/store/*.jpg"):
            while (i <= 5 and getattr(t,"flag",True)):

                image = os.path.dirname(os.path.realpath(__file__))+"/store/" + str(v) + ".jpg"
                length = len(image)
                len_s = len(os.path.dirname(os.path.realpath(__file__))+"/store/")
                img = image[len_s:length]
                os.rename(image, os.path.dirname(os.path.realpath(__file__))+"/test/" + img)
                v=v+1
                i = i + 1
            flag_test = 1
            v = v - 6
    t1.flag=False
    t1.join()


if __name__ == '__main__':
    start()

