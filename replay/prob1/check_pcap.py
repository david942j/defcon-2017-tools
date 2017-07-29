from utils import check
import os,time,glob


while True:
    files = os.listdir('bin')
    version = len(files)
    name = glob.glob('bin/'+str(version)+'_*')[0]
    out_dir = 'json/'+str(version)
    fl = os.listdir('json/todo')
    print len(fl)
    if fl != 0:
        check(name[4:],'json/todo',out_dir,True)
    time.sleep(200)
