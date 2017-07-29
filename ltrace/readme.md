ltrace 
---

顯示 function name 需要 .map file
可以由 poloo 的 libc label 產生:

`parse.py label > {binary_name}.map`

.map 檔案名稱需要與 binary 相同才會被載入
支援 emulator 的各種功能

```bash
$ ./9trace ./rubix -L 0
Parsing map file ./rubix.map...
Found _start
Found atoi
Found atol
Found isascii
...
Read 127 entries
Loading ./rubix
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




