# -*- coding: utf-8 -*-
__author__ = "lance"

#下载网页文件到本地文件夹
import os,urllib,time

#定义下载函数downLoadPicFromURL（本地文件夹，网页URL）
def downLoadFromURL(dest_dir, url):
    try:
        urllib.urlretrieve(url , dest_dir)
    except:
        print('\tError retrieving the URL:', dest_dir)
    time.sleep(4)

if __name__ == '__main__':

    typename = 'cyb'

    #设置下存储路径
    path=r'/Users/lance/Desktop/For嘉琳'

    f = open(path + "/code_" + typename + ".txt")             # 返回一个文件对象
    line = f.readline()             # 调用文件的 readline()方法

    while line:
        print(line)                 # 后面跟 ',' 将忽略换行符
        line = line.strip('\n')
        file_name=line + '.xls'   #文件名，包含文件格式
        dest_dir=os.path.join(path + "/" + typename, file_name)

        #设置下载链接的路径
        url="http://money.finance.sina.com.cn/corp/go.php/vDOWN_BalanceSheet/displaytype/4/stockid/"+line+"/ctrl/all.phtml"
        #运行
        downLoadFromURL(dest_dir, url)
        line = f.readline()

    f.close()


