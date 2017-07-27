from pwn import *
import sys

global r


context.log_level=100
r = process(['/tmp2/clemency-emu',sys.argv[1],'-d','0'])

r.recvuntil('\n> ')


def parse_function(address):
	data = ''
	maxx = 0
	r.sendline('u '+str(address)+' 5000')
	r.recvline()
	s = r.recvuntil('\n> ').split('\n')
	for line in s:
		line = line.replace('\0','')
		now = int(line[:line.find(':')],16)
		if 'car' in line :
			x = line[line.find('(')+1:line.find(')')][2:]
		elif 'Error' in line :
			print data
			return
		elif '(' in line:
			x = line[line.find('(')+1:line.find(')')][2:]
			if int(x,16)>maxx:
				maxx = int(x,16)
		elif 're' in line and maxx < now:
			print data+'\n'+line
			return
		if data != '':
			data += '\n'
		data += line

parse_function(sys.argv[2])

