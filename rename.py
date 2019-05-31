import subprocess
import os
import glob
import numpy as np
def cfg(path_cfg,file):
    with open(path_cfg,'r+') as cfgfile:
        cfgfile.write('terr_pointClouds_filepath='+file[-16:])

#pname = r"wine CSFDemo.exe"

path = '/media/fengzicai/study/Princeton2/xml/'
# file_list = glob.glob(os.path.join(path, "*.txt"))
file_list = os.listdir(path)
# path_cfg = '/home/smile/Documents/dfc2019-master/data/CSFDemo(V2.0)/params.cfg'
# files = os.listdir(path)
# sys.path.append(path)


for file in file_list:
# path='/media/fengzicai/study/'
# file = 'child_no1_depth'
    # data = np.loadtxt(file, delimiter=',', dtype='f8')
    # np.savetxt(file, data, fmt='%.2f %.2f %.2f %d %d')
    # cfg(path_cfg, file+'\n')
    #p = subprocess.call(pname, shell=True)
    # p = subprocess.run(["wine", "CSFDemo.exe"])
    if 'depth' in file:
        png_paths = glob.glob(os.path.join(path,file+'/*.xml'))
        png_paths.sort(key=lambda x: int(os.path.basename(x).split('.')[0].split('-')[-1]))
        for i,png_path in enumerate(png_paths):
            os.rename(png_path, os.path.join(os.path.split(png_path)[0], '0000' + format(str(i), '0>3s') + '.xml'))
        # os.rename(file, file.replace(' (copy)','_rgb'))
    else:
        # os.rename(file, file[:-5].replace(' (copy)', '_rgb'))
        JPEG_paths = glob.glob(os.path.join(path, file + '/*.xml'))
        JPEG_paths.sort(key=lambda x: int(os.path.basename(x).split('.')[0].split('-')[-1]))
        for i, JPEG_path in enumerate(JPEG_paths):
            os.rename(JPEG_path, os.path.join(os.path.split(JPEG_path)[0], '0000' + format(str(i), '0>3s') + '.xml'))
    # os.rename(path + '/non-ground.txt',path + '/' + file[-15:-7] + 'non-ground.txt')
    print('ground.txt', '======>','ground.txt')
