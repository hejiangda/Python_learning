#!/usr/bin/env python
#coding=utf-8

n=int(raw_input())
summ=0
import math
def prime(num):
    for x in range(2,int(math.sqrt(num))+1):
        if num%x==0  :
            return 0
    return num
for x in range(2,n+1):
    if prime(x)!=0:
        summ+=x

print summ
