#!/bin/python

import sys


n = int(raw_input().strip())
s = raw_input().strip()
k = int(raw_input().strip())
data = ""

range1 = range(65, 91)
range2 = range(97, 123)
for char in s:
    if not char.isalpha():
        data += char
        continue
    if ord(char) in range1:
        if ord(char) + k > 90:
            data += chr((ord(char) + k - 90) + 64)
            continue
    if ord(char) in range2:
        if ord(char) + k > 122:
            
            data += chr((ord(char) + k - 122) + 96)
            continue
        
    data = data + chr(ord(char) + k)
print data
