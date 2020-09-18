#!/usr/bin/env python
# coding: utf-8

from PIL import Image
import os

os.chdir('your/path') # where your file is
im1 = Image.open(r'filename.jpg') # open your file
im1.save(r'filename.png')
