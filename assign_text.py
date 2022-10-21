
#!/usr/bin/env python3
# Author ID: jyhwang

from decimal import ROUND_05UP
import subprocess

def percent_to_graph(percent, max_length=20):
    # "returns a string: eg. '##  ' for 50 if total_chars == 4"  
    num_chr = round((max_length * percent) / 100) # Calculating input into actual number of characters to draw. Round up.
    num_spc = max_length - num_chr  # Calculating the number of spaces to print
    graph_draw = (('=' * num_chr) + (' ' * num_spc)) # print out the character "#" as many times as num_char value.
    return graph_draw

def call_du_sub(location):
    p = subprocess.Popen(['du -d 1 ' + location], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # This command line runs 'du -d 1' command on the <target directory> and put it into variable "p".
    output = p.communicate()
    # output is used to store raw data in the tuple data format so that it can be processed in more managable ways later on.
    result = output[0].decode('utf-8').strip().split('\n')
    # Splits the tuple data into a list so that it can be used later on by another function.
    return result

def create_dir_dict(raw_dat):
    "get list from du_sub, return dict {'directory': 0} where 0 is size"
    dict = {}
    for item in raw_dat:
        newlist = item.split('\t')
        dict[newlist[1]] = newlist[0]
    return dict

def get_total(raw_dict, target_dir):
    value = int()
    for k, v in raw_dict.items():
        if k == target_dir:
            value = v 
    return value

    "return total size (in bytes) of the target directory"
    
# def get_total(raw_dict, target_dir):
#    sum = int()
#    for k, v in raw_dict.items():
#        if k is not target_dir:
#            sum = sum + int(v)
#    return sum
#    "return total size (in bytes) of the target directory"

raw_dict = create_dir_dict(call_du_sub('~/ops435'))
print(raw_dict)
print(get_total(raw_dict, '/home/jyhwang/ops435/lab3'))

