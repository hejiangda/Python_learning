#!/usr/bin/python2.7
#coding=utf-8


allmoney=0

def moneyafter(year):
    global allmoney
    if year ==1:
        return 1047
    else:
        return (moneyafter(year-1)+1000)*(1.047)


print moneyafter(10)

import math
a=10
b=40
c=15
delta=math.sqrt(b**2-4*a*c)

x1=(-b+delta)/(2*a)
x2=(-b-delta)/(2*a)

print x1,x2
