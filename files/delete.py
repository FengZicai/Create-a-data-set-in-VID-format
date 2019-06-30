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
# src_img_dir = "/media/fengzicai/study/Princeton2/data"
# # 图像的 ground truth 的 txt 文件存放位置
src_csv_dir = "/media/fengzicai/study/vot-2019/deted"
# 生成xml文件存放位置
# src_xml_dir = "/media/fengzicai/study/Princeton2/xml"
#
csvs = glob(os.path.join(src_csv_dir, '*.csv'))
for csv in csvs:
#
#     # picture_path = np.loadtxt(csv, delimiter=',', dtype='str')
#     for i in range(1,len(picture_path)):
#
#     # os.path.join(src_img_dir,os.path.basename(txt).split('.')[0])
#     # if 'depth' in picture_path:
#     #     picture = glob(os.path.join(picture_path,'*.png'))
#     # else:
#     #     picture = glob(os.path.join(picture_path, '*.JPEG'))
    picture.sort(key=lambda x: int(os.path.basename(x).split('.')[0].split('-')[-1]))
#     # data = np.loadtxt(txt, delimiter=',', dtype='str')
#     # for i in range(len(data)):
#     #     if 'NaN' in data[i,:]:
#
    os.remove(picture_path[i, 1])



    # data = np.loadtxt(txt, delimiter=',', dtype='str')
    # # pass
    # index = set(np.where(data == 'NaN')[0])
    # data = np.delete(data,list(index),0)
    # data = np.float_(data)
    # # with open('/home/fengzicai/Desktop/new_ex_occ4_rgb.txt', 'r+') as new_file:
    # #     new_file.seek(0)
    # #     new_file.truncate()
    # #     new_file.write(str(data))
    # if data.shape[1] == 5:
    #     np.savetxt(txt, data, fmt="%.2f,%.2f,%.2f,%.2f,%.2f", delimiter=",")
    # else:
    #     np.savetxt(txt, data, fmt="%.2f,%.2f,%.2f,%.2f", delimiter=",")




# numbers =[]
# path = '/media/fengzicai/study/Princeton1/data'
# cls = np.array(os.listdir(path))
# cls = cls.reshape(-1,1)
# for i,_ in enumerate(cls):
#     if '_depth' in cls[i,0]:
#         numbers.append(str(cls[i,0]).replace('_depth',''))
# numbers = np.array(numbers).reshape(-1,1)
# np.savetxt('/media/fengzicai/FT/1.txt', numbers,fmt='%s', delimiter="\n")
