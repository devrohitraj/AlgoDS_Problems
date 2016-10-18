#!/bin/python

import sys

def do_it(n, k):
    output = 0
    for i in range(1, n):
        for j in range(i+1, n+1):
            val = i & j
            if val == k - 1:
                return val
            if val < k and val > output:
                output = val
    return output

t = int(raw_input().strip())
for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = [int(n),int(k)]
    output = do_it(n, k)
    print output
    
    

            
