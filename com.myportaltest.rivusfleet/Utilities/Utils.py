'''
Created on 28 Oct 2020

@author: 612563313
'''

import os
import time

import urllib.request


def CreateDir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        
nowTsttime =time.strftime("%Y%m%d%H%M")  


def get_FileDownload(url,fname,ftype):
    fpath = fname+ftype
    urllib.request.urlretrieve(url,fpath)  
        






