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
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main.
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
from os import listdir

# TODO 2: Define get_pet_labels function below please be certain to replace None
#       in the return statement with results_dic dictionary that you create
#       with this function
#
def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames
    of the image files. These pet image labels are used to check the accuracy
    of the labels that are returned by the classifier function, since the
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Points to folder containing dog images
    pet_images = listdir(image_dir)
    results_dic = dict()
    # Applies methods to each image in file
    for i in range(0, len(pet_images), 1):
        # Skips file if it starts with "." because it won't be a pet image file
        if pet_images[i][0] != ".":
            # Applies methods to filename
            pet_lower = pet_images[i].split("_")
            # Creates temporary label variable to hold extracted pet label name
            pet_name = ""
            # Only adds string to temporary variable if string is alphabetic,
            # places space between words and removes excess whitespace via
            # .strip
            for j in pet_lower:
                if j.isalpha():
                    pet_name += j.lower() + " "
            pet_name = pet_name.strip()
            # If filename doesn't exist in dictionary, add it and its new label,
            # otherwise print error message indicating a duplicate.
            if pet_images[i] not in results_dic:
                results_dic[pet_images[i]] = pet_name
            else:
                print("Warning: Duplicate files exist in directory",
                    pet_images[i])

    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic
    items_in_dic = len(results_dic)
