import os
import re


def get_sleep_record(filename):
    """Build a dict of dicts. Outer dict keys are the guard id's. Values are
    a dict with keys representing each hour the guard was asleep and values
    representing the number of times the guard was asleep on that minute.
    returns: {'id':{minute: total}}
    """
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
    return sleep_record

def get_sleepiest_guard(sleep_record):
    """Finds guard in sleep_record who spent the most total minutes asleep.

    returns: ('guard', total_minutes_slept)
    """
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
    """For a guard's sleep record, return the minute he was most often asleep.

    returns: (most_slept_minute, times_slept_that_minute)
    """
    sleepiest = 0, 0
    for minute in guard_sleep:
        if guard_sleep[minute] > sleepiest[1]:
            sleepiest = minute, guard_sleep[minute]
    return sleepiest


if __name__ == '__main__':
    sleep_record = get_sleep_record('1.txt')
    # (guard_id, most_slept_minute, total_minutes_slept_that_minute)
    max_sleep = '', 0, 0
    for guard in sleep_record:
        for minute in sleep_record[guard]:
            if sleep_record[guard][minute] > max_sleep[2]:
                max_sleep = guard, minute, sleep_record[guard][minute]
    print(max_sleep)
