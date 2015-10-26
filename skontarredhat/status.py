#!/usr/bin/python

from __future__ import print_function

from os import path
import os


directories = ['2048', '4096']
for directory in directories:
    files = os.listdir(directory)
    finished = len([a for a in files if path.getsize(path.join(directory, a)) != 0])
    print(directory, '->', finished)
