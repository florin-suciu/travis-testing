import os
import threading
import time

THREAD_COUNT = 3
COUNT_TO = 25
SLEEP_TIME = 1


def count(nr, raise_exception):
    for i in range(nr):
        time.sleep(SLEEP_TIME)
        print(i)
    if raise_exception:
        raise Exception('Something went wrong.')


if __name__ == '__main__':
    print('Counting to {}.'.format(COUNT_TO))
    raise_exc = False
    threads = []
    for index in range(THREAD_COUNT):
        if index == 1:
            raise_exc = True
        t = threading.Thread(target=count, args=(COUNT_TO, raise_exc))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('Secret is: {}.'.format(os.getenv('SECRET')))
    print('Done counting.')
