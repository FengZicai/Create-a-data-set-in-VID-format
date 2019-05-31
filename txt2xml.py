# ! /usr/bin/python
# -*- coding:UTF-8 -*-
import os, sys
import glob
from PIL import Image
import numpy as np
import tqdm
import pandas as pd



#
# type = '.png'
# def is_file(in_path):
#     if not os.path.isfile(in_path):
#         return False
#     if in_path is not str and not in_path.endswith(type): #深度一次，ＲＧＢ一次
#         return False
#     return True


def xml(img_dir,spt):
    im = Image.open(img_dir)
    width, height = im.size  # xml文件中需要width和height信息，这里通过Image库计算出来
    split = img_dir.split('/')
    if not os.path.exists(src_xml_dir + split[-3]+'_'+split[-2]+'/'):
        os.mkdir(src_xml_dir + split[-3]+'_'+split[-2]+'/')
    xml_dir = src_xml_dir + split[-3]+'_'+split[-2]+'/'+split[-1]
    if 'png' in img_dir:
        xml_dir = xml_dir.replace('png','xml')
    else:
        xml_dir = xml_dir.replace('JPEG','xml')
    xml_file = open((xml_dir), 'w')
    xml_file.write('<annotation>\n')
    xml_file.write('    <folder>VOC2007</folder>\n')
    xml_file.write('    <filename>' + str(os.path.split(xml_dir)[1].split('.')[0]) + '</filename>\n')
    xml_file.write('    <size>\n')
    xml_file.write('        <width>' + str(width) + '</width>\n')
    xml_file.write('        <height>' + str(height) + '</height>\n')
    xml_file.write('        <depth>3</depth>\n')
    xml_file.write('    </size>\n')
    xml_file.write('    <object>\n')
    xml_file.write('        <trackid>0</trackid>\n')
    xml_file.write('        <name>' + str('child_no1') + '</name>\n')  # 类别名称,可以固定下来
    xml_file.write('        <bndbox>\n')
    xml_file.write('            <xmin>' + str(int(spt[0])) + '</xmin>\n')
    xml_file.write('            <ymin>' + str(int(spt[1])) + '</ymin>\n')
    xml_file.write('            <xmax>' + str(int(spt[0] + spt[2] + 1)) + '</xmax>\n')
    xml_file.write('            <ymax>' + str(int(spt[1] + spt[3] + 1)) + '</ymax>\n')
    xml_file.write('        </bndbox>\n')
    xml_file.write('    </object>\n')

    xml_file.write('</annotation>')


def xml_batch(in_dir, out_dir, data_dir):
    """
    批量转换PGM文件
    :param in_dir: pgm文件夹路径
    :param out_dir: 输出文件夹路径
    """
    if not os.path.isdir(in_dir):
        raise Exception('%s 不是路径' % in_dir)
    if not os.path.isdir(out_dir):
        raise Exception('%s 不是路径' % out_dir)
    i = 0

    file_list = os.listdir(in_dir) #有嚴重的問題，讀入的圖片循序是亂序的，沒有解決．
    for file_name in file_list:
        file_path = os.path.join(in_dir, file_name)
        # 若为pgm文件路径，那么将其进行格式转换
        if is_file(file_path):
            data = np.loadtxt(data_dir + '.txt', delimiter=',', dtype='float')
            xml(in_dir, out_dir, os.path.splitext(file_name)[0], data[i, :])
            i+=1
        # 若为目录，则新建结果文件目录，递归处理
        elif os.path.isdir(file_path):
            file_out_dir = os.path.join(out_dir, file_name)
            if not os.path.exists(file_out_dir):
                os.mkdir(file_out_dir)
            txt_dir = os.path.join(data_dir, file_name)
            xml_batch(file_path, file_out_dir, txt_dir)
        else:
            pass
    # i = 0
    # print(i)
    print(file_name)
    print('batch operation over')



# for id in tqdm.tqdm(data):
#     path2 = '/home/fengzicai/Documents/vot2019/sequences/' + id + '/color'
#     list = glob.glob(os.path.join(path2, '*.jpg'))
#     number.append(len(list))

if __name__ == '__main__':
    path = '/home/fengzicai/Documents/vot-toolkit/vot/sequences/list.txt'
    data = np.loadtxt(path, dtype='str')
    for id in tqdm.tqdm(data):
        src_xml_dir = "/media/fengzicai/study/vot-2019/"
        src_img_dir = "/home/fengzicai/Documents/vot-toolkit/vot/sequences/" + id
        src_txt_dir = "/home/fengzicai/Documents/vot-toolkit/vot/sequences/" + id + '/groundtruth.txt'
        if not os.path.isdir(src_img_dir):
            raise Exception('%s 不是路径' % src_img_dir)
        if not os.path.isdir(src_xml_dir):
            raise Exception('%s 不是路径' % src_xml_dir)

        file_list = os.listdir(src_img_dir)  # 有嚴重的問題，讀入的圖片循序是亂序的，沒有解決．
        for file_name in file_list:
            i = 0
            number = []
            file_path = os.path.join(src_img_dir, file_name)
            if os.path.isdir(file_path):
                # 若为pgm文件路径，那么将其进行格式转换
                if 'depth' in file_path:
                    files = glob.glob(os.path.join(file_path, '*.png'))
                    files.sort(key=lambda x: int(os.path.basename(x).split('.')[0]))
                    for i, file in enumerate(files):
                        # data_dir = file.replace('data','txt')
                        # data_dir = os.path.split(data_dir)[0] + '.txt'
                        data = np.loadtxt(src_txt_dir, delimiter=',', dtype='float')
                        if 'nan' not in str(data[i, 0]):
                            xml(file, data[i, :])
                        else:
                            number.append(file)
                            test = pd.DataFrame(data=number)
                            csvsplit = file.split('/')

                            test.to_csv('/media/fengzicai/study/deted/' + csvsplit[-3] + '_' + csvsplit[-2]  + '.csv')

                else:
                    files = glob.glob(os.path.join(file_path, '*.jpg'))
                    files.sort(key=lambda x: int(os.path.basename(x).split('.')[0]))
                    for i, file in enumerate(files):
                        # data_dir = file.replace('data', 'txt')
                        # data_dir = os.path.split(data_dir)[0] + '.txt'
                        data = np.loadtxt(src_txt_dir, delimiter=',', dtype='float')
                        if 'nan' not in str(data[i, 0]):
                            xml(file, data[i, :])
                        else:
                            number.append(file)
                            test = pd.DataFrame(data=number)
                            csvsplit = file.split('/')
                            test.to_csv('/media/fengzicai/study/deted/' + csvsplit[-3] + '_' + csvsplit[-2] + '.csv')



