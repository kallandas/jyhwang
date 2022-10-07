
#!/usr/bin/env python3
# Author ID: jyhwang

import subprocess

def percent_to_graph(percent, total_chars, max_length=20):
    # "returns a string: eg. '##  ' for 50 if total_chars == 4"  
    percent = int(percent)
    total_chars = int(total_chars)
    if 0 <= percent <= 100:
        num_char = total_chars * percent // 100 # Calculation input into actual number of characters to draw.
        num_space = total_chars - num_char # Calculating the number of spaces to print
        graph_draw = (print(('#' * num_char) + ('.' * num_space))) # print out the character "#" as many times as num_char value.
        return str(graph_draw)
    else:
        return print("Error, percent value is out of range. Must be in range of 0 to 100")

percent_to_graph(33,10)
percent_to_graph(56,15)
percent_to_graph(70,20)
percent_to_graph(63,30)
percent_to_graph(89,80)
print(round(10.55))

def call_du_sub(location):
    p = subprocess.Popen(['du -d 1 ' + location], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    # This command line runs 'du -d 1' command on the <target directory> and put it into variable "p".
    output = p.communicate()
    # output is used to store raw data in the tuple data format so that it can be processed in more managable ways later on.
    result = output[0].decode('utf-8').strip().split('\n')
    # Splits the tuple data into a list so that it can be used later on by another function.
    return result