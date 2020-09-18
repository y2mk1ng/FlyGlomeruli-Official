#!/usr/bin/env python
# coding: utf-8

from PIL import Image
import os

os.chdir('your/path')
im1 = Image.open(r'filename.jpg')
im1.save(r'filename.png')

