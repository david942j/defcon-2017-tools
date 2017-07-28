
cLEMENCy IDA Plugin
===================


### Usage

1. Copy `clemency.py` and `clemency_inst.py` to `IDA 6.8/procs/`
2. Run `preprocess.py` for target binary
3. Open preprocessed binary in IDA and then choose `clemency` processor
4. Press Ok to all


- Press `c` to makecode
- Press `z` to convert bytes to tribytes data
- Press `,` to convert bytes to tribytes string


### Simplified Instructions

- `ml rA, lo + mh rA, hi -> meh rA, (hi << 10) | (lo & 0x3ff)`
    - Warning: the result may be incorrect if ml and mh are at the boundary of two basicblocks
