# -*- coding: utf-8 -*-
"""
Created on Tue Oct  9 07:21:15 2018

@author: Akhila Sri Manasa
"""

from textblob.classifiers import NaiveBayesClassifier as NBC
from textblob import TextBlob
#import NaiveBayesClassifier
training_corpus = [
                   ('How to implement classes', 'Implementation'),
                   ('How to implement structs', 'Implementation'),
                   ('My code throws an error', 'Error'),
                   ('I am getting error - Segmentation fault', 'Error'),
                   ('Is there a way to learn java easily', 'Conceptual'),
                   ('Is there a way to understand python better', 'Conceptual'),
                   ("How to learn coding",'Conceptual'),
                   ('Why is my code not working', 'Discrepancy'),
                   ('How could this be fixed', 'Discrepancy'),
                   ('When i execute, my system got crashed', 'Crash'),
                   ('System gets crashed', 'Crash')]
test_corpus = [
                ("I'm getting error - Invalid pointer", 'Error'), 
                ('How can ArrayIndexOutofBound exception be fixed', 'Discrepancy'),
                ('How can I learn implementation of stacks','Conceptual')]

model = NBC(training_corpus) 
print(model.classify("How to implement nltk library"))
print(model.classify("How to classify")) 
print(model.classify("How to learn c++"))

print(model.accuracy(test_corpus))
