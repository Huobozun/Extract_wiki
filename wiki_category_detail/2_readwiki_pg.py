
#本文件是读取Wikipedia的界面信息的文件，以便于后续字典的建立
#需要enwiki-latest-page.sql.gz文件放在目录下的wiki2022文件夹下
#读入文件：/wiki2022/enwiki-latest-page.sql.gz
#写出文件：page-nm.txt、page-id.txt
#写出文件格式：
#(page-id.txt):{page_id:[namespace,name]}#dict#记录了所有界面的id,id下的界面类型namespace,以及界面标题name
#(page-nm.txt):{name:page_id}#dict#记录了页面标题和id的关系（仅namespace==14也就是说使category的界面）
import gzip
import json
import os
path = os.getcwd()


#page:{page_id:[namespace,name]}#dict#记录了所有界面的id,id下的界面类型namespace,以及界面标题name
#page2:{name:page_id}#dict#记录了页面标题和id的关系（仅namespace==14也就是说使category的界面）


with gzip.open(path+'/wiki2022/enwiki-latest-page.sql.gz', 'r')as ff2:
    i = 0
    zlist2 = dict()
    total = 0
    for lines in ff2:
        print(i)
        if(i > 50 and i < 6659):
            x = lines.decode(encoding='utf-8')
            b = 0  # 标记括号
            i1 = 0
            iq = 0  # 标记逗号
            while(i1 < len(x)):
                if(b == 0 and x[i1] == '(' and x[i1+1].isdigit()):
                    yi = ''
                    b = 1
                    i1 += 1
                    continue
                if(b == 1 and x[i1].isdigit()):
                    yi += x[i1]
                    i1 += 1
                    continue
                if(b == 1 and x[i1].isdigit() == False and x[i1] == ','):
                    yi = int(yi)
                    b = 2
                    yns = ''
                    i1 += 1
                    continue
                if(b == 2 and x[i1].isdigit()):
                    yns += x[i1]
                    i1 += 1
                    continue
                if(b == 2 and x[i1].isdigit() == False and x[i1] == ','):
                    if(yns == ''):
                        yns = -1
                    yns = int(yns)
                    b = 3
                    ynm = ''
                    iynm = x[i1+1]
                    i1 += 2
                    continue
                if(b == 3):
                    if(x[i1] == iynm and x[i1+1] == ','):
                        zn = []
                        zn.append(yns)
                        zn.append(ynm)
                        if(yi not in zlist2):
                            zlist2[yi] = zn
                        total += 1
                        b = 0
                        i1 += 1
                        continue

                    else:
                        if(x[i1] == '_'):
                            ynm += ' '
                            i1 += 1
                            continue
                        else:
                            ynm += x[i1]
                            i1 += 1
                            continue
                i1 += 1

        i += 1

ff2.close()


cl0 = dict()
for i in zlist2:  # 构造{name:pageid}
    if(zlist2[i][0] == 14):  # category类
        if(zlist2[i][1] not in cl0):
            cl0[zlist2[i][1]] = i

js22 = json.dumps(cl0)
file22 = open(path+'/page-nm.txt', 'w', encoding='utf-8')
file22.write(js22)
file22.close()

#{'000':[namespace,name]}
js2 = json.dumps(zlist2)
file2 = open(path+'/page-id.txt', 'w', encoding='utf-8')
file2.write(js2)
file2.close()
