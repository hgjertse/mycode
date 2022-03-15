#!/usr/bin/env python3

import shutil
import os

#start in the home directory
os.chdir('/home/student/mycode/')

#moving the file or folder at the path source to the path destination and will return a string of the absolute path of the new location
shutil.move('raynor.obj', 'ceph_storage/')


#prompt user for a new name for the file
xname = input('What is the new name for kerrigan.obj? ')


#rename the current file
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)



