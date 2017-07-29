`/tmp2/clemency-emu mh.bin` 會直接把 flag 加密後噴出來
過 base64 後給 backdoor_dec 當第一參，backdoor_dec 會噴解密結果至 stdout
```
/tmp2/clemency-emu mh.bin | base64 | xargs ./backdoor_dec.rb
```
