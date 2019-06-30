import os
import numpy as np
import tqdm
import glob
import pandas as pd
import cv2


def statistic_picture_pixels():
    pixels = []
    video_sequence_path = '/media/fengzicai/study/Princeton/data'
    data = glob.glob(os.path.join(video_sequence_path, '*'))
    for picture_path in tqdm.tqdm(data):
        picture = cv2.imread(picture_path, 0)
        picarray = np.array(picture).reshape(1, -1)
        pixel = set(picarray[0])
        pixels.append(pixel)
    test = pd.DataFrame(index=data, data=pixels)
    test.to_csv('/media/fengzicai/study/Princeton/data/pixel.csv')


def statistic_picture_numbers():
    number = []
    path = '/home/fengzicai/Documents/vot2019/sequences/list.txt'
    data = np.loadtxt(path, dtype='str')
    for id in tqdm.tqdm(data):
        path2 = '/home/fengzicai/Documents/vot2019/sequences/' + id + '/color'
        list = glob.glob(os.path.join(path2, '*.jpg'))
        number.append(len(list))

    test = pd.DataFrame(index=data, data=number)
    test.to_csv('/home/fengzicai/Documents/vot2019/number.csv')

