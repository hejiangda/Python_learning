#!/usr/bin/env python
#coding=utf-8

year=int(raw_input())
month=int(raw_input())

def leap_year(year):
    if year%4==0 and year%100!=0 or year%400==0:
        return True
    else:
        return False

def months(year,month):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:

        return 30
    elif month ==0:

        return 0
    elif leap_year(year):

        return 29
    else:

        return 28

day={1:'Mon',2:'Tue',3:'Wed',4:'Thu',5:'Fri',6:'Sat',7:'Sun'}

# 1800.1.1 Wed


def allday(year,month):
    days=0
    for n in range(1800,year):
        if leap_year(n):
            days+=366
        else:
            days+=365
    for n in range(1,month+1):
        days+=months(year,n)
    return days

m=(allday(year,month))%7+2
print day[m]
