# -*- coding:utf-8 -*-
import io
import os

file = open('after.mp4','w')
fileobj = open('a.txt','rb')

key = "made by hehe"

while True:
	line = fileobj.readline()
	if key in line:
		print(line)
		line = line.replace(key,'')
		print(line)
	if len(line)==0:
		break;
	file.write(line)

fileobj.close
file.close

