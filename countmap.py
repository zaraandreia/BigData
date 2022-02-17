#!/usr/bin/python
import sys


TAB_CHAR = '\t'

#count the number of lines, words and characters
n_lines = 0
n_words = 0
n_char = 0
for line in sys.stdin:
    n_lines+=1
    for token in line.strip().split(" "):
        n_words +=1
        n_char += len(token)
        if token: 
            print(token + TAB_CHAR + '1')

