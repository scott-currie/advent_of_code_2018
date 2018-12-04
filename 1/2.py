import os


def f():
    base = os.path.split(__file__)[0]
    r = set([0])
    s = 0
    while True:
        with open(os.path.join(base, '2.txt')) as infile:
            for line in infile:
                s += int(line[1:]) if line[0] == '+' else -(int(line[1:]))
                # print(s)
                if s in r:
                    return s

                else:
                    r.add(s)


if __name__ == '__main__':
    print(f())
