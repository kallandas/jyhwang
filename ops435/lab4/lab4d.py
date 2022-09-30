#!/usr/bin/env python3
# Author ID: jyhwang
# Strings 1

str1 = 'Hello World!!'
str2 = 'Seneca College'

num1 = 1500
num2 = 1.50

def first_five(string):
    substring = string[0:5]
    return substring
    # Place code here - refer to function specifics in section below

def last_seven(string):
    substring = string[-7:]
    return substring
    # Place code here - refer to function specifics in section below

def middle_number(number):
    number=str(number)
    substring = number[1] + number[2]
    return substring
    # Place code here - refer to function specifics in section below

def first_three_last_three(string1,string2):
    substring = string1[0:3] + string2[-3:]
    return substring
    # Place code here - refer to function specifics in section below


if __name__ == '__main__':
    print(first_five(str1))
    print(first_five(str2))
    print(last_seven(str1))
    print(last_seven(str2))
    print(middle_number(num1))
    print(middle_number(num2))
    print(first_three_last_three(str1, str2))
    print(first_three_last_three(str2, str1))