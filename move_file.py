# coding=utf-8

import re
import os
import time
import shutil
import sys

current_path = os.path.split(os.path.realpath(__file__))[0]

def touch_dir(path):
    if not os.path.exists(path):
        os.mkdir(path)

def get_filenames(path):
    names = []
    for (dirpath, dirnames, filenames) in os.walk(path):
        names.extend(filenames)

    # print(names)
    return names

def move(folder_name, number_of_part):
    dir = '%s/%s' % (current_path, folder_name)
    output_path = '%s/../%s_splited' % (dir, folder_name)
    touch_dir(output_path)
    loop = 1
    for filename in get_filenames(dir):
        if (number_of_part < loop):
            loop = 1
        copy_to = '%s/%d' % (output_path, loop)
        touch_dir(copy_to)
        item = "%s/%s" % (dir, filename)
        shutil.copy(item, copy_to)
        loop = loop + 1


if __name__=='__main__':
    #usage python3 move_file.py folder_name number_of_part
    move(sys.argv[1], int(sys.argv[2]))
