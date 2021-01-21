import multiprocessing
import time
import random
import datetime


def work(secs):
    time.sleep(secs)
    print(f'{secs} and now {datetime.datetime.now()}')


if __name__ == "__main__":
    print(datetime.datetime.now())
    for i in range(20):
        sec = random.random()*3
        proc = multiprocessing.Process(target=work, args=(sec,))
        proc.start()
