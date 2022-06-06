
# 本界面是建立一个page界面对应的categories信息字典的文件，以便于查找page界面的信息
#读入文件：categorytree-id-pickle.tsv
#写出文件：pagetree-id.tsv
import pickle
import json
import os
path = os.getcwd()

# 建立pages页x={page_id:{'term':'','lang':{'en':'','zh':''},'category_id':[,],'category_nm':[,]}}
file = open(path+'/categorytree-id-pickle.tsv', 'rb')
dicr = file.read()
dicrr = pickle.loads(dicr)
file.close()


a = []
print(dicrr['15961454']['name'])  # Hidden categories
a = dicrr['15961454']['sub_nm']  # 不用Hidden categories的内容

dicp = dict()
for item in dicrr:
    if dicrr[item]['name'] not in a:
        for ipages in range(0, len(dicrr[item]['pages_id'])):
            if str(dicrr[item]['pages_id'][ipages]) not in dicp:
                dicp[str(dicrr[item]['pages_id'][ipages])] = dict()
                dicp[str(dicrr[item]['pages_id'][ipages])
                     ]['term'] = dicrr[item]['pages_nm'][ipages]
                dicp[str(dicrr[item]['pages_id'][ipages])]['lang'] = dict()
                dicp[str(dicrr[item]['pages_id'][ipages])
                     ]['lang']['en'] = dicrr[item]['pages_nm'][ipages]
                dicp[str(dicrr[item]['pages_id'][ipages])]['category_id'] = []
                dicp[str(dicrr[item]['pages_id'][ipages])]['category_nm'] = []
            dicp[str(dicrr[item]['pages_id'][ipages])
                 ]['category_id'].append(item)
            dicp[str(dicrr[item]['pages_id'][ipages])
                 ]['category_nm'].append(dicrr[item]['name'])



#下面补充了page界面的多语言信息，丰富了page界面字典
#读入文件：langlinks.txt
#写出文件：pagetree-id.tsv


#建立pages页x={page_id:{'term':'','lang':{'en':'','zh':''},'category_id':[,],'category_nm':[,]}}


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




