import os

base = os.path.split(__file__)[0]
with open(os.path.join(base, '1.txt')) as infile:
    s = 0
    for line in infile:
        s += int(line[1:]) if line[0] == '+' else -(int(line[1:]))
print(s)
