#!/usr/bin/env python3

'''
generate a list of random numbers and letters
'''

import random as r
import os

names = ['alpha', 'beta', 'gamma', 'test', 'example', 'banana', 'orange', 'apple', 'capybara', 'kangaroo', 'network', 'program', 'quiz', 'output']

suffixes = ['jpg', 'png', 'gif', 'txt', 'md', 'docx', 'rtf', 'csv', 'pdf', 'py', 'sh', 'bash', 'html', 'exe', 'conf', 'hex']

numbers = range(0, 9)

def randofilename():
    if r.randint(0, 6) == 0:
        return r.choice(names) + str(r.choice(numbers))
    else:
        return r.choice(names) + str(r.choice(numbers)) + '.' + r.choice(suffixes)

def randotouch():
    for i in range(0, numlines):
        x = os.system('touch ' + randofilename())
        if x:
            print('An error occurred.')

def randofile(filename='output'):
    with open(filename, 'w') as f:
        for i in range(0, numlines):
            f.write(randofilename() + '\n')

if __name__ == "__main__":
    numlines = 15
    for i in range(0, 21):
        print(randofilename())
    randofile('files.txt')
    randotouch()