#!/usr/bin/env python
#coding=utf-8

# 数字197可以被称为循环素数，因为197的三个数位循环移位
# 后的数字：197,971,719均为素数。100以内这样的数字包括
# 13个，2,3,5,7,11,13,17,31,37,71,73,79,97。要求任
# 意正整数n以内一共有多少个这样的循环素数。

n=int(raw_input())
import math
def prime(num):
    for x in range(2,int(math.sqrt(num))+1):
        if num%x==0:
            return 0
    return num

count=0

def loop_prime(num):
    global count
    if num/10==0 and prime(num)!=0:
        count+=1
    elif num/100==0 and prime(num)!=0:
        num1=num%10*10+num/10
        if prime(num1)!=0:
            count+=1
    elif num/1000==0 and prime(num)!=0:
        num1=num/10%10*100+num%10*10+num/100
        num2=num%10*100+num/100*10+num/10%10
        if prime(num1)!=0 and prime(num2)!=0:
            count+=1

for x in range(2,n+1):
    loop_prime(x)
print count
