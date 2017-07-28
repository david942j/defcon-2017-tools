from pwn import *

context.log_level=100

def parse_function(binary, address):
    r = process(['/tmp2/clemency-emu',binary,'-d','0'])
    r.recvuntil('\n> ')

    try:
        data = ''
        r.sendline('u '+hex(address)[2:]+' 30')
        r.recvline()
        s = r.recvuntil('\n> ').split('\n')
        for line in s:
            line = line.replace('\0', '').strip()
            if line.startswith('>'):
                break

            data += line + '\n'

        return data.strip()
    finally:
        r.close()
