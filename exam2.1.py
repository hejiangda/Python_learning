#!/usr/bin/python2.7
#coding=utf-8

weight=float(raw_input())
high=float(raw_input())

bmi=weight/(high**2)

print format(bmi,'.2f')
# print '{:.2f}'.format(bmi)
