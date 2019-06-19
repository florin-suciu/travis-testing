import os
import threading
import time

THREAD_COUNT = 3
COUNT_TO = 400
SLEEP_TIME = 1


def count(nr, raise_exception):
    for i in range(nr):
        if (i == 303) and raise_exception:
            raise Exception('Something went wrong.')
        time.sleep(SLEEP_TIME)
        print(str(i) * 100)


if __name__ == '__main__':
    print('Counting to {}.'.format(COUNT_TO))
    threads = []
    for index in range(THREAD_COUNT):
        raise_exc = False if index != 0 else True
        t = threading.Thread(target=count, args=(COUNT_TO, raise_exc))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('Secret is: {}.'.format(os.getenv('SECRET')))
    print('Done counting.')
