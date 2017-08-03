## Files
* `mh.asm` assembly of flag encryptor. Use fixer to patch it into binaries.
* `asm_util.rb` helper to generate cLEMENCy assembly.
* `mh.asm.rb` will genereate `mh.asm`.

## Sample
`clemency-emu mh.bin` will output the encrypted flag.

Encode it with base64 and feed as argument to `backdoor_dec.rb` will show the decrypted flag.
```
clemency-emu mh.bin | base64 | xargs ./backdoor_dec.rb
# ABcDeFGHijKlmnopQrstUvwxYZ
```
