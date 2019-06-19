import time

COUNT_TO = 20
SLEEP_TIME = 1


def count(nr):
    for i in range(nr):
        time.sleep(SLEEP_TIME)
        print(i)


if __name__ == '__main__':
    print('Counting to {}.'.format(COUNT_TO))
    count(COUNT_TO)
    print('Done counting.')
