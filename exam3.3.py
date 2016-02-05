#!/usr/bin/env python
#coding=utf-8

# 1900.1.1 MON
# 1900.1.7 SUN

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

days=366
count=0

for year in range(1901,2000+1):
    for month in range(1,13):
        days+=months(year,month)
        if days%7==0:
            count+=1

print count
