#!/usr/bin/python2.7
#coding=utf-8

seconds=int(raw_input())
hour=seconds/3600
minute=(seconds%3600)/60
second=(seconds%3600)%60

print hour,minute,second
