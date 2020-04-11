def de(func):
    def quanxian(username,password):
        func(username,password)
        if username == 'root' and password == '1223':
            print('你有权限')
        else:
            print('你没有权限')
    return quanxian
@de
def func1(name,password):
    return name, password
func1('root','1223')
import os

import os

allfile = []

l=[]
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

if __name__ == '__main__':

    path = "/Users/liusitong/PycharmProjects/paytm/test/lacyliu"
    allfiles = getallfile(path)
    #print(max(allfiles))
    for item in allfiles:
        print (item)
        l.append(os.path.getsize(item))
    print(max(l))





