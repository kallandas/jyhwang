#!/usr/bin/env python3
# Author ID: jyhwang

import sys

# Codes discussed & practiced during the lecture.

class Temperature:

    temp = 28.5 # incorrect, celsius format

    def rtrn_celsius(self):
        return self.temp

    def rtrn_fahrenheit(self):
        return self.temp * 1.8 + 32

    def return_unit(self):
        return 'C'

    def __eq__(self):
        return
