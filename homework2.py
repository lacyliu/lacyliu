def de(func):
    def quanxian(username,password):
        func(username,password)
        if username == 'root' and password == '1223':
            print('你有权限')
            print("登录成功")
        else:
            print('你没有权限')
            print("账号或者密码错误")
    return quanxian
@de
def func1(name,password):
    return name, password
    #print("登录成功")

func1('root','1223')
import os

import os

allfile = []

l1=[]
l2=[]
l3=[]
l4=[]
def getallfile(path):
    allfilelist = os.listdir(path)
    for file in allfilelist:
        filepath = os.path.join(path, file)
        # 判断是不是文件夹
        if os.path.isdir(filepath):
            getallfile(filepath)
        allfile.append(filepath)
    return allfile
    #print(Max(os.path.getsize(allfile)))

def getdir(path):
    allfilelist = os.listdir(path)
    for file in allfilelist:
        filepath = os.path.join(path, file)
        # 判断是不是文件夹
        if os.path.isdir(filepath):
            l2.append(os.path.getsize(filepath))

    return l2
if __name__ == '__main__':

    path = "/Users/liusitong/PycharmProjects/paytm/"
    allfiles = getallfile(path)
    #print(max(allfiles))
    for item in allfiles:
        print (item)
        l1.append(os.path.getsize(item))
    print(max(l1))
    l2=getdir(path)
    print(max(l2))








