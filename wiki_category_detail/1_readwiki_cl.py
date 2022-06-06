
#本文件是读取Wikipedia的category界面跳转信息的文件，以便于后续字典的建立
#需要enwiki-latest-categorylinks.sql.gz文件放在目录下的wiki2022文件夹下
#读入文件：/wiki2022/enwiki-latest-categorylinks.sql.gz
#写出文件：categorylinks.txt
#写出文件格式:
# (categorylinks.txt):[pageid,parent_name]#list#list#本文件记录了本页id以及本页的父类，可以对应构建关系
import gzip
import json
import os
path = os.getcwd()


#categorylinks:[pageid,parent_name]#list#本文件记录了本页id以及本页的父类，可以对应构建关系

with gzip.open(path+'/wiki2022/enwiki-latest-categorylinks.sql.gz', 'r')as ff1:
    i = 0
    zlist1 = []
    total = 0
    for lines in ff1:
        print(i)
        if(i > 43 and i < 25322):
            x = lines.decode(encoding='utf8', errors='ignore')

            b = 0  # 标记括号
            y = ''
            i1 = 0
            iq = 0  # 标记逗号
            while(i1 < len(x)):
                if(b == 0 and x[i1] == '(' and x[i1+1].isdigit()):
                    ys = ''
                    b = 1
                    i1 += 1
                    continue
                if(b == 1 and x[i1].isdigit()):
                    ys += x[i1]
                    i1 += 1
                    continue
                if(b == 1 and x[i1].isdigit() == False and x[i1] == ','):
                    ys = int(ys)
                    b = 2
                    yn = ''
                    i1 += 2
                    continue
                if(b == 2):
                    if(x[i1]+x[i1+1] == "',"):
                        yz = []
                        yz.append(ys)
                        yz.append(yn)
                        zlist1.append(yz)
                        total += 1
                        b = 0
                        i1 += 1
                        continue

                    else:
                        if(x[i1] == '_'):
                            yn += ' '
                            i1 += 1
                            continue
                        else:
                            yn += x[i1]
                            i1 += 1
                            continue
                i1 += 1

        i += 1
        if(i % 10 == 0):
            print(total)
            print(len(zlist1))

ff1.close()

#[[983, 'French_people_of_Spanish_descent']]
js1 = json.dumps(zlist1)
file1 = open(path+'/categorylinks.txt', 'w', encoding='utf-8')
file1.write(js1)
file1.close()
