import requests
from bs4 import BeautifulSoup
import queue
import threading

from lock import lock

start_page = "http://www.163.com"
domain = "163.com"
url_queue = queue.Queue()
seen = set()

seen.add(start_page)
url_queue.put(start_page)
lock = threading.Lock()


#def sotre(url):
    #pass



def extract_urls(url):
    urls = []
    html = requests.get(url)
    soup = BeautifulSoup(html.content, "html.parser")
    for e in soup.findAll('a'):
    #如果没有href属性，就给他的默认值，#是给key的默认值
        url = e.attrs.get('href', '#')
        urls.append(url)
    return urls


def consumer():
    while True:
        if not url_queue.empty():

            current_url = url_queue.get()
            with lock:
                print(current_url)
                producer(current_url)
            url_queue.task_done()
        else:
            break
def producer(current_url):
    while True:
        for next_url in extract_urls(current_url):
            if next_url not in seen and domain in next_url:
                seen.add(next_url)
                url_queue.put(next_url)


if __name__ == '__main__':
    thread1=threading.Thread(target=consumer)
    thread1.start()
    thread2=threading.Thread(target=producer,args=(url_queue.get()))
    thread2.start()