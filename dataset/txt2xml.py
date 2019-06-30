# ! /usr/bin/python
# -*- coding:UTF-8 -*-
import os, sys
import glob
from PIL import Image
import numpy as np
import tqdm

CLASSES = ('ignore', 'pedestrian', 'people', 'bicycle', 'car',
           'van', 'truck', 'tricycle', 'awning-tricycle', 'bus',
           'motor', 'other')
label = {'ignore': 0, 'pedestrian': 1, 'people': 2, 'bicycle': 3, 'car': 4,
         'van': 5, 'truck': 6, 'tricycle': 7, 'awning-tricycle': 8, 'bus': 9,
         'motor': 10, 'other': 11}


def xml(img_dir, id, data):
    im = Image.open(img_dir)
    width, height = im.size  # xml文件中需要width和height信息，这里通过Image库计算出来
    split = img_dir.split('/')
    if not os.path.exists(src_xml_dir):
        os.mkdir(src_xml_dir)
    xml_dir = src_xml_dir + id +'.xml'
    xml_file = open((xml_dir), 'w')
    xml_file.write('<annotation>\n')
    xml_file.write('    <folder>VOC2007</folder>\n')
    xml_file.write('    <filename>' + str(id) + '.jpg' + '</filename>\n')
    xml_file.write('    <size>\n')
    xml_file.write('        <width>' + str(width) + '</width>\n')
    xml_file.write('        <height>' + str(height) + '</height>\n')
    xml_file.write('        <depth>3</depth>\n')
    xml_file.write('    </size>\n')

    for i,_ in enumerate(data):
        spt = data[i, 0: 4]
        name = data[i, 4]
        xml_file.write('    <object>\n')
        xml_file.write('        <trackid>'+ str(i) + '</trackid>\n')
        xml_file.write('        <name>' + CLASSES[name] + '</name>\n')  # 类别名称,可以固定下来
        xml_file.write('        <bndbox>\n')
        xml_file.write('            <xmin>' + str(int(spt[0])) + '</xmin>\n')
        xml_file.write('            <ymin>' + str(int(spt[1])) + '</ymin>\n')
        xml_file.write('            <xmax>' + str(int(spt[0] + spt[2] + 1)) + '</xmax>\n')
        xml_file.write('            <ymax>' + str(int(spt[1] + spt[3] + 1)) + '</ymax>\n')
        xml_file.write('        </bndbox>\n')
        xml_file.write('    </object>\n')

    xml_file.write('</annotation>')


if __name__ == '__main__':

    list_path = '/home/fengzicai/Documents/predict/val500/list.txt'
    lists = np.loadtxt(list_path, dtype='str')
    for id in tqdm.tqdm(lists):

        src_xml_dir = "/home/fengzicai/Documents/predict/val500/xml/"
        src_img_dir = "/home/fengzicai/Documents/predict/val500/images/" + id + '.jpg'
        src_txt_dir = "/home/fengzicai/Documents/predict/val500/annotations/" + id + '.txt'

        # if not os.path.isdir(src_img_dir):
        #     raise Exception('%s 不是路径' % src_img_dir)
        # if not os.path.isdir(src_xml_dir):
        #     raise Exception('%s 不是路径' % src_xml_dir)
        data = np.loadtxt(src_txt_dir, delimiter=',', dtype=int).reshape(-1, 5)
        xml(src_img_dir, id, data)
