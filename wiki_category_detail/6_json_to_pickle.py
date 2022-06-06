

#本文件是将前面写的json.dumps改为pickle.dumps，以求提高读写文件速度
#读入文件：categorytree-id.tsv、categorytree-nm.tsv
#写出文件：categorytree-id-pickle.tsv、categorytree-nm-pickle.tsv
import json
import pickle
import os
path = os.getcwd()


file = open(path+'/categorytree-id.tsv', 'rb')
idicr = file.read()
idicrr = json.loads(idicr)
file.close()

idicw = pickle.dumps(idicrr)
file1 = open(path+'/categorytree-id-pickle.tsv', 'wb')
file1.write(idicw)
file1.close()

file2 = open(path+'/categorytree-nm.tsv', 'rb')
ndicr = file2.read()
ndicrr = json.loads(ndicr)
file2.close()

ndicw = pickle.dumps(ndicrr)
file3 = open(path+'/categorytree-nm-pickle.tsv', 'wb')
file3.write(ndicw)
file3.close()
