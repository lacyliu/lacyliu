a=[]
class Contact:

    def __init__(self,id,name,tel):
        self.id=id;
        self.name=name;
        self.tel=tel;

    def add_record(b):
        global a
        a.append((b))
        print("添加成功")

    def qurey_record(c):
        global a
        if a.count(c)>0:
            print(c)
        else:
            print("未找到")
    #qurey_record([2,"zhang","234234234err"])
    def del_record(c):
        global a
        if a.count(c) > 0:
            a.remove(c)
        else:
            print("未有该联系人")
    def update_record(c):
        global a
        if a.count(c) > 0:
            c[-1]="455655443434"
            print("您修改的是"+c)
    #update_record([3,"li","3333333"])
def main(c):
    add="增加联系人"
    select="查找联系人"
    delete="删除联系人"
    update="修改联系人"
    opertion=input("请输入您的操作:")
    if opertion==add:
        Contact.add_record(c);
    elif opertion==select:
        Contact.qurey_record(c);
    elif opertion==delete:
        Contact.del_record(c);
    elif opertion==update:
        Contact.update_record()



if __name__ == '__main__':
    main([2,"liu","123123123"])


