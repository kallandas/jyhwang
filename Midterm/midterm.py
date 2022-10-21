#!/usr/bin/env python3
# Author Name: Ji Yong Hwang
# Student Number: 058819954

import os

def list_files():
    p = os.popen('ls -A')
    l1 = p.read()
    l2 = l1.split('\n')
    return l2

def div_list(list):             # This code is imcomplete due to running out of time. 
    filename=[]                 # This is how far I got before running out of time.
    fileext=[]                  # VM did crash 4th time, I don't know why.
    for item in list:               
        temp = item.split('.')
        filename.append(temp[0])
        fileext.append(temp[1])  
    return filename, fileext          

if __name__ == "__main__":
    result_list = list_files()
    print(div_list(result_list))