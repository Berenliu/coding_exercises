#!/bin/python3

import math
import os
import random
import re
import time
import sys

def down_binary_search(arr, x):
# find the number of element in arr that are smaller than x
    l = 0
    h = len(arr)
    res = 0
    if h <= 5:
        for i in arr:
            if i<x:
                res += 1
            else:
                break
    else:
        mid = len(arr)//2
        if arr[mid]>x:
            res=down_binary_search(arr[:mid], x)
        elif arr[mid+1]<x:
            res=down_binary_search(arr[(mid+2):], x) + mid + 2
        else:
            res = mid + 1
    return res

# Complete the countTriplets function below.
def countTriplets(arr, r):
    max_num = max(arr)
    res = 0
    ind = {}
    if r>1:
        for (j, i) in enumerate(arr):
            if i in ind:
                ind[i].append(j)
            else:
                ind[i] = [j]
        keys = list(ind.keys())
        keys.sort()
        for start in keys:
            if start%r==0 and start/r in ind and start*r in ind:
                for k in ind[start]:
                    res += down_binary_search(ind[start/r], k)*(len(ind[start*r])-down_binary_search(ind[start*r],k))
    elif r==1:
        for i in arr:
            if i in ind:
                ind[i] +=1
            else:
                ind[i] = 1
        for i in ind:
            l = ind[i]
            if l>=3:
                res += l*(l-1)*(l-2)//6
    return res

def countTriplets_eff(arr, r):
    res = 0
    ind1 = {}
    ind2 = {}
    if r>1:
        for i in arr:
            if i in ind2:
                res += ind2[i]
            if i in ind1:
                if i*r in ind2:
                    ind2[i*r] += ind1[i]
                else:
                    ind2[i*r] = ind1[i]
            if i not in ind1:
                ind1[i] = 1
            else:
                ind1[i] += 1
        return res
    elif r==1:
        for i in arr:
            if i in ind:
                ind[i] +=1
            else:
                ind[i] = 1
        for i in ind:
            l = ind[i]
            if l>=3:
                res += l*(l-1)*(l-2)//6
    return res

                

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # nr = input().rstrip().split()

    # n = int(nr[0])

    # r = int(nr[1])

    # arr = list(map(int, input().rstrip().split()))

    f = open("../input10.txt", "rb")

    start = time.time()
    n, r = [int(i) for i in f.readline().strip().split()]

    arr = [int(i) for i in f.readline().strip().split()]

    # arr = [100]*100

    # r = 1

    # arr = list(range(1000))

    ans = countTriplets_eff(arr, r)

    print(ans)
    print(time.time()-start)
    #fptr.write(str(ans) + '\n')

    #fptr.close()
