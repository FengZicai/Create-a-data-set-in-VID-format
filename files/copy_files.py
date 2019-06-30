import os
import numpy as np
import tqdm
import glob

output = '/media/fengzicai/study/vot-2019/data/'
path = '/home/fengzicai/Documents/vot-toolkit/vot/sequences/list.txt'
data = np.loadtxt(path, dtype='str')
for id in tqdm.tqdm(data):
    src_img_dir = "/home/fengzicai/Documents/vot-toolkit/vot/sequences/" + id + '/color'
    names = glob.glob(os.path.join(src_img_dir, '*'))
    for name in names:
        split = name.split('/')
        if not os.path.exists(output + split[-3] + '_' + split[-2] + '/'):
            os.mkdir(output + split[-3] + '_' + split[-2] + '/')
        os.system('cp '+name + ' ' + output + split[-3] + '_' + split[-2] + '/' + split[-1])
    src_img_dir = "/home/fengzicai/Documents/vot-toolkit/vot/sequences/" + id + '/depth'
    names = glob.glob(os.path.join(src_img_dir, '*'))
    for name in names:
        split = name.split('/')
        if not os.path.exists(output + split[-3] + '_' + split[-2] + '/'):
            os.mkdir(output + split[-3] + '_' + split[-2] + '/')
        os.system('cp ' + name + ' ' + output + split[-3] + '_' + split[-2] + '/' + split[-1])