

#本文件是建立一个用名称为key的Wikipedia字典，直接输入名称（小写）就可查询字典内容
#读入文件：categorytree-id.tsv
#写出文件：categorytree-nm.tsv
import pickle
import os
path = os.getcwd()
#x=dict()
#之前为x={000:{'name':'boy','lang':{'en':'','zh':''},'parent_id':[1,2],'parent_nm':['',''],'hidden_parent_id':[,],'hidden_parent_nm':['',''],'sub_id':[3,4],'sub_nm':['',''],'pages_id':[,],'pages_nm':['','']}}

#之后为x={name:{'lang':{'en':'','zh':''},'parent_nm':['',''],'hidden_parent_nm':['',''],'sub_nm':['',''],'pages_nm':['','']}}


file = open(path+'/categorytree-id-pickle.tsv',
            'r', encoding='utf-8')
js = file.read()
dic = pickle.loads(js)  # dic2为字典
file.close()

cl = dict()
for i0 in dic:
    x = str(dic[str(i0)]['name']).lower()
    cl[x] = dict()
    cl[x]['lang'] = dic[str(i0)]['lang']
    cl[x]['hidden_parent_nm'] = dic[str(i0)]['hidden_parent_nm']
    cl[x]['parent_nm'] = dic[str(i0)]['parent_nm']
    cl[x]['sub_nm'] = dic[str(i0)]['sub_nm']
    cl[x]['pages_nm'] = dic[str(i0)]['pages_nm']


js3 = pickle.dumps(cl)
file3 = open(path+'/categorytree-nm-pickle.tsv', 'w', encoding='utf-8')
file3.write(js3)
file3.close()
