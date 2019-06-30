# -*- coding: utf-8 -*-
import cv2
import glob
import numpy as np
import os

if __name__ == '__main__':
    input_path = '/media/fengzicai/study/Princeton2/data/'
    output_path = '/media/fengzicai/study/videos/'
    # dirs = np.loadtxt(input_path + 'list.txt', dtype='str').reshape(1, -1)
    dirs = os.listdir(input_path)
    for category in range(0, len(dirs)):
        category_path = input_path + '/' + dirs[category]
        picture_path = category_path # + 'color/'

        video_path = output_path + dirs[category] + '.avi'
        txt_path = '/media/fengzicai/study/Princeton2/txt/' + dirs[category] +'.txt'
        if 'depth' in picture_path:
            pictures = glob.glob(os.path.join(picture_path + '/*.png'))
        else:
            pictures = glob.glob(os.path.join(picture_path + '/*.JPEG'))
        pictures.sort(key=lambda x: int(os.path.basename(x).split('.')[0].split('-')[-1]))
        image = cv2.imread(pictures[0]).shape
        locations = np.loadtxt(txt_path, delimiter=',', dtype='float')

        fps = 30
        image_size = (image[1], image[0])
        fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
        videoWriter = cv2.VideoWriter(video_path, fourcc, fps, image_size)
        row = 0
        for picture in pictures:
            frame = cv2.imread(picture)
            if str(locations[row][0]) != 'NaN':
                location_row = int(locations[row][0])
                location_column = int(locations[row][1])
                width = int(locations[row][2]-locations[row][0])
                height = int(locations[row][3]-locations[row][1])
                cv2.rectangle(frame, (location_row, location_column),
                              (location_row + width, location_column + height), (0, 255, 0), 1)
            videoWriter.write(frame)
            row += 1

        videoWriter.release()
