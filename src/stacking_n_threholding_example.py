#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This is the total code for the Antennal Lobe image segmentation using the image stacking method
# packed on Aug 12, 2020
from PIL import Image
import os, sys, shutil, pandas
import numpy
p = 'E:/Glo@BF_class20190617/Glo@BF' ## where all the files are
os.chdir(p)
path_1 = p + '/2DY_predict/2DY@July27-2_R@BF123456'
os.chdir(path_1)
ext = '.png'
os.getcwd()
def movefile():
    for a in range(0, 10):
        for b in range (1, 10):
            if not os.path.isdir(path_2 + '/' + str(a)):
                os.mkdir(path_2 + '/' + str(a))
            filename_1 = 'X00' + str(a) + '_July27-2_L_Raw_Predict@UNet_Glomerulus2DX@July26-6_L@BF1234-0' + str(b) + ext
            path_original_1 = path_2 + '/' + filename_1
            path_new_1 = path_2 + '/' + str(a) + '/' + filename_1
            shutil.copy(path_original_1, path_new_1)
    for a in range(0, 10):
        for b in range (10, 11):
            if not os.path.isdir(path_2 + '/' + str(a)):
                os.mkdir(path_2 + '/' + str(a))
            filename_1 = 'X00' + str(a) + '_July27-2_L_Raw_Predict@UNet_Glomerulus2DX@July26-6_L@BF1234-' + str(b) + ext
            path_original_1 = path_2 + '/' + filename_1
            path_new_1 = path_2 + '/' + str(a) + '/' + filename_1
            shutil.copy(path_original_1, path_new_1)
    for a in range(10, 100):
        for b in range (1, 10):
            if not os.path.isdir(path_2 + '/' + str(a)):
                os.mkdir(path_2 + '/' + str(a))        
            filename_10 = 'X0' + str(a) + '_July27-2_L_Raw_Predict@UNet_Glomerulus2DX@July26-6_L@BF1234-0' + str(b) + ext
            path_original_10 = path_2 + '/' + filename_10
            path_new_10 = path_2 + '/' + str(a) + '/' + filename_10        
            shutil.copy(path_original_10, path_new_10)
    for a in range(10, 100):
        for b in range (10, 11):
            if not os.path.isdir(path_2 + '/' + str(a)):
                os.mkdir(path_2 + '/' + str(a))        
            filename_10 = 'X0' + str(a) + '_July27-2_L_Raw_Predict@UNet_Glomerulus2DX@July26-6_L@BF1234-' + str(b) + ext
            path_original_10 = path_2 + '/' + filename_10
            path_new_10 = path_2 + '/' + str(a) + '/' + filename_10        
            shutil.copy(path_original_10, path_new_10)
    for a in range(100, 512):
        for b in range (1, 10):
            if not os.path.isdir(path_2 + '/' + str(a)):
                os.mkdir(path_2 + '/' + str(a))        
            filename_10 = 'X' + str(a) + '_July27-2_L_Raw_Predict@UNet_Glomerulus2DX@July26-6_L@BF1234-0' + str(b) + ext
            path_original_10 = path_2 + '/' + filename_10
            path_new_10 = path_2 + '/' + str(a) + '/' + filename_10        
            shutil.copy(path_original_10, path_new_10)
    for a in range(100, 512):
        for b in range (10, 11):
            if not os.path.isdir(path_2 + '/' + str(a)):
                os.mkdir(path_2 + '/' + str(a))        
            filename_10 = 'X' + str(a) + '_July27-2_L_Raw_Predict@UNet_Glomerulus2DX@July26-6_L@BF1234-' + str(b) + ext
            path_original_10 = path_2 + '/' + filename_10
            path_new_10 = path_2 + '/' + str(a) + '/' + filename_10        
            shutil.copy(path_original_10, path_new_10)
def stack_addtion_and_thresholds():
    for foldername in range(10, 78):
        path = p2 +'/' + str(foldername)
        print(path)
        im_9 = numpy.array(Image.open(path + '/Z' + str(foldername) + '_July27-2_L_Raw_Predict@UNet_Glomerulus2DZ@July27-2_R@BF123456-09.png'))
        im_10 = numpy.array(Image.open(path + '/Z' + str(foldername) + '_July27-2_L_Raw_Predict@UNet_Glomerulus2DZ@July27-2_R@BF123456-10.png'))
        im_9_10 = Image.fromarray(im_9 + im_10)
        im_9_10.save(path + '/pix_add9-10data.png')
        for a in range (1, 5):
            num_odd = 2 * a - 1
            num_even = 2 * a
            open_file_odd = Image.open(path + '/Z' + str(foldername) +'_July27-2_L_Raw_Predict@UNet_Glomerulus2DZ@July27-2_R@BF123456-0' + str(num_odd) + ext)
            open_file_even = Image.open(path + '/Z' + str(foldername) +'_July27-2_L_Raw_Predict@UNet_Glomerulus2DZ@July27-2_R@BF123456-0' + str(num_even) + ext)
            pix_odd = numpy.array(open_file_odd)
            pix_even = numpy.array(open_file_even)
            pix_add = pix_odd + pix_even
            print(pix_add)
            pandas.DataFrame(pix_add).to_csv(path + '/pix_add' + str(num_odd) + '-' + str(num_even) + 'data.csv')
            im_add = Image.fromarray(pix_add)
            im_add.save(path + '/pix_add' + str(num_odd) + '-' + str(num_even) + 'data.png')
            im_open = Image.open(path + '/pix_add' + str(num_odd) + '-' + str(num_even) + 'data.png')
            im_np = numpy.array(im_open)
            im_np += im_np
            im_ave = im_np / 10
            new_im_np = Image.fromarray(im_ave)
            new_im_np = new_im_np.convert("L")
            new_im_np.save(path + '/average.png')
            pandas.DataFrame(im_ave).to_csv(path + '/average.csv')
            # make thresholds
            im_threshold = im_ave
            im_threshold[im_threshold < 5000] = 0
            threshold_im_png = Image.fromarray(im_threshold)
            threshold_im_png = threshold_im_png.convert("L")
            threshold_im_png.save(path + '/average-5000.png')
            pandas.DataFrame(im_threshold).to_csv(path +'/average-5000.csv')
def quantitation():
    for foldernum in range(10, 78):
        for num in range (1, 9):
            num_new = num + 1
            file_1 = 'Z' + str(foldernum) + '_July27-2_L_Raw_Predict@UNet_Glomerulus2DZ@July27-2_R@BF123456-0' + str(num) + ext
            file_2 = 'Z' + str(foldernum) + '_July27-2_L_Raw_Predict@UNet_Glomerulus2DZ@July27-2_R@BF123456-0' + str(num_new) + ext
            r1 = Image.open(file_1)
            pix_1 = numpy.array(r1)    
            r2 = Image.open(file_2)
            pix_2 = numpy.array(r2)
            pix_minus = pix_2 - pix_1
            print(pix_minus)
            pandas.DataFrame(pix_minus).to_csv(str(foldernum) +'/pix_minux' + str(num_new) + '-' + str(num) + 'data.csv')
            im_minus = Image.fromarray(pix_minus)
            im_minus.save(str(foldernum) + '/pix_minus' + str(num_new) + '-' + str(num) + 'data.png')
    for foldernum in range(1, 10):
        for num in range (1, 9):
            num_new = num + 1
            file_1 = 'Z0' + str(foldernum) + '_July27-2_L_Raw_Predict@UNet_Glomerulus2DZ@July27-2_R@BF123456-0' + str(num) + ext
            file_2 = 'Z0' + str(foldernum) + '_July27-2_L_Raw_Predict@UNet_Glomerulus2DZ@July27-2_R@BF123456-0' + str(num_new) + ext
            r1 = Image.open(file_1)
            pix_1 = numpy.array(r1)    
            r2 = Image.open(file_2)
            pix_2 = numpy.array(r2)
            pix_minus = pix_2 - pix_1
            pandas.DataFrame(pix_minus).to_csv(str(foldernum) + '/pix_minux' + str(num_new) + '-' + str(num) + 'data.csv')
            im_minus = Image.fromarray(pix_minus)
            im_minus.save(str(foldernum) +'/pix_minus' + str(num_new) + '-' + str(num) + 'data.png')
        

