probX:
    json 裡面是模擬過後的payload分類
        todo 是還沒模擬的
        1,2,3 ... 是第幾隻binary
            ok: 是模擬後沒事的payload
            exception: 是有跳出exception的
            touch_flag: 不但有跳出exception且有aceess flag那塊的address


每一題 cd 進去 bash init.sh 會清空json
```
python new_binary.py binary 會改用這個binary來跑模擬，同時也會檢查前一隻binary的exception和touch_flag(如果太多，註解一下code)
```
python get.py 會call parser.py 來parse最新的pcap
python takebin.py 抓我們更新的patch

看一份json: ./viewer.rb stream/5566/00ed10cc1a38ac7109b55cbfc0497563.json
看多份json: ./a.rb stram/5566

新題目要更新parser.py中port和problem的對照表，和utils.py模擬時用的port
