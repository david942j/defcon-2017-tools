push R00 # push ebp
adi R00, ST, 0 # mov ebp, esp
ml ST, 0x1337 # fuck up esp
ml R06,0 #000 123 000
mh R06,0x10040 # 080 123 040
ml R02,0 # 000 121 000
mh R02,0x14040 # 0a0 113 040
xr R04,R04,R04 # 108 070 040
ml R04,0x20 # 000 122 020
dmt R02,R06,R04 # 08c 0d0 080
stt R04, [R02 + 0x2000] # 104 168 000 080 000 000
adi ST, R00, 0
pop R00
BACK
