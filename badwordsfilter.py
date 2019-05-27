#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 21 00:35:49 2019

@author: finnmccool
"""

#Use a function to generalise the procedure

def change_comma_toline(inputfile,outputfile):
    with open(inputfile) as file:
        data = file.read()
        badwords = data.replace(',','\n') 
    with open(outputfile,'w') as file:
        for line in badwords:
            file.write(line)
    return file
        
inputfile = input('Enter comma separated file to change to lines: >> ')
outputfile = input('Enter he name of the output file >> ')
change_comma_toline(inputfile,outputfile)
print('Your ',outputfile,' has been created!')