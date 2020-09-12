import requests
import threading
from datetime import datetime

def execute_func(name):
    wavpath = './sample.wav'
    files = {'file': open(wavpath, 'rb')}
    r = requests.post('http://127.0.0.1:8090/upload', files=files)
    result = r.json()
    ast_text = result[0]
    asr_confidence = result[1]
    print('thread '+str(name)+': '+ast_text)
    print('thread '+str(name)+': '+str(asr_confidence))

if __name__ == '__main__':
    threads = []
    start = datetime.now()
    for i in range(50): # 循环创建500个线程
        t = threading.Thread(target=execute_func,args=(i,))
        threads.append(t)
    for t in threads: # 循环启动500个线程
        t.start()
        duration = datetime.now() - start
        print(duration)
    for t in threads:
        t.join() # 阻塞线程


