# -*- coding: utf-8 -*-
import cv2
import glob
import numpy as np
from tqdm import tqdm


colors = []
for pixel in range(256):
    colors.append((np.random.randint(256), np.random.randint(256), np.random.randint(256)))


if __name__ == '__main__':
    input_path = 'E:/VOT-RGBD2019/'
    output_path = 'C:/Users/Lenovo/Desktop/Videos/'
    dirs = np.loadtxt(input_path + 'list.txt', dtype='str').reshape(1, -1)
    for category in range(dirs.size):
        category_path = input_path + dirs[0][category] + '/'
        picture_path = category_path + 'color/'

        video_path = output_path + dirs[0][category] + '.avi'
        txt_path = category_path + 'groundtruth.txt'

        pictures = glob.glob(picture_path + '*.jpg')
        image = cv2.imread(pictures[0]).shape
        locations = np.loadtxt(txt_path, delimiter=',', dtype='float')

        fps = 30
        image_size = (image[1] * 2, image[0] * 2)
        fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
        videoWriter = cv2.VideoWriter(video_path, fourcc, fps, image_size)
        row = 0
        for picture in tqdm(pictures):
            piece = cv2.imread(picture)
            size = piece.shape
            frame = np.zeros((size[0] * 2, size[1] * 2, size[2]), np.uint8)
            frame_tmp = np.zeros(size, np.uint8)
            if str(locations[row][0]) != 'nan':
                location_row = int(locations[row][0])
                location_column = int(locations[row][1])
                width = int(locations[row][2])
                height = int(locations[row][3])
                cv2.rectangle(piece, (location_row, location_column),
                              (location_row + width, location_column + height), (0, 255, 0), 1)

            frame[0:size[0], 0:size[1], :] = piece
            frame[(size[0]):(size[0] * 2), (size[1]):(size[1] * 2), :] = piece

            depth = picture.replace('color', 'depth').replace('jpg', 'png')
            depth_piece = cv2.imread(depth, 0)

            for i in range(256):
                frame_tmp[depth_piece == i] = colors[i]

            frame[size[0]:, 0:size[1], :] = frame_tmp
            frame[0:size[0], size[1]:, :] = frame_tmp

            videoWriter.write(frame)
            row += 1

        videoWriter.release()
