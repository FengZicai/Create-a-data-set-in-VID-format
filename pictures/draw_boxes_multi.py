import cv2
import os
import numpy as np


CLASSES = ('ignore', 'pedestrian', 'people', 'bicycle', 'car',
           'van', 'truck', 'tricycle', 'awning-tricycle', 'bus',
           'motor', 'other')

# txt_dir = '/home/tfboys/datasets/VIS_balance400/VisDrone2019-DET-val/annotations/'
txt_dir = '/home/fengzicai/Documents/predict/val_400_100_100_(1)/annotations/'
img_dir = '/home/fengzicai/Documents/predict/val_400_100_100_(1)/images/'
output_dir = '/home/fengzicai/Documents/predict/val_400_100_100_(1)/picture/'
for file in sorted(os.listdir(txt_dir)):
    print(file)
    txt_file = open(txt_dir+file)
    img = cv2.imread(img_dir+file[:-4]+'.jpg')
    for linea in txt_file.readlines():
        linea=linea.split(",")
        ltx = int(linea[0].split('.')[0])
        lty = int(linea[1].split('.')[0])
        rbx = int(linea[2].split('.')[0])+ltx
        rby = int(linea[3].split('.')[0])+lty
        #score = linea[4]
        # num = int(linea[4])
        # print (CLASSES[num])
        # if float(linea[4])>0.4:
        cv2.rectangle(img, (int(ltx), int(lty)), (int(rbx), int(rby)), (0, 255, 0), 2)
        #cv2.rectangle(img,(int(ltx),int(lty)-15),(int(ltx)+100,int(lty)-0),(255,255,255),2)
        # cv2.putText(img, str(CLASSES[num]), (int(linea[0]), int(linea[1])), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)
    txt_file.close()
    # cv2.imshow('a.jpg',img)
    cv2.imwrite(output_dir+file[:-4]+'.jpg', img)

'''
    cv2.rectangle(img,(int(ltx),int(lty)),(int(rbx),int(rby)),(0,255,0),2)
    cv2.rectangle(img,(int(ltx),int(lty)-15),(int(ltx)+100,int(lty)-0),(255,255,255),2)
    cv2.putText(img, linea[1], (int(linea[2]), int(linea[3])), cv2.FONT_HERSHEY_DUPLEX, 0.6, (0, 0, 0), 1)
'''
