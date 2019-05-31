# -*- coding:utf-8 -*-

from __future__ import print_function
import os, shutil
import pandas as pd
import csv
workspace = os.getcwd()
dataspace = '/home/smile/Desktop/'

import cv2
from lxml import objectify,etree
flagfile = dataspace+'nois/'
imgs_path = '/home/smile/Desktop/Faster-R-CNN-MXNet/data/Relationship-NonIs/'
csv_path = flagfile+'nois.csv'
xmls_path = flagfile+'xmls/'
def getxmls():
    assert os.path.exists(imgs_path)
    assert os.path.exists(csv_path)
    if not os.path.exists(xmls_path):   os.mkdir(xmls_path)
    imgs_file = os.listdir(imgs_path)
    with open(csv_path, 'r') as csvlines:
        for csvline in csvlines.readlines()[1:]:
        # csvline = '0000b86e2fd18333,Man,Coffee cup,0,0.42375,0,0.9962963,0.36,0.51625,0.5564815,0.8185185,holds\n'
            line = csvline.strip('\n').split(',')
            if line[0]+'.jpg' not in imgs_file:
                #print(imgs_file)
                continue
            img = cv2.imread(os.path.join(imgs_path, line[0]+'.jpg'))
            (width,height,dim) = img.shape
            E = objectify.ElementMaker(annotate=False)
            bbox1 = list(map(float, line[3:7]))
            bbox2 = list(map(float, line[7:11]))
            anno_tree = E.annotation(
                E.folder('VOC2007'),
                E.filename("%s.jpg" % line[0]),
                E.source(
                    E.database('The VOC2007 Database'),
                    E.annotation('PASCAL VOC2007'),
                    E.image('flickr'),
                    E.flickrid(341012865)
                ),
                E.owner(
            		E.flickrid('Fried Camels'),
            		E.name('Jinky the Fruit Bat')
            	),
                E.size(
                    E.width(width),
                    E.height(height),
                    E.depth(dim)
                ),
                E.segmented(0),
                # E.object(tree(E,line[1],line[3:7])),
                # E.object(tree(E,line[2],line[7:11])),
                E.object(
                    E.name(line[1]),
                    E.pose('Left'),
                    E.truncated(1),
                    E.difficult(0),
                    E.bndbox(
                            E.xmin(int(bbox1[0]*width)),
                            E.ymin(int(bbox1[2]*height)),
                            E.xmax(int(bbox1[1]*width)),
                            E.ymax(int(bbox1[3]*height))
                    ),
                ),
                E.object(
                    E.name(line[2]),
                    E.pose('Left'),
                    E.truncated(1),
                    E.difficult(0),
                    E.bndbox(
                            E.xmin(int(bbox2[0]*width)),
                            E.ymin(int(bbox2[2]*height)),
                            E.xmax(int(bbox2[1]*width)),
                            E.ymax(int(bbox2[3]*height))
                    ),
                ),
            )
            etree.ElementTree(anno_tree).write(os.path.join(xmls_path, "%s.xml" % line[0]), pretty_print=True)


if __name__ == '__main__':
    getxmls()
