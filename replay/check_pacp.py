from utils import check
import os,time,glob


while True:
    files = os.listdir('bin')
    version = len(files)
    name = glob.glob('bin/'+str(version)+'_*')[0]
    out_dir = 'json/'+str(version)
    check(name[4:],'json/todo',out_dir)
    time.sleep(30)
