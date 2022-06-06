
#本文件是读取Wikipedia的多语言信息的文件，以便于后续字典的建立
#需要enwiki-latest-langlinks.sql.gz文件放在目录下的wiki2022文件夹下
#读入文件：/wiki2022/enwiki-latest-langlinks.sql.gz
#写出文件：langlinks.txt
#写出文件格式：
#(langlinks.txt):[id_nl_nm]#list#记录了源界面id，对应的多语言语种nl(ISO 639-1),对应的语种下的内容nm

import gzip
import json
import os
path = os.getcwd()

#langlinks:[id_nl_nm]#list#记录了源界面id，对应的多语言语种nl(ISO 639-1),对应的语种下的内容nm


with gzip.open(path+'/wiki2022/enwiki-latest-langlinks.sql.gz', 'r')as ff3:
    i = 0
    zlist3 = []
    total = 0
    for lines in ff3:
        print(i)
        if(i > 30 and i < 1713):
            try:
                x = lines.decode(encoding='utf-8')
            except TypeError:
                i += 1
                continue
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
                if(b == 1 and x[i1].isdigit() == False and x[i1]+x[i1+1] == ",'"):
                    yi = int(yi)
                    b = 2
                    ynl = ''
                    i1 += 2
                    continue
                if(b == 2 and x[i1]+x[i1+1] != "',"):
                    ynl += x[i1]
                    i1 += 1
                    continue
                if(b == 2 and x[i1]+x[i1+1] == "',"):
                    b = 3
                    ynm = ''
                    iynm = x[i1+2]
                    i1 += 3
                    continue
                if(b == 3):
                    if(x[i1] == iynm and x[i1+1] == ')'):
                        zl = []
                        zl.append(yi)
                        zl.append(ynl)
                        zl.append(ynm)
                        if(yi != 0 and len(ynl) > 0 and len(ynm) > 0):
                            zlist3.append(zl)
                        total += 1
                        b = 0
                        i1 += 3
                        continue

                    else:
                        ynm += x[i1]
                        i1 += 1
                        continue
                i1 += 1

        i += 1

ff3.close()


js3 = json.dumps(zlist3)
file3 = open(path+'/langlinks.txt', 'w', encoding='utf-8')
file3.write(js3)
file3.close()
