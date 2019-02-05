import os
import copy
import cv2
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

ROOT_PATH = "I:\programing\python\cascade\photo\\"
IN_JPG_PATH = "./photo/"
OUT_JPG_PATH = "./output/"

cascade_lst = [
    "haarcascade_frontalface_alt_tree",
    "haarcascade_frontalface_alt",
    "haarcascade_frontalface_alt2",
    "haarcascade_frontalface_default",
    ]

def getPictureFilePath(path):
    path_lst = []
    for filename in os.listdir(path):
        path_lst.append(path + filename)
    return path_lst

def writeImageFromCascade(path, cascade):
    # read image
    image_gs = cv2.imread(path)

    face_list = cascade.detectMultiScale(image_gs, scaleFactor=1.11, minNeighbors=3, minSize=(50,50))

    if len(face_list) == 0:
        return False

    saveFlg = False
    for rect in face_list:
        x = rect[0]
        y = rect[1]
        width = rect[2]
        height = rect[3]
        dst = image_gs[y:y+height, x:x+width]
        dst = cv2.resize(dst, (300, 300))
        save_path = OUT_JPG_PATH + '/' + os.path.basename(path)
        
        tmp_img = copy.deepcopy(image_gs)
        cv2.rectangle(tmp_img, (x, y), (x+width, y+height), (0, 0, 255), 1)
        cv2.imshow("img", tmp_img)
        key = cv2.waitKey(0)
        if key == 27:
            continue
        cv2.destroyAllWindows()

        # save
        a = cv2.imwrite(save_path, dst)
        saveFlg = True
        #plt.show(plt.imshow(np.asarray(Image.open(save_path))))

    return saveFlg


def trming():
    files = getPictureFilePath(ROOT_PATH)
    for cascade_path in cascade_lst:
        print(cascade_path)
        cascade = cv2.CascadeClassifier('./%s.xml' % cascade_path)
        for f in files:
            print(f)
            result = writeImageFromCascade(f, cascade)
            if result == True:
                files.remove(f)