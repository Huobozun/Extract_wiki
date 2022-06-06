

#本界面将Wikipedia字典以及page界面字典都整理成以term为key的字典形式，便于查询
#读入文件：pagetree-id.tsv、categorytree-id-pickle.tsv
#写出文件：pagetree-term.tsv、categorytree-term.tsv
#写出文件格式：
#(pagetree-term.tsv):{'term':{'lang':{'en':'','zh':''},'category_term':[,]}}
#(categorytree-term.tsv):{'term':{'lang':{'en':'','zh':''},'category_term':[,],'subcategory_term':[,],'page_term':[,]}}
import pickle
import os
path = os.getcwd()

file = open(path+'/pagetree-id.tsv', 'rb')
pk = file.read()
dicp = pickle.loads(pk)
file.close()

cl = dict()
for item in dicp:
    cl[dicp[item]['term'].lower()] = dict()
    cl[dicp[item]['term'].lower()]['lang'] = dicp[item]['lang']
    cl[dicp[item]['term'].lower()]['category_term'] = dicp[item]['category_nm']

pk2 = pickle.dumps(cl)
file1 = open(path+'/pagetree-term.tsv', 'wb')
file1.write(pk2)
file1.close()

file3 = open(path+'/categorytree-id-pickle.tsv', 'rb')
pk3 = file3.read()
dicc = pickle.loads(pk3)
file3.close()

cl2 = dict()
for item1 in dicc:
    cl2[dicc[item1]['name'].lower()] = dict()
    cl2[dicc[item1]['name'].lower()]['lang'] = dicc[item1]['lang']
    cl2[dicc[item1]['name'].lower()]['category_term'] = dicc[item1]['parent_nm']
    cl2[dicc[item1]['name'].lower()]['subcategory_term'] = dicc[item1]['sub_nm']
    cl2[dicc[item1]['name'].lower()]['page_term'] = dicc[item1]['pages_nm']


pk4 = pickle.dumps(cl2)
file4 = open(path+'/categorytree-term.tsv', 'wb')
file4.write(pk4)
file4.close()
