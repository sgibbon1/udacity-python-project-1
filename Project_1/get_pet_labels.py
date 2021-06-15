#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER: Sean Gibbons
# DATE CREATED: Friday, June 11, 2021
# REVISED DATE:
# PURPOSE: Create the function get_pet_labels that creates the pet labels from
#          the image's filename. This function inputs:
#           - The Image Folder as image_dir within get_pet_labels function and
#             as in_arg.dir for the function call within the main function.
#          This function creates and returns the results dictionary as labels_dic
#          within get_pet_labels function and as results within main.
#          The labels_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with labels_dic dictionary that you create
#       with this function
#
def get_pet_labels(image_dir):
    pet_images = listdir(image_dir)
    labels_dic = dict()

    for i in range(0, len(pet_images), 1):

       if pet_images[i][0] != ".":
           image_name = pet_images[i].split("_")
           pet_label = ""
           for word in image_name:
               if word.isalpha():
                   pet_label += word.lower() + " "
           pet_label = pet_label.strip()
           if pet_images[i] not in labels_dic:
              labels_dic[pet_images[i]] = pet_label
           else:
               print("Warning: Duplicate files exist in directory",
                     pet_images[i])
    return(labels_dic)
    items_in_dic = len(labels_dic)
