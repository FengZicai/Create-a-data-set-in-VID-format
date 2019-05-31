# -*- coding: utf-8 -*-
from __future__ import print_function

import cv2
import time
import os
import operator
import numpy as np
import argparse
from PIL import Image
from glob import glob
src_img_dir = "/media/fengzicai/study/Princeton2/data"
# 图像的 ground truth 的 txt 文件存放位置
src_txt_dir = "/media/fengzicai/study/Princeton2/txt"
# 生成xml文件存放位置  
src_xml_dir = "/media/fengzicai/study/Princeton2/xml"

txts = glob(os.path.join(src_txt_dir, '*.txt'))
for txt in txts:
    # picture_path = os.path.join(src_img_dir,os.path.basename(txt).split('.')[0])
    # if 'depth' in picture_path:
    #     picture = glob(os.path.join(picture_path,'*.png'))
    # else:
    #     picture = glob(os.path.join(picture_path, '*.JPEG'))
    # picture.sort(key=lambda x: int(os.path.basename(x).split('.')[0].split('-')[-1]))
    # data = np.loadtxt(txt, delimiter=',', dtype='str')
    # for i in range(len(data)):
    #     if 'NaN' in data[i,:]:
    #         os.remove(picture[i])



    data = np.loadtxt(txt, delimiter=',', dtype='str')
    # pass
    index = set(np.where(data == 'NaN')[0])
    data = np.delete(data,list(index),0)
    data = np.float_(data)
    # with open('/home/fengzicai/Desktop/new_ex_occ4_rgb.txt', 'r+') as new_file:
    #     new_file.seek(0)
    #     new_file.truncate()
    #     new_file.write(str(data))
    if data.shape[1] == 5:
        np.savetxt(txt, data, fmt="%.2f,%.2f,%.2f,%.2f,%.2f", delimiter=",")
    else:
        np.savetxt(txt, data, fmt="%.2f,%.2f,%.2f,%.2f", delimiter=",")


