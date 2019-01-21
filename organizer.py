# -*- coding: utf-8 -*-
"""
Created on Sun Jan 20 20:20:39 2019

@author: Amin
"""
from glob import glob # using glob to input all the poem files
from pers_alphab import pers_alphab # used to normalize the poem alphabet
import re # for quick split function
from time import time # to time the code


def stop_word_importer(file_name):# importing persian stopwords
    with open(file_name, 'r', encoding="utf8") as myfile:
        stop_words = myfile.read().replace('\n', ' ').replace("\u200c","").replace("\ufeff","").replace("."," ").split(' ')# a list of stop words
    return stop_words

tic =  time() # start time

original_path = 'original/*.txt'  # where the original (scraped) files exist
poet_files = glob(original_path)  # captures list of all the files in the folder
stop_words = stop_word_importer('stop_words.txt') # importing stop words to a list

def document_traverser(original_path, normalized_path, stop_remv_path):
    # one read two writes are initiated
    with open(original_path, "r", encoding="utf8") as f,\
    open(normalized_path, "w",  encoding="utf8") as n,\
    open(stop_remv_path, "w",  encoding="utf8") as s:
        for line in f:
            normalized = pers_alphab(line) # normelizing the content
            word_list = re.split('[\t\s:]+', normalized) # tokenizing the content
            cleaned_words = [x for x in word_list if x not in stop_words] # no stop word is in it
            n.write(normalized) # writing out the normalized documents
            s.write(" ".join(cleaned_words) + '\n')  # writing out the stop word removed documents
      

for poet in poet_files: # going over the list of all poems
    poet_name = poet[9:-4] # taking poems name out for output files
    document_traverser(poet, "normalized/" + poet_name + "_norm.txt",
                       "stop words removed/" + poet_name + "_stp_rmv.txt")
    
    
toc = time() # end time
print("This code takes {} seconds to run.".format(toc - tic))