import os
import numpy as np
from glob import glob


path = '/home/fengzicai/Documents/predict/val500/annotations'
save_path = '/home/fengzicai/Documents/predict/val500/list.txt'


def create_lists(path,save_path):
    lists = []
    files = glob(os.path.join(path, '*txt'))
    for file in files:
        lists.append(os.path.basename(file).split('.')[0])
    lists = np.asarray(lists).reshape(-1, 1)
    np.savetxt(save_path, lists, fmt='%s')


create_lists(path, save_path)
