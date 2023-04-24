#!/usr/bin/env python
# coding: utf-8
# By Maxim Vovenko


import os
from random import choice
import shutil

# Create empty arrays to store file names
imgs = []
xmls = []

# setup dir names
##IMPORTANT NOTE: If you will add more images and labels later, the number of files in train/val directory pairs must match.
workspace_base_dir = os.getcwd()
ee104TrainImagePath = f'{workspace_base_dir}\\images\\ee104_train'
ee104TrainLabelPath = f'{workspace_base_dir}\\labels\\ee104_train'
ee104ValImagePath = f'{workspace_base_dir}\\images\\ee104_val'
ee104ValLabelPath = f'{workspace_base_dir}\\labels\\ee104_val'

coco_images = f'{workspace_base_dir}\\coco_dataset'  # dir where downloaded images are stored
coco_labels = f'{workspace_base_dir}\\coco_dataset'  # dir where downloaded annotations txt files are stored

images_im_adding = f'{workspace_base_dir}\\images_im_adding'

# setup ratio (val ratio = rest of the files in origin dir after splitting into train and test)
train_ratio = 0.8
val_ratio = 0.2

# total count of imgs
totalImgCount = len(os.listdir(coco_images))
print("Total number of COCO images are : ", totalImgCount)

# storing files to corresponding arrays
for (dirname, dirs, files) in os.walk(coco_images):
    for filename in files:
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.gif') or filename.endswith(
                '.jpeg') or filename.endswith('.heif') or filename.endswith('.hif'):
            imgs.append(filename)
for (dirname, dirs, files) in os.walk(coco_labels):
    for filename in files:
        if filename.endswith('.txt'):
            xmls.append(filename)

for (dirname, dirs, files) in os.walk(images_im_adding):
    for filename in files:
        if filename.endswith('.jpg') or filename.endswith('.png') or filename.endswith('.gif') or filename.endswith(
                '.jpeg') or filename.endswith('.heif') or filename.endswith('.hif'):
            imgs.append(filename)
for (dirname, dirs, files) in os.walk(images_im_adding):
    for filename in files:
        if filename.endswith('.txt'):
            xmls.append(filename)

# counting range for cycles
countForTrain = int(len(imgs) * train_ratio)
countForVal = int(len(imgs) * val_ratio)
print("Number of training images are   : ", countForTrain)
print("Number of validation images are : ", countForVal)

# cycle for train dir
for x in range(countForTrain):
    fileJpg = choice(imgs)  # get name of random image from origin dir
    fileXml = fileJpg[:-4] + '.txt'  # get name of corresponding annotation file
    try:
        shutil.copy(os.path.join(coco_images, fileJpg), os.path.join(ee104TrainImagePath, fileJpg))
        shutil.copy(os.path.join(coco_labels, fileXml), os.path.join(ee104TrainLabelPath, fileXml))
    except Exception as E:
        print(E)
        pass
    # remove files from arrays
    try:
        imgs.remove(fileJpg)
        xmls.remove(fileXml)
    except Exception as E:
        print(E)
        pass


# cycle for val dir
for x in range(countForVal):
    fileJpg = choice(imgs)  # get name of random image from origin dir
    fileXml = fileJpg[:-4] + '.txt'  # get name of corresponding annotation file

    # move both files into train dir
    try:
        shutil.copy(os.path.join(coco_images, fileJpg), os.path.join(ee104ValImagePath, fileJpg))
        shutil.copy(os.path.join(coco_labels, fileXml), os.path.join(ee104ValLabelPath, fileXml))
    except Exception as E:
        print(E)
        pass
    # remove files from arrays
    try:
        imgs.remove(fileJpg)
        xmls.remove(fileXml)
    except Exception as E:
        print(E)
        pass

# The rest of files will be validation files, so rename origin dir to val dir
# os.rename(crsPath, valPath)
# shutil.move(coco_images, ee104ValImagePath)
# shutil.move(coco_labels, ee104ValLabelPath)
