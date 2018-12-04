import os


f = os.path.join(os.path.split(__file__)[0], '1.txt')
threes, twos = 0, 0
with open(f) as infile:
    for line in infile:
        line = sorted(list(line))
        for c in set(line):
            if line.count(c) == 2:
                twos += 1
                break
        for c in set(line):
            if line.count(c) == 3:
                threes += 1
                break
print(threes * twos)
