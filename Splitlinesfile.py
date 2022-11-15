# -*- coding: utf-8 -*-
"""
Created on Fri Dec 14 13:06:24 2018

@author: karthikamaravadi
"""

lines_per_file = 50000
smallfile = None
bigfile = open('filename.txt', errors='ignore')
with bigfile:
    for lineno, line in enumerate(bigfile):
        if lineno % lines_per_file == 0:
            if smallfile:
                smallfile.close()
            small_filename = 'filename_{}.txt'.format(lineno + lines_per_file)
            smallfile = open(small_filename, "w")
        smallfile.write(line)
    if smallfile:
        smallfile.close()