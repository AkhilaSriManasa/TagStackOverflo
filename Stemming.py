# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 06:33:31 2018

@author: Akhila Sri Manasa
"""


from nltk.stem.wordnet import WordNetLemmatizer 
#import nltk
#nltk.download('wordnet')
lem = WordNetLemmatizer()
from nltk.stem.porter import PorterStemmer 
stem = PorterStemmer()
word = "executing" 
nw=lem.lemmatize(word, "v")
print(nw)
sw=stem.stem(word)
print(sw)
