
#本文件为建立Wikipedia字典的整合文件，包括了初步建立categories界面内容，加入多语言信息，区分hidden category
#4.1，4.2，4.3为本文件的拆分文件，避免本文件运行内存太大的问题
#读入文件：langlinks.txt、page-id.txt、page-nm.txt、categorylinks.txt
#写出文件：categorytree-id.tsv
import json
import pickle
import os
path = os.getcwd()

#langlinks:[id_nl_nm]#list#记录了源界面id，对应的多语言语种nl(ISO 639-1),对应的语种下的内容nm
#page:{page_id:[namespace,name]}#dict#记录了所有界面的id,id下的界面类型namespace,以及界面标题name
#page2:{name:page_id}#dict#记录了页面标题和id的关系（仅namespace==14也就是说使category的界面）
#categorylinks:[pageid,parent_name]#list#本文件记录了本页id以及本页的父类，可以对应构建关系

#x=dict()最后字典的形式如下：
#x={'pageid':{'name':'','lang':{'en':''，‘zh':''},'parent_id':[,],'parent_nm':['',''],'hidden_parent_id':[,],'hidden_parent_nm':['',''],'sub_id':[,],'sub_nm':['',''],'pages_id':[,],'pages_nm':['','']}}

file1 = open(path+'/langlinks.txt', 'r', encoding='utf-8')
js1 = file1.read()
dic1 = json.loads(js1)  # dic1为list
file1.close()

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

#建立字典
cl = dict()
for item0 in dic3:#从每个category跳转的源头先通过page-id.txt判断本页类型是category页还是page页，然后加入到category字典中（category页作为key加入字典，再添加本key的跳转父类；page页作为对应跳转父类的page_nm加入字典）
    #print(i0, len(dic3))
    if (str(item0[0]) not in dic2) or (str(item0[1]) not in dic22):  # 没找到该界面，则跳过（category可能会有很多跳转，我们只查找在page中出现的）
        continue
    if dic2[str(item0[0])][0] == 14:  # namespace=14代表本页是一个category页，则添加该category页到cl字典key中
        if str(item0[0]) not in cl:  # 本页page_id不在cl字典key中，则新添
            cl[str(item0[0])] = dict()
            cl[str(item0[0])]['name'] = dic2[str(item0[0])][1]
            cl[str(item0[0])]['lang'] = dict()
            cl[str(item0[0])]['lang']['en'] = dic2[str(
                item0[0])][1]  # 本身是英文字典，所以自带一个多语言字典中的'en'
            cl[str(item0[0])]['parent_id'] = []
            cl[str(item0[0])]['parent_nm'] = []
            cl[str(item0[0])]['hidden_parent_id'] = []
            cl[str(item0[0])]['hidden_parent_nm'] = []
            cl[str(item0[0])]['sub_id'] = []
            cl[str(item0[0])]['sub_nm'] = []
            cl[str(item0[0])]['pages_id'] = []
            cl[str(item0[0])]['pages_nm'] = []
        cl[str(item0[0])]['parent_id'].append(
            dic22[str(item0[1])])  # 添加父类（父类需要在page-nm.txt中通过name对应找到page-id)
        cl[str(item0[0])]['parent_nm'].append(item0[1])
    if dic2[str(item0[0])][0] == 0:  # namespace=0代表本页是一个page页,本页不是category页，不加入cl的key,作为父类的page加入cl字典
        if str(item0[1]) not in dic22:  # 父类不是category页，不记录，跳过
            continue
        # 本页parent_id不在cl字典key中，则先新添该category，再添加page
        if str(dic22[item0[1]]) not in cl:
            cl[str(dic22[item0[1]])] = dict()
            cl[str(dic22[item0[1]])]['name'] = item0[1]
            cl[str(dic22[item0[1]])]['lang'] = dict()
            cl[str(dic22[item0[1]])]['lang']['en'] = item0[1]
            cl[str(dic22[item0[1]])]['parent_id'] = []
            cl[str(dic22[item0[1]])]['parent_nm'] = []
            cl[str(dic22[item0[1]])]['hidden_parent_id'] = []
            cl[str(dic22[item0[1]])]['hidden_parent_nm'] = []
            cl[str(dic22[item0[1]])]['sub_id'] = []
            cl[str(dic22[item0[1]])]['sub_nm'] = []
            cl[str(dic22[item0[1]])]['pages_id'] = []
            cl[str(dic22[item0[1]])]['pages_nm'] = []
        cl[str(dic22[item0[1]])]['pages_id'].append(item0[0])
        cl[str(dic22[item0[1]])]['pages_nm'].append(
            dic2[str(item0[0])][1])

#根据父类子类关系添加sub_id
for i1 in cl:
    for i2 in range(0, len(cl[str(i1)]['parent_id'])):
        if str(cl[str(i1)]['parent_id'][i2]) not in cl:
            continue
        cl[str(cl[str(i1)]['parent_id'][i2])]['sub_id'].append(i1)
        cl[str(cl[str(i1)]['parent_id'][i2])
           ]['sub_nm'].append(cl[str(i1)]['name'])


#根据languagelink建立多语言字典
for item3 in dic1:
    x = item3
    if str(x[0]) in cl:
        if str(x[1]) not in cl[str(x[0])]['lang']:
            zb = ''
            for i4 in range(0, len(x[2])):
                zb += x[2][i4]
                if x[2][i4] == ':':
                    break
            zz = x[2].replace(zb, '')#此处是为了删除多语言信息中存在的'category:'内容，否则多语言信息会显示为'category:cancer',而不是'cancer'
            cl[str(x[0])]['lang'][str(x[1])] = zz


#区分hidden-category和category
a = []
#print(cl['15961454']['name'])
# 所有的hidden-category都记录在这个界面里面，只需要根据是不是这里面的来摘取hidden-category即可
a = cl['15961454']['sub_nm']
for item5 in cl:
    x = cl[item5]
    xp = []
    xpi = []
    xph = []
    xphi = []
    for i6 in range(0, len(x['parent_nm'])):
        if x['parent_nm'][i6] in a:
            xph.append(x['parent_nm'][i6])
            xphi.append(x['parent_id'][i6])
        else:
            xp.append(x['parent_nm'][i6])
            xpi.append(x['parent_id'][i6])

    cl[item5]['parent_id'] = xpi
    cl[item5]['parent_nm'] = xp
    cl[item5]['hidden_parent_id'] = xphi
    cl[item5]['hidden_parent_nm'] = xph


#写入文件
js4 = pickle.dumps(cl)
file4 = open(path+'/categorytree-id-pickle.tsv', 'w', encoding='utf-8')
file4.write(js4)
file4.close()
