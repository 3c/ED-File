# -*- coding:utf-8 -*-
import io
import os

file = open('a.txt','w')
file.write('made by hehe')

fileobj = open('test.mp4','rb')

while True:
	line = fileobj.readline()
	if len(line)==0:
		break;
	file.write(line)

fileobj.close
file.close

