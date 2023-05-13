# coding:utf-8
# time: 2023/5/12
# author: evan
# 进程间通信
import json
import multiprocessing


class Work:
    def __init__(self, queue):
        self.queue = queue

    def send(self, msg):
        if not isinstance(msg, str):
            msg = json.dumps(msg)
        self.queue.put(msg)

    def receive(self):
        while True:
            result = self.queue.get()
            try:
                res = json.loads(result)
            except Exception as e:
                res = result
                print(e)
            print(f'recv is {res}')


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    work = Work(queue)

    send = multiprocessing.Process(target=work.send, args=('hehe isis',))
    recv = multiprocessing.Process(target=work.receive)

    send.start()
    recv.start()
    send.join()
    recv.terminate()
