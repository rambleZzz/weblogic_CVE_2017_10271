#coding:utf-8
import threading
import Queue
import weblogic_CVE_2017_10271
import os

class RunPoc(threading.Thread):
    def __init__(self,que):
        threading.Thread.__init__(self)
        self._que = que
    def run(self):
        while True:
            if self._que.empty():
                break
            url = self._que.get(timeout=0.5)
            #print url
            weblogic_CVE_2017_10271.verify(url)

def main():
    que = Queue.Queue()
    thread_count = 3
    ths = []
    with open('url.txt','r') as f:
        for url in f:
            url=url.strip('\n')
            que.put(url)
            print url
    for i in range(thread_count):
        th = RunPoc(que)
        th.start()
        ths.append(th)
    try:
        while True:
            alive = False
            for t in ths:
                alive = alive or t.is_alive()
            if not alive:
                print 'Done'
                break
    except KeyboardInterrupt:
        print 'exit'
        os._exit(0)

if __name__ == '__main__':
    main()


