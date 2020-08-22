#n = int(input().strip())
#arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
#The following passed the test
#print(*reversed(arr))
#l = []
#for i in range(4):
 #  a = input().strip().split(' ')
  # l.append(a)

#arr = [int(i) for i in input().strip().split(' ')]
#print(l)

#!/bin/python3


#!/bin/python3


#!/bin/python3

import sys

def multi(n):
    s = {}
    for i in range(n):
        if(i%3== 0 or i%5 == 0):
            s.add(i)
    print(s)        
t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    multi(n)

