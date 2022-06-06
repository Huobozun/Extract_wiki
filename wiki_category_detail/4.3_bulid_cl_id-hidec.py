

#本文件将Wikipedia的hidden categories与categories区别开
#读入文件：categorytree-id-pre2.tsv
#写出文件：categorytree-id.tsv
import json
import os
path = os.getcwd()
#x=dict()
#x={000:{'name':'boy','lang':{'en':'','zh':''},'parent_id':[1,2],'parent_nm':['',''],'sub_id':[3,4],'sub_nm':['',''],'pages_id':[,],'pages_nm':['','']}}


#x=dict()最后字典的形式如下：
#x={'pageid':{'name':'','lang':{'en':''，‘zh':''},'parent_id':[,],'parent_nm':['',''],'hidden_parent_id':[,],'hidden_parent_nm':['',''],'sub_id':[,],'sub_nm':['',''],'pages_id':[,],'pages_nm':['','']}}


file = open(path+'/categorytree-id-pre2.tsv', 'r', encoding='utf-8')
js = file.read()
dic = json.loads(js)  # dic2为字典
file.close()


a = []
print(dic['15961454']['name'])
a = dic['15961454']['sub_nm']

for i0 in dic:
    x = dic[i0]
    xp = []
    xpi = []
    xph = []
    xphi = []
    for i1 in range(0, len(x['parent_nm'])):
        if(x['parent_nm'][i1] in a):
            xph.append(x['parent_nm'][i1])
            xphi.append(x['parent_id'][i1])
        else:
            xp.append(x['parent_nm'][i1])
            xpi.append(x['parent_id'][i1])

    dic[i0]['parent_id'] = xpi
    dic[i0]['parent_nm'] = xp
    dic[i0]['hidden_parent_id'] = xphi
    dic[i0]['hidden_parent_nm'] = xph


js4 = json.dumps(dic)
file4 = open(path+'/categorytree-id.tsv', 'w', encoding='utf-8')
file4.write(js4)
file4.close()
