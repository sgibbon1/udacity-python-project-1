#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images_hints.py
#
# PROGRAMMER: Sean Gibbons
# DATE CREATED: June 11, 2021
# REVISED DATE:
from classifier import classifier

# TODO 3: EDIT and ADD code BELOW to do the following that's stated in the
#       comments below that start with "TODO: 3" for the classify_images function
#       Specifically EDIT and ADD code to define the classify_images function.
#       Notice that this function doesn't return anything because the
#       results_dic dictionary that is passed into the function is a mutable
#       data type so no return is needed.
#
def classify_images(images_dir, labels_dic, model):
    results_dic = dict()
    for key in labels_dic:
       model_label = classifier(images_dir + key, model)
       model_label = model_label.lower()
       model_label = model_label.strip()
       check = labels_dic[key]
       correct = model_label.find(check)
       if correct >= 0:
           if ( (correct == 0 and len(check) == len(model_label)) or
                (  ( (correct == 0) or (model_label[correct - 1] == " ") )  and
                   ( (correct + len(check) == len(model_label)) or
                      (model_label[correct + len(check): correct + len(check) +
                      1] in (","," ") ) ) ) ):
               if key not in results_dic:
                   results_dic[key] = [check, model_label, 1]
           else:
               if key not in results_dic:
                   results_dic[key] = [check, model_label, 0]
       else:
           if key not in results_dic:
               results_dic[key] = [check, model_label, 0]
    return(results_dic)
