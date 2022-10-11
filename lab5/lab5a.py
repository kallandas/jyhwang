#!/usr/bin/env python3
# Author ID: jyhwang

def read_file_string(file_name):
    f = open(file_name, 'r')
    newlist = f.read()
    f.close()
    return newlist
    # Takes file_name as string for a file name, returns its entire contents as a string

def read_file_list(file_name):
    f = open(file_name, 'r')
    newlist = f.readlines()
    f.close()
    return newlist
    # Takes a file_name as string for a file name, 
    # return its entire contents as a list of lines without new-line characters

if __name__ == '__main__':
    file_name = 'data.txt'
    print(read_file_string(file_name))
    print(read_file_list(file_name))