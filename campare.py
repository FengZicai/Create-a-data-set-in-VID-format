import numpy as np
import os
import glob
txt_dir = '/media/fengzicai/study/ExampleResult/ExampleResult'
img_dir = '/media/fengzicai/study/Folder'

# txts = glob.glob(os.path.join(txt_dir, '*.txt'))
doc = '/media/fengzicai/study/Untitled Document'
txts = np.loadtxt(doc, dtype='str')
# txts = os.listdir(img_dir)
for i in range(len(txts)):
    path = os.path.join(txt_dir, txts[i]+'.txt')
    data = np.loadtxt(path, delimiter=',', dtype='str')
    if '0' not in data[:, 0:4]:
        print(txts[i])
