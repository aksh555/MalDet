import subprocess
import scipy.misc
import os
import array
import glob
import numpy as np
import math
import random
from skimage import io


def generate_and_save_image(input_dir, output_dir, filename):
    out_file = os.path.splitext(os.path.basename(filename))[0] + '.png'
    out_file_full = output_dir + out_file
    input_file_path = filename
    print("out_file_full: ", out_file_full)
    f = open(input_file_path, 'rb')
    ln = os.path.getsize(input_file_path)  # length of file in bytes
    width = 256
    rem = ln % width
    a = array.array("B")  # uint8 array
    a.fromfile(f, ln - rem)
    f.close()
    g = np.reshape(a, (len(a) // width, width))
    g = np.uint8(g)
    io.imsave(out_file_full, g)  # save the image


def convert_bin_to_img(input_dir, output_dir):
    if not os.path.isdir(input_dir):
        print(input_dir, 'Input directory not found. Exiting.')
        exit(0)
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)
        print(input_dir)
    files = [f for f in glob.glob(
        input_dir + "*/*.exe", recursive=True)]  # use *.EXE as well
    print(len(files))
    count = 0
    for filename in files:
        generate_and_save_image(input_dir, output_dir, filename)
        count += 1
    print(f"Converted {count} files")

# Paths
convert_bin_to_img("./", './Mal test img/')
#convert_bin_to_img("./", './Mal train img/')
