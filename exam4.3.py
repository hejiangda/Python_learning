#!/usr/bin/env python
#coding=utf-8

def hanoi(n,A="left",B='mid',C='right'):
    if n ==0:
        return
    else:
        hanoi(n-1,A,C,B)
        print "Move",n,"from",A,"to",C
        hanoi(n-1,B,A,C)

n=int(raw_input())

hanoi(n)

s = raw_input()
y = 0

for i in s:
    y += 1
    print y, i,

s1 = raw_input()
index = 0
s2 = ''

while index < len(s1) - 1:
    if s1[index] > s1[index + 1]:
        s2 += s1[index]
    else:
        s2 = s2 * 2

    index += 1

print s2
