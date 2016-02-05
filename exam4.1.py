#!/usr/bin/env python
#coding=utf-8

def fib(num):
    if num ==1:
        return 1
    elif num ==2:
        return 2
    else:
        return fib(num-1)+fib(num-2)



n=int(raw_input())
summ=0
for m in range(1,n+1):
    if fib(m)>n:
        break
for t in range(1,m):
    if fib(t)%2==0:
        summ+=fib(t)

print summ
