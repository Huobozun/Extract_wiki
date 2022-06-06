
#本文件加入了字典的多语言信息
#读入文件：categorytree-id-pre1.tsv、langlinks.txt
#写出文件：categorytree-id-pre2.tsv
import json
import os
path = os.getcwd()
#x=dict()
#x={000:{'name':'boy','lang':{'en':''},'parent_id':[1,2],'parent_nm':['',''],'sub_id':[3,4],'sub_nm':['',''],'pages_id':[,],'pages_nm':['','']},001:{'name':'girl','parent_id':[1,2],'sub_id':[3,4],'page_nm':['','']}}

#langlinks:[id_nl_nm]#list#记录了源界面id，对应的多语言语种nl(ISO 639-1),对应的语种下的内容nm
#x=dict()
#x={000:{'name':'boy','lang':{'en':'','zh':''},'parent_id':[1,2],'parent_nm':['',''],'sub_id':[3,4],'sub_nm':['',''],'pages_id':[,],'pages_nm':['','']}}

file = open(path+'/categorytree-id-pre1.tsv', 'r', encoding='utf-8')
js = file.read()
dic = json.loads(js)  # dic2为字典
file.close()


file1 = open(path+'/langlinks.txt', 'r', encoding='utf-8')
js1 = file1.read()
dic1 = json.loads(js1)  # dic3为list
file1.close()

for i0 in range(0, len(dic1)):
    print(i0, len(dic1))
    x = dic1[i0]
    if(str(x[0]) in dic):
        if(str(x[1]) not in dic[str(x[0])]['lang']):
            z = ''
            for i1 in range(0, len(x[2])):
                z += x[2][i1]
                if(x[2][i1] == ':'):
                    break
            zz = x[2].replace(z, '')
            dic[str(x[0])]['lang'][str(x[1])] = zz


js4 = json.dumps(dic)
file4 = open(path+'/categorytree-id-pre2.tsv', 'w', encoding='utf-8')
file4.write(js4)
file4.close()
