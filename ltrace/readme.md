ltrace 
---

顯示 function name 需要 .map file
可以由 poloo 的 libc label 產生
`parse.py label > {binary_name}.map`

.map 檔案名稱需要與 binary 相同才會被載入

```bash
$ ./9trace -d 0 ./rubix
Parsing map file ./rubix.map...
Found _start
Found atoi
Found atol
Found isascii
...
Read 127 entries
Loading ./rubix
R00: 0000000    R01: 0000000    R02: 0000000    R03: 0000000
R04: 0000000    R05: 0000000    R06: 0000000    R07: 0000000
R08: 0000000    R09: 0000000    R10: 0000000    R11: 0000000
R12: 0000000    R13: 0000000    R14: 0000000    R15: 0000000
R16: 0000000    R17: 0000000    R18: 0000000    R19: 0000000
R20: 0000000    R21: 0000000    R22: 0000000    R23: 0000000
R24: 0000000    R25: 0000000    R26: 0000000    R27: 0000000
R28: 0000000     ST: 0000000     RA: 0000000     PC: 0000000
 FL: 0000000

 0000000 <_start>:                2b0402000002b8  ldt    R01, [R00 + 0x57, 3]
 > g
 [000004D] car 0000901 (000C000, 3FEB800, 000FFAE)
 [0000931] car memset(000A04C, 0000000, 0000021)
 [000093E] car memset(000C000, 0000000, 000000F)
 [0000051] car 00090F1 (0000000, 0000000, 0000000)
 [0009106] car 0008A4D (0000000, 0000000, 0000000)
 [0008A62] car malloc(0001000, 0000000, 0000000)
 [0009110] car printf(0009E73, 000C000, 000E000)
 [0004DAB] car vfprintf(00098E9, 0009E73, 3FFFB91)
 [0004854] car oc(00098E9, 0000054, 3FFFB91)
 [0004854] car oc(00098E9, 0000068, 3FFFB91)
 [0004854] car oc(00098E9, 0000069, 3FFFB91)

...
```




