#本目录是抽取Wikipedia信息的集合文件  
#1-3是准备工作，需要先在路径下面建立文件夹/wiki2022,然后将enwiki-latest-categorylinks.sql.gz,enwiki-latest-langlinks.sql.gz,enwiki-latest-page.sql.gz放到该文件夹中，然后运行  
#4是以pageid作为key建立categorytree的文件  
#5是以pagetitle作为key建立categorytree的文件(此处的categorytree包括了hiddencategory的信息，用于后面streamlit展示所有信息)  
#6是将json储存方式改为pickle储存  
#7_show_streamlit_nm.py是用streamlit写的小demo,可以输入具体category查找相应信息  
 运行指令streamlit run 7_show_streamlit_nm.py，然后可以浏览器打开  
#8是以id作为key建立pagetree的文件(page页与其父类category的信息)  
#9是以pagetitle作为key建立pagetree和categorytree的文件(此处的categorytree不包括hiddencategory的信息)，用于search_wiki.py文件查询相应的信息  

#10_search_wiki.py可以通过命令行查找输出Wikipedia的categorytree:  
    usage: 10_search_wiki.py [-h] [-word WORD] [-type TYPE] [-cat CAT] [-sub SUB] [-file FILE]  

    wikipedia词条查询  

    optional arguments:  
    -h, --help  show this help message and exit  
    -word WORD  输入想要查询的词条  
    -type TYPE  输入想要查询的类型：'0'为仅输出词条pages,'1'为pages多语言描述,'2'为pages多语言加上categoties  
    -cat CAT    输入想要查询父类categories的阶数(默认为'1',表示查找一阶父类,'2'表示查询二阶父类,以此类推。'-1'表示查询所有父类)  
    -sub SUB    输入想要查询子类pages的阶数(默认为'0',表示不查找子类,'1'表示查询一阶子类的pages,以此类推。'-1'表示查询所有子类)  
    -file FILE  输入想要存储的文件名称  


 比如指令：python3 10_search_wiki.py -word 'Routes of administration' -type 2 -cat -1 -sub -1 -file Routes_of_administration_-1-1.json  
 表示查找'Routes of administration'所有子类词条信息，并且说出这些词条所有父类list,所有多语言信息，以文件Routes_of_administration_-1-1.json保存到当下路径  
