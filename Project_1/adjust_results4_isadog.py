#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py
#
# PROGRAMMER: Sean Gibbons
# DATE CREATED: June 11, 2021
# REVISED DATE:
# PURPOSE: Create a function adjust_results4_isadog that adjusts the results
#          dictionary to indicate whether or not the pet image label is of-a-dog,
#          and to indicate whether or not the classifier image label is of-a-dog.
#          All dog labels from both the pet images and the classifier function
#          will be found in the dognames.txt file. We recommend reading all the
#          dog names in dognames.txt into a dictionary where the 'key' is the
#          dog name (from dognames.txt) and the 'value' is one. If a label is
#          found to exist within this dictionary of dog names then the label
#          is of-a-dog, otherwise the label isn't of a dog. Alternatively one
#          could also read all the dog names into a list and then if the label
#          is found to exist within this list - the label is of-a-dog, otherwise
#          the label isn't of a dog.
#         This function inputs:
#            -The results dictionary as results_dic within adjust_results4_isadog
#             function and results for the function call within main.
#            -The text file with dog names as dogfile within adjust_results4_isadog
#             function and in_arg.dogfile for the function call within main.
#           This function uses the append function to add items to the list
#           that's the 'value' of the results dictionary. You will be adding the
#           whether or not the pet image label is of-a-dog as the item at index
#           3 of the list and whether or not the classifier label is of-a-dog as
#           the item at index 4 of the list. Note we recommend setting the values
#           at indices 3 & 4 to 1 when the label is of-a-dog and to 0 when the
#           label isn't a dog.
#
##
# TODO 4: Define adjust_results4_isadog function below, specifically replace the None
#       below by the function definition of the adjust_results4_isadog function.
#       Notice that this function doesn't return anything because the
#       results_dic dictionary that is passed into the function is a mutable
#       data type so no return is needed.
#
def adjust_results4_isadog(results_dic, dogfile):
    breeds_dic = {}
    with open(dogfile) as f:
        for line in f:
            line = line.rstrip('\n').lower()
            if line not in breeds_dic:
                breeds_dic[line] = 1

    for filename, labels in results_dic.items():
        picture_match = 1 if labels[0] in breeds_dic else 0
        classifier_match = 1 if labels[1] in breeds_dic else 0
        results_dic[filename].extend([picture_match, classifier_match])
