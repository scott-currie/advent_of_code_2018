import os


def get_map(filename):
    f = os.path.join(os.path.split(__file__)[0], filename)
    claimed = {}
    with open(f) as infile:
        for line in infile:
            if not line.startswith('.'):
                data = line.split('@ ')[1].split(': ')
                coords = tuple([int(n) for n in data[0].split(',')])
                width, height = [int(n) for n in data[1].split('x')]
                # print(coords, width, height)
                for col in range(coords[0], coords[0] + width):
                    for row in range(coords[1], coords[1] + height):
                        # print(col, row)
                        try:
                            claimed[(col, row)] += 1
                            # print(col, row)
                        except KeyError:
                            claimed[(col, row)] = 1

    return claimed

def check_map(filename, claimed):
    f = os.path.join(os.path.split(__file__)[0], filename)
    with open(f) as infile:
        for line in infile:
            if not line.startswith('.'):
                data = line.split('@ ')[1].split(': ')
                coords = tuple([int(n) for n in data[0].split(',')])
                width, height = [int(n) for n in data[1].split('x')]
                # print(coords, width, height)
                overlaps = False
                for col in range(coords[0], coords[0] + width):
                    for row in range(coords[1], coords[1] + height):
                        if claimed[(col, row)] != 1:
                            overlaps = True
                            break
                    if overlaps:
                        break
                else:
                    print(line)

if __name__ == '__main__':
    filename = '1.txt'
    check_map(filename, get_map(filename))