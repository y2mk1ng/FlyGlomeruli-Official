#!/usr/bin/env python
# coding: utf-8
print('Code by Yanling Guo (aka Asuka M). ')

## This is how I move the files into the subfolders based on the numbers in the file names.

from PIL import Image
import os, sys, shutil, pandas
p = 'E:/Glo@BF_class20190617/Glo@BF' # Where all the files are
os.chdir(p)
os.getcwd()

# go to your "from" folder
path_1 = p + '/2DX_predict/2DX@July26-6_L@BF123' # The folder where you will operate on the files
os.chdir(path_1)
ext = '.png'

# to move files from the file name number (front) of less than 10
for a in range(0, 10):
    for b in range (1, 10):
        if not os.path.isdir(path_1 + '/' + str(a)):
            os.mkdir(path_1 + '/' + str(a))
        filename_1 = 'X00' + str(a) + '_July27-2_L_Raw_Predict@UNet_Glomerulus2DX@July26-6_L@BF123-0' + str(b) + ext
        path_original_1 = path_1 + '/' + filename_1
        path_new_1 = path_1 + '/' + str(a) + '/' + filename_1
        shutil.copy(path_original_1, path_new_1)

for a in range(0, 10):
    for b in range (10, 11):
        if not os.path.isdir(path_1 + '/' + str(a)):
            os.mkdir(path_1 + '/' + str(a))
        filename_1 = 'X00' + str(a) + '_July27-2_L_Raw_Predict@UNet_Glomerulus2DX@July26-6_L@BF123-' + str(b) + ext
        path_original_1 = path_1 + '/' + filename_1
        path_new_1 = path_1 + '/' + str(a) + '/' + filename_1
        shutil.copy(path_original_1, path_new_1)


# to move files from the file name number (front) of more than 10 but less than 100

print(os.getcwd())
for a in range(10, 100):
    for b in range (1, 10):
        if not os.path.isdir(path_1 + '/' + str(a)):
            os.mkdir(path_1 + '/' + str(a))        
        filename_10 = 'X0' + str(a) + '_July27-2_L_Raw_Predict@UNet_Glomerulus2DX@July26-6_L@BF123-0' + str(b) + ext
        path_original_10 = path_1 + '/' + filename_10
        path_new_10 = path_1 + '/' + str(a) + '/' + filename_10        
        shutil.copy(path_original_10, path_new_10)        

for a in range(10, 100):
    for b in range (10, 11):
        if not os.path.isdir(path_1 + '/' + str(a)):
            os.mkdir(path_1 + '/' + str(a))        
        filename_10 = 'X0' + str(a) + '_July27-2_L_Raw_Predict@UNet_Glomerulus2DX@July26-6_L@BF123-' + str(b) + ext
        path_original_10 = path_1 + '/' + filename_10
        path_new_10 = path_1 + '/' + str(a) + '/' + filename_10        
        shutil.copy(path_original_10, path_new_10)


# to move files from the file name number (front) of more than 100

for a in range(100, 512):
    for b in range (1, 10):
        if not os.path.isdir(path_1 + '/' + str(a)):
            os.mkdir(path_1 + '/' + str(a))        
        filename_10 = 'X' + str(a) + '_July27-2_L_Raw_Predict@UNet_Glomerulus2DX@July26-6_L@BF123-0' + str(b) + ext
        path_original_10 = path_1 + '/' + filename_10
        path_new_10 = path_1 + '/' + str(a) + '/' + filename_10        
        shutil.copy(path_original_10, path_new_10)
for a in range(100, 512):
    for b in range (10, 11):
        if not os.path.isdir(path_1 + '/' + str(a)):
            os.mkdir(path_1 + '/' + str(a))        
        filename_10 = 'X' + str(a) + '_July27-2_L_Raw_Predict@UNet_Glomerulus2DX@July26-6_L@BF123-' + str(b) + ext
        path_original_10 = path_1 + '/' + filename_10
        path_new_10 = path_1 + '/' + str(a) + '/' + filename_10        
        shutil.copy(path_original_10, path_new_10)

## Please just change the path names when you want to work from another folder.

