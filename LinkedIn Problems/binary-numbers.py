#!/bin/python

import sys


n = int(raw_input().strip())
top_count = 0
count = 0
flag = False
data = bin(n)
#print data, len(data), int(data[2])
for i in range(2, len(data)):
    #print int(data[i]), top_count, count
    if int(data[i]) == 0:
        if count > top_count:
            top_count = count
        count = 0
        flag = False
        continue
    if int(data[i]) == 1 and flag is False:
        flag = True
        count = 1
        continue
    if int(data[i]) == 1 and flag is True:
        count += 1
    if i == len(data) - 1:
        if count > top_count:
            top_count = count
print top_count
