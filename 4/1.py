import os
import re


def f(filename):
    f = os.path.join(os.path.split(__file__)[0], filename)
    with open(f) as in_file:
        lines = in_file.readlines()
    lines.sort()
    p = re.compile(r'\[(.+)\]')
    sleep_record = {}
    for line in lines:
        timestamp = re.search(p, line).group(1)
        if '#' in line:
            guard = re.search(r'\#\d+', line).group()[1:]
        elif 'falls asleep' in line:
            start = int(timestamp.split(':')[1])
        else:
            end = int(timestamp.split(':')[1])
            for i in range(start, end):
                try:
                    sleep_record[guard]
                except KeyError:
                    sleep_record[guard] = {}
                try:
                    sleep_record[guard][i] += 1
                except KeyError:
                    sleep_record[guard][i] = 1

    sleepiest_guard = get_sleepiest_guard(sleep_record)
    print('sleepiest_guard=', sleepiest_guard)
    sleepiest_minute = get_sleepiest_minute(sleep_record[sleepiest_guard[0]])
    print(sleepiest_guard[0], sleepiest_minute[0])

def get_sleepiest_guard(sleep_record):
    sleepiest = '', 0
    for guard in sleep_record:
        sleep_mins = 0
        for minute in sleep_record[guard]:
            sleep_mins += sleep_record[guard][minute]
        if sleep_mins > sleepiest[1]:
            sleepiest = guard, sleep_mins
            print(sleepiest)
    return sleepiest

def get_sleepiest_minute(guard_sleep):
    sleepiest = 0, 0
    for minute in guard_sleep:
        if guard_sleep[minute] > sleepiest[1]:
            sleepiest = minute, guard_sleep[minute]
    return sleepiest


if __name__ == '__main__':
    f('1.txt')
