COUNT_TO = 100


def count(nr):
    for i in range(nr):
        print(i)


if __name__ == '__main__':
    print('Counting to {}.'.format(COUNT_TO))
    count(COUNT_TO)
    print('Done counting.')
