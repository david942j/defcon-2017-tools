
Example:

FD=5,6,7,9,11 LD_PRELOAD=./emu89.so ./clemency-emu -l 2134 a.bin

FD=6 LD_PRELOAD=./emu89.so socat tcp-listen:8001,reuseaddr,fork tcp:localhost:8000
