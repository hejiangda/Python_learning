#!/usr/bin/env python
#coding=utf-8

f=open("names.txt")


def is_palindrome(name):
    low =0
    up = len(name)-1
    while low <up:
        if name[low]!=name[up]:
            return False
        low +=1
        up-=1
    return name

for line in f:
    name =line.strip()
    if is_palindrome(name)!=False:
        if len(name)==8:
            print is_palindrome(name)


f.close()
