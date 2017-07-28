import sys,os
from shutil import move,copyfile
from hashlib import md5
from utils import check

bin_name= sys.argv[1]

files = os.listdir('bin/')
version = len(files)+1

filemd5 = md5(open(bin_name).read()).hexdigest()
name = str(version)+'_'+filemd5
copyfile(bin_name,'bin/'+name)

dirname = 'json/'+str(version)
os.mkdir(dirname)

if version > 1: 
    dirname2 = 'json/'+str(version-1)
    os.system('cp '+dirname2+'/ok/ '+dirname+'/ok -r')
    os.mkdir(dirname+'/exception')
    os.mkdir(dirname+'/touch_flag')
    check(name,dirname2+'/exception',dirname)
    check(name,dirname2+'/touch_flag',dirname)

else:
    os.mkdir(dirname+'/ok')
    os.mkdir(dirname+'/exception')
    os.mkdir(dirname+'/touch_flag')
