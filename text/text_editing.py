import os
import numpy as np
import tqdm
import glob
import pandas as pd
from shutil import copyfile

def deletelines(file):
    with open(file, 'r') as old_file:
        with open(file, 'r+') as new_file:
            del_line =0
            current_line = 0

            # 定位到需要删除的行
            while current_line < (del_line - 1):
                old_file.readline()
                current_line += 1

            # 当前光标在被删除行的行首，记录该位置
            seek_point = old_file.tell()

            # 设置光标位置
            new_file.seek(seek_point, 0)

            # 读需要删除的行，光标移到下一行行首
            old_file.readline()

            # 被删除行的下一行读给 next_line
            next_line = old_file.readline()

            # 连续覆盖剩余行，后面所有行上移一行
            while next_line:
                new_file.write(next_line)
                next_line = old_file.readline()

            # 写完最后一行后截断文件，因为删除操作，文件整体少了一行，原文件最后一行需要去掉
            new_file.truncate()

txtfile = ''
deletelines(txtfile)
