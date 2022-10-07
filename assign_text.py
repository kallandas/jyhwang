
#!/usr/bin/env python3
# Author ID: jyhwang

from decimal import ROUND_05UP
import subprocess

def percent_to_graph(percent, max_length=20):
    # "returns a string: eg. '##  ' for 50 if total_chars == 4"  
    num_chr = round((max_length * percent) / 100) # Calculating input into actual number of characters to draw. Round up.
    inv_pcnt = 100 - percent  # Calculating Inverse percent.
    num_spc = round((max_length * inv_pcnt) / 100) # Calculating the number of spaces to print
    graph_draw = (('=' * num_chr) + (' ' * num_spc)) # print out the character "#" as many times as num_char value.
    return num_chr, num_spc, graph_draw

print(percent_to_graph(33,10))
print(percent_to_graph(56,15))
print(percent_to_graph(70,20))
print(percent_to_graph(63,30))
print(percent_to_graph(89,80))

def call_du_sub(location):
    p = subprocess.Popen(['du -d 1 ' + location], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # This command line runs 'du -d 1' command on the <target directory> and put it into variable "p".
    output = p.communicate()
    # output is used to store raw data in the tuple data format so that it can be processed in more managable ways later on.
    result = output[0].decode('utf-8').strip().split('\n')
    # Splits the tuple data into a list so that it can be used later on by another function.
    return result