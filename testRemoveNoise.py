# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 06:19:05 2018

@author: Akhila Sri Manasa
"""
#this code does stop-word removal and also generates n-gram tokens of size n =2.

noise_list = ["is", "a", "this", "that", "?", "!", "..."] 
def _remove_noise(input_text):
    words = input_text.split() 
    noise_free_words = [word for word in words if word not in noise_list] 
    noise_free_text = " ".join(noise_free_words) 
    return noise_free_text
final = _remove_noise("how to understand executing a program that uses strings?")
print(final)

import re
from nltk.util import ngrams
s= final
s = s.lower()
s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
tokens = [token for token in s.split(" ") if token != ""]
output = list(ngrams(tokens, 2))
print(output)