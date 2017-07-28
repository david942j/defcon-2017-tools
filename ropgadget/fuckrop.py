#!/usr/bin/python
from pwn import *
from collections import deque
import sys
import os

global r

context.log_level=100
if len(sys.argv) < 2 :
	print "useage: ./fuckrop binary [roplen]"
	exit()

r = process(['./clemency-emu',sys.argv[1],'-d','0'])

r.recvuntil('\n> ')

func = {}

func["0"]=1

todo = ["0"]
if len(sys.argv) >2 :
	roplen = int(sys.argv[2])
else:
	roplen = 4
roptodo = deque([])
roplist = dict()

def parse_function(address):
	data = ''
	maxx = 0
	r.sendline('u '+hex(address)[2:]+' 500')
	r.recvline()
	s = r.recvuntil('\n> ').split('\n')[:-1]
	for line in s:
		line = line.replace('\0','')
		if len(roptodo) < roplen :
			roptodo.append(line)
		else:
			roptodo.popleft()
			roptodo.append(line)	
		now = int(line[:line.find(':')],16)
		if 'car' in line :
			x = line[line.find('(')+1:line.find(')')][2:]
			x = x.lstrip('0')
			if(func.has_key(x)==False):
				func[x]=1
				todo.append(x)
		elif 'Error' in line :
			return 0
		elif '(' in line:
			x = line[line.find('(')+1:line.find(')')][2:]
			if int(x,16)>maxx:
				maxx = int(x,16)
		elif 're' in line and maxx < now:
			key = int(roptodo[0].split(":")[0],16)
			if(roplist.has_key(key)==False):
				roplist[key] = "\n".join(roptodo)
			roptodo.clear()
			return now#data+'\n'+line
		elif 'ir' in line and maxx < now:
			return now#data+'\n'+line
		elif 'ht' in line and maxx < now:
			return now#data+'\n'+line



Q = 0x00
maxsize = 0
while(len(todo)):
        x = todo.pop()
	if(int(x,16)>maxsize):
		maxsize=int(x,16)
        parse_function(int(x,16))

while (Q<maxsize):
	x = parse_function(Q)
	if x == 0:
		Q +=1 
	else :
		Q = x + 1
D =  roplist.keys()
D.sort()

for addr in D :
	print "-------------"
	print roplist[addr]
