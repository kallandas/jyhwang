#!/usr/bin/env python3
# Author ID: jyhwang
# To demonstrate the different way of comparing sets. 
# There will be three functions, each returning a different set comparison. 

def join_sets(s1, s2):
    s3 = set(s2).union(set(s1))
    return s3
    # join_sets will return a set that contains every value from both s1 and s2

def match_sets(s1, s2):
    s3 = set(s1).intersection(set(s2))
    return s3
    # match_sets will return a set that contains all values found in both s1 and s2

def diff_sets(s1, s2):
    s3 = set(s2).symmetric_difference(set(s1))
    return s3 
    # diff_sets will return a set that contains all different values which are not shared between the sets

if __name__ == '__main__':
    set1 = set(range(1,10))
    set2 = set(range(5,15))
    print('set1: ', set1)
    print('set2: ', set2)
    print('join: ', join_sets(set1, set2))
    print('match: ', match_sets(set1, set2))
    print('diff: ', diff_sets(set1, set2))
