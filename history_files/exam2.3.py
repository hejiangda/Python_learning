#!/usr/bin/env python
#coding=utf-8

a=int(raw_input())
b=int(raw_input())
c=int(raw_input())

import math

C=math.acos((c**2-a**2-b**2)/(-2*a*b))

print (C/math.pi)*180
