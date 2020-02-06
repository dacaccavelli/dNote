# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
Created on Thu Jul 26 11:41:58 2018

Note taking code.
Allows for quick addition of notes from command line to desired file.

Usage:  dNote '' : open cmd line for input

        Follow instructions from there
        Pretty straightforward future Daniel
        Figure it out

@author: dcaccavelli
"""

import os

# Saves the path including the sequence name and the folder counter
my_directory = ".\\dNote_Files"

# Creates the folder if not aleady existing
if not os.path.exists(my_directory):
    os.makedirs(my_directory)

os.chdir(my_directory)
files = []
print('List of current files')
for file in os.listdir():
    files.append(file)
    print(files.index(file), file[:-4])

string = '''If adding to existing notes, enter the index.
            \rElse, enter your desired name.:'''
response = input(string).strip()

try:
    num = int(response)
    print("Adding to '%s'" % files[num])
except as err:
    print("New file '%s' made." % response)
    response = response + '.txt'
    files.append(response)
    num = files.index(response)

note = input('Enter new note:') + '\n'
with open(files[num], 'a') as file:
    file.write(note)
