import random
import time
import queue
from threading import Thread

queues = queue.Queue(10)


class Producer(Thread):
    def run(self):
        while True:
            elem = random.randrange(9)
            queues.put(elem)
            print("厨师 {} 做了 {} 饭 --- 还剩 {} 饭没卖完".format(self.name, elem, queues.qsize()))
            time.sleep(random.random())


class Consumer(Thread):
    def run(self):
        while True:
            elem = queues.get()
            print("吃货{} 吃了 {} 饭 --- 还有 {} 饭可以吃".format(self.name, elem, queues.qsize()))
            time.sleep(random.random())


def main():
    for i in range(3):
        p = Producer()
        p.start()
    for i in range(2):
        c = Consumer()
        c.start()


if __name__ == '__main__':
    main()
