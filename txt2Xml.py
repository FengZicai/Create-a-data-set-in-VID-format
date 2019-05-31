# -*- coding: utf-8 -*-
import copy
from lxml.etree import Element, SubElement, tostring, ElementTree
from lxml import etree, objectify
import cv2
import os
import numpy as np


#  默认每个图片序列文件中都有一个Report.info文件
def txt2xml(img_path, txt_path, xml_save_path):
    assert os.path.exists(img_path)
    assert os.path.exists(txt_path)
    if not os.path.exists(xml_save_path):
        os.makedirs(xml_save_path)
    img_files = os.listdir(img_path)
    train_txt = os.listdir(txt_path)
    txt = []
    class_list = []
    for txt_name in train_txt:
        with open(os.path.join(txt_path, txt_name), 'r') as f:
            obj = f.readlines()
            txt.append(obj)
            class_list.append(txt_name.split('-')[0])

    img = cv2.imread(os.path.join(img_path, img_files[0]))
    width = img.shape[1]
    height = img.shape[0]
    dim = img.shape[2]

    for i in range(1, len(img_files)):
        E = objectify.ElementMaker(annotate=False)
        anno_tree = E.annotation(
            E.folder(img_path),
            E.filename("%06d.tiff" % i),
            E.source(
                E.database('IPIU'),
            ),
            E.size(
                E.width(width),
                E.height(height),
                E.depth(dim)
            ),
            E.segmented(0),
        )
        # tree.parse(os.path.join(xml_save_path, '%06d.xml' % i))

        for lable, bbox in zip(class_list, txt):
            bbox = list(map(int, bbox[i-1].strip().split(',')))
            if bbox[0] == -1:
                continue
            E2 = objectify.ElementMaker(annotate=False)
            anno_tree2 = E2.object(
                E.name(lable),
                E.bndbox(
                    E.xmin(bbox[0]),
                    E.ymin(bbox[1]),
                    E.xmax(bbox[0] + bbox[2]),
                    E.ymax(bbox[1] + bbox[3])
                ),
                E.difficult(0)
            )
            anno_tree.append(anno_tree2)

        etree.ElementTree(anno_tree).write(os.path.join(xml_save_path, "%06d.xml" % i), pretty_print=True)
        print('\r%s save %06d.xml' % (img_path, i), end='')


if __name__ == '__main__':
    img_path = '/home/smile/Desktop/fashuju06'
    txt_path = 'test_result/data3'
    xml_save_path = 'xml/data3'
    txt2xml(img_path, txt_path, xml_save_path)
