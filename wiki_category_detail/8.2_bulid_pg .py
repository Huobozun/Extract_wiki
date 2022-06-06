

#本界面补充了page界面的多语言信息，丰富了page界面字典
#读入文件：pagetree-id-pre1.tsv、langlinks.txt
#写出文件：pagetree-id.tsv
import json
import pickle
import os
path = os.getcwd()

#建立pages页x={page_id:{'term':'','lang':{'en':'','zh':''},'category_id':[,],'category_nm':[,]}}
file = open(path+'/pagetree-id-pre1.tsv', 'rb')
pk = file.read()
dicp = pickle.loads(pk)
file.close()

file1 = open(path+'/langlinks.txt', 'r', encoding='utf-8')
js1 = file1.read()
dic1 = json.loads(js1)  # dic3为list
file1.close()


for i0 in range(0, len(dic1)):
    print(i0, len(dic1))
    x = dic1[i0]
    if(str(x[0]) in dicp):
        if(str(x[1]) not in dicp[str(x[0])]['lang']):

            dicp[str(x[0])]['lang'][str(x[1])] = x[2]


pk2 = pickle.dumps(dicp)
file2 = open(path+'/pagetree-id.tsv', 'wb')
file2.write(pk2)
file2.close()
