#!/usr/bin/env python
#coding=utf-8

n=int(raw_input())
sum=0
y=z=0

for y in range(0,n,5):
    sum+=y

for z in range(0,n,3):
    sum+=z

print sum
