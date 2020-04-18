import queue
import threading,time,requests

requestnum=5
numproduce=20
numconsumers=20
lock=threading.Lock()
queue1=queue.Queue()
url="https://www.baidu.com/"
totalnum=0
def produce(idnum):
    for msgnum in range(requestnum):
        queue1.put("producer id =%d,count=%d" % (idnum,msgnum))
def consumer1(idnum):
    while True:
        try:
            dataQueue=queue1.get(block=False)
        except queue.Empty:
            break
        with lock:
            data = requests.get(url)
            print(data.status_code)
            print("当前消费者 consumer",idnum,"got =>",dataQueue )
        global totalnum
        totalnum=totalnum+1
        time.sleep(0.1)
        queue1.task_done()
if __name__ == '__main__':
    for i in range (numproduce):
        thread=threading.Thread(target=produce,args=(i,))
        thread.start()
    for i in range(numconsumers):
        thread = threading.Thread(target=consumer1, args=(i,))
        thread.start()

    queue1.join()
    print(totalnum)


#作业2：使用多进程写一个并发http，get请求的程序， 可设置并发数和请求总数，返回请求状态码
from multiprocessing import process, Queue, Lock, Process
import  queue
import time

requestnum=5
numproduce=20
numconsumers=20
url="https://www.baidu.com/"
totalnum1=0

def producer(idnum,dataQueue):
    for msgnum in range (requestnum):
        dataQueue.put("producer id=%d,count=%d" %(idnum,msgnum))
def consumer(idnum,dataQueue,lock):
    while True:
        try:
            data=dataQueue.get(block=False)
        except  queue.Empty:
            break
        with lock:
            json = requests.get(url)
            print(json.status_code)
            print("当前消费者 consumer", idnum, "got =>", data)
        global totalnum1
        totalnum1 = totalnum1 + 1
        print(totalnum1)
        time.sleep(0.1)

if __name__ == '__main__':
    lock=Lock()
    dataQueue=Queue()
    #consumers=[]
    #producers=[]
    for i in range(numproduce):
        p=Process(target=producer,args=(i,dataQueue))
        p.daemon=True
        p.start()
        p.join()

    for i in range(numconsumers):
        p=Process(target=consumer,args=(i,dataQueue,lock))
        p.daemon=True
        p.start()
        p.join()
    #print(totalnum1)


#作业3：get 与post的请求的区别
''' get请求一般是查数据，post请求一般是插入数据或者更改数据
    post请求一般比get请求安全，不会暴露在url地址栏里，get会把参数暴露在地址栏里
    get请求的数据最大不更超过4m，post可以更大
    
'''
#作业4：post请求
'''
    1.application/x-www-form-urlencoded
    2.multipart/form-data
    3.application/json
    4.text/xml
'''