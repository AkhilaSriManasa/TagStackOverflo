# -*- coding: utf-8 -*-
"""
Created on Mon Sep 24 12:16:32 2018

@author: Akhila Sri Manasa
"""
import re
from nltk.util import ngrams
s= "how to make it force download of externally hosted image?"
s = s.lower()
s = re.sub(r'[^a-zA-Z0-9\s]', ' ', s)
tokens = [token for token in s.split(" ") if token != ""]
output = list(ngrams(tokens, 3))
print(output)
