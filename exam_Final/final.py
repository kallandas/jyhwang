#!/usr/bin/env python3
# Author Name: Ji Hwang
# Student Number: 058819954

import sys
import os, subprocess

def get_list():
    'create a list from "ls -l" command on current folder'
    p = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
    stdout = p.communicate()
    stdout = stdout[0].decode('utf-8')
    output =  stdout.split('\n')
    return output

def makeDict(list):
    'create a dictionary of filename and filesize from a list of filenames'
    newDict = dict()
    for i in list:
        if i != '' and 'total' not in i:
            item = i.split()
            filename = item[-1]
            filesize = os.path.getsize(item[-1])
            newDict[filename] = filesize
    return newDict

if __name__ == '__main__':
    flist = get_list()
    fDict = makeDict(flist)
    temp = list(fDict)
    total = 0
    for i in temp:
        if "a" in i[0]:
            print(i + " will be backed up.")
            total = total + fDict[i]
        elif "b" in i[0]:
            print(i + " will be backed up.")
            total = total + fDict[i]
        elif "c" in i[0]:
            print(i + " will be backed up.")
            total = total + fDict[i]
        elif "d" in i[0]:
            print(i + " will be backed up.")
            total = total + fDict[i]
        elif "e" in i[0]:
            print(i + " will be backed up.")
            total = total + fDict[i]
        elif "f" in i[0]:
            print(i + " will be backed up.")
            total = total + fDict[i]
    print("Total file size for bakcup is " + str(total))

