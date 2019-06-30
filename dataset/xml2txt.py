import os
import sys
import xml.etree.ElementTree as ET
import glob

global label



def xml_to_txt(indir,outdir,label):

    os.chdir(indir)
    annotations = os.listdir('.')
    annotations = glob.glob(str(annotations)+'*.xml')



    for i, file in enumerate(annotations):

        file_save = file.split('.')[0]+'.txt'
        file_txt=os.path.join(outdir,file_save)
        f_w = open(file_txt,'w')

        # actual parsing
        in_file = open(file)
        tree=ET.parse(in_file)
        root = tree.getroot()

        for obj in root.iter('object'):
                current = list()
                name = obj.find('name').text

                xmlbox = obj.find('bndbox')
                xn = xmlbox.find('xmin').text
                xx = xmlbox.find('xmax').text
                yn = xmlbox.find('ymin').text
                yx = xmlbox.find('ymax').text
                #print xn
                f_w.write(xn+','+yn+','+xx+','+yx+',0,')
                f_w.write(str(labels[name])+',0,0' +'\n')

indir='/home/fengzicai/Documents/test-challenge/xml'   #xml目录
outdir='/home/fengzicai/Documents/test-challenge/txt'  #txt目录

labels = {'ignore': 0, 'pedestrian': 1, 'people': 2, 'bicycle': 3, 'car': 4,
         'van': 5, 'truck': 6, 'tricycle': 7, 'awningtricycle': 8, 'bus': 9,
         'motor': 10, 'other': 11}
xml_to_txt(indir, outdir, labels)
