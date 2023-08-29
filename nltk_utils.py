#!/usr/bin/env python
# coding: utf-8
 
import nltk
import numpy as np
from nltk.stem import PorterStemmer
ps = PorterStemmer()

# nltk.download('punkt') 

def tokenize(sentence): 
    return nltk.word_tokenize(sentence) 

def stem(word_to_stem):
    word = word_to_stem.lower()
    return ps.stem(word)

def bag_of_words(tokenized_sentence, all_words):
    tokenized_sentence = [stem(w) for w in tokenized_sentence]
    
    bag = np.zeros(len(all_words), dtype=np.float32)
    for idx, w in enumerate(all_words):
        if w in tokenized_sentence:
            bag[idx] = 1.0 
        
    return bag

