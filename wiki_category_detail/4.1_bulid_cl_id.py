
#本文件初步建立Wikipedia字典，以page_id作为key，收录所有的categories界面内容
#读入文件：page-id.txt、page-nm.txt、categorylinks.txt
#写出文件：categorytree-id-pre1.tsv
import json
import os
path = os.getcwd()


#page:{page_id:[namespace,name]}#dict#记录了所有界面的id,id下的界面类型namespace,以及界面标题name
#page2:{name:page_id}#dict#记录了页面标题和id的关系（仅namespace==14也就是说使category的界面）
#categorylinks:[pageid,parent_name]#list#本文件记录了本页id以及本页的父类，可以对应构建关系

#x=dict()
#x={000:{'name':'boy','lang':{'en':''},'parent_id':[1,2],'parent_nm':['',''],'sub_id':[3,4],'sub_nm':['',''],'pages_id':[,],'pages_nm':['','']},001:{'name':'girl','parent_id':[1,2],'sub_id':[3,4],'page_nm':['','']}}

file2 = open(path+'/page-id.txt', 'r', encoding='utf-8')
js2 = file2.read()
dic2 = json.loads(js2)  # dic2为字典
file2.close()

file22 = open(path+'/page-nm.txt', 'r', encoding='utf-8')
js22 = file22.read()
dic22 = json.loads(js22)  # dic22为字典
file22.close()


file3 = open(path+'/categorylinks.txt', 'r', encoding='utf-8')
js3 = file3.read()
dic3 = json.loads(js3)  # dic3为list
file3.close()

cl = dict()
for i0 in range(0, len(dic3)):
    print(i0, len(dic3))
    if((str(dic3[i0][0]) not in dic2) or (str(dic3[i0][1]) not in dic22)):  # 没找到该界面，则跳过
        continue
    if(dic2[str(dic3[i0][0])][0] == 14):  # 本页是一个category页，则添加该category页到cl字典key中
        if(str(dic3[i0][0]) not in cl):  # 本页page_id不在cl字典key中，则新添
            cl[str(dic3[i0][0])] = dict()
            cl[str(dic3[i0][0])]['name'] = dic2[str(dic3[i0][0])][1]
            cl[str(dic3[i0][0])]['lang'] = dict()
            cl[str(dic3[i0][0])]['lang']['en'] = dic2[str(
                dic3[i0][0])][1]  # 本身是英文字典，所以自带一个多语言字典中的'en'
            cl[str(dic3[i0][0])]['parent_id'] = []
            cl[str(dic3[i0][0])]['parent_nm'] = []
            cl[str(dic3[i0][0])]['sub_id'] = []
            cl[str(dic3[i0][0])]['sub_nm'] = []
            cl[str(dic3[i0][0])]['pages_id'] = []
            cl[str(dic3[i0][0])]['pages_nm'] = []
        cl[str(dic3[i0][0])]['parent_id'].append(
            dic22[str(dic3[i0][1])])  # 添加父类
        cl[str(dic3[i0][0])]['parent_nm'].append(dic3[i0][1])
    if(dic2[str(dic3[i0][0])][0] == 0):  # 本页是一个page页,本页不是category页，不加入cl的key,作为父类的page加入cl字典
        if(str(dic3[i0][1]) not in dic22):  # 父类不是category页，不记录，跳过
            continue
        # 本页parent_id不在cl字典key中，则先新添该category，再添加page
        if(str(dic22[dic3[i0][1]]) not in cl):
            cl[str(dic22[dic3[i0][1]])] = dict()
            cl[str(dic22[dic3[i0][1]])]['name'] = dic3[i0][1]
            cl[str(dic22[dic3[i0][1]])]['lang'] = dict()
            cl[str(dic22[dic3[i0][1]])]['lang']['en'] = dic3[i0][1]
            cl[str(dic22[dic3[i0][1]])]['parent_id'] = []
            cl[str(dic22[dic3[i0][1]])]['parent_nm'] = []
            cl[str(dic22[dic3[i0][1]])]['sub_id'] = []
            cl[str(dic22[dic3[i0][1]])]['sub_nm'] = []
            cl[str(dic22[dic3[i0][1]])]['pages_id'] = []
            cl[str(dic22[dic3[i0][1]])]['pages_nm'] = []
        cl[str(dic22[dic3[i0][1]])]['pages_id'].append(dic3[i0][0])
        cl[str(dic22[dic3[i0][1]])]['pages_nm'].append(
            dic2[str(dic3[i0][0])][1])


for i1 in cl:  # 根据父类子类关系添加sub_id
    for i2 in range(0, len(cl[str(i1)]['parent_id'])):
        if(str(cl[str(i1)]['parent_id'][i2]) not in cl):
            continue
        cl[str(cl[str(i1)]['parent_id'][i2])]['sub_id'].append(i1)
        cl[str(cl[str(i1)]['parent_id'][i2])
           ]['sub_nm'].append(cl[str(i1)]['name'])


js4 = json.dumps(cl)
file4 = open(path+'/categorytree-id-pre1.tsv', 'w', encoding='utf-8')
file4.write(js4)
file4.close()
