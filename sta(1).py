import os
import numpy as np
import tqdm
import glob
import pandas as pd
import cv2
number = []
path = '/media/fengzicai/study/Princeton/data'
data = glob.glob(os.path.join(path, '*'))
for path2 in tqdm.tqdm(data):
    # path2 = '/home/fengzicai/Documents/vot2019/sequences/' + id + '/depth'
    png_dir = glob.glob(os.path.join(path2, '*00000.png'))
    picture = cv2.imread(png_dir, 0)
    picarray = np.array(picture).reshape(1, -1)

    pixel = set(picarray[0])
    number.append(pixel)
test = pd.DataFrame(index=data, data= number)
test.to_csv('/media/fengzicai/study/Princeton/data/pixel.csv')

